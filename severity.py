import cv2
import numpy as np
from PIL import Image

def calculate_disease_severity(image_input, is_healthy: bool = False):
    """
    Estimates the visible percentage severity of plant leaf disease by segmenting 
    the total leaf surface and calculating the proportion of necrotic, chlorotic, 
    and diseased lesion tissue.

    Args:
        image_input: str (file path), PIL.Image, or numpy.ndarray
        is_healthy: bool indicating whether the diagnostic model classified the plant as healthy

    Returns:
        dict containing:
            - severity_score: float (0.0 to 100.0)
            - stage: str (Healthy, Mild, Moderate, Severe, Critical)
            - color: str (hex color code for UI rendering)
            - overlay_image: PIL.Image highlighting lesion spots (or original if healthy)
    """
    if is_healthy:
        if isinstance(image_input, str):
            orig_pil = Image.open(image_input).convert("RGB")
        elif isinstance(image_input, Image.Image):
            orig_pil = image_input.convert("RGB")
        else:
            orig_pil = Image.fromarray(image_input)

        return {
            "severity_score": 0.0,
            "stage": "Healthy / No Infection",
            "color": "#16a34a",
            "overlay_image": orig_pil
        }

    # Convert image input to cv2 numpy array (BGR)
    if isinstance(image_input, str):
        img = cv2.imread(image_input)
        if img is None:
            pil_temp = Image.open(image_input).convert("RGB")
            img = cv2.cvtColor(np.array(pil_temp), cv2.COLOR_RGB2BGR)
    elif isinstance(image_input, Image.Image):
        img_rgb = np.array(image_input.convert("RGB"))
        img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    elif isinstance(image_input, np.ndarray):
        img = image_input.copy()
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:
        raise ValueError("Unsupported image input type.")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 1. Segment the leaf from the background
    # Plant foliage typically has Hue in [10, 100], Saturation > 25, Value in [25, 255]
    lower_leaf = np.array([10, 25, 25])
    upper_leaf = np.array([105, 255, 255])
    leaf_mask = cv2.inRange(hsv, lower_leaf, upper_leaf)

    # Clean the mask using morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_CLOSE, kernel)
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_OPEN, kernel)

    total_leaf_pixels = int(np.sum(leaf_mask > 0))

    if total_leaf_pixels < 100:
        # Fallback if leaf mask couldn't segment properly
        total_leaf_pixels = img.shape[0] * img.shape[1]
        leaf_mask = np.ones((img.shape[0], img.shape[1]), dtype=np.uint8) * 255

    # 2. Segment healthy green tissue (Hue between ~35 and ~85, healthy green)
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green_in_leaf = cv2.bitwise_and(green_mask, green_mask, mask=leaf_mask)

    # 3. Diseased tissue: leaf tissue displaying chlorosis (yellowing), necrosis (brown/black), or spots
    diseased_mask = cv2.bitwise_and(leaf_mask, cv2.bitwise_not(green_in_leaf))
    diseased_pixels = int(np.sum(diseased_mask > 0))

    severity_pct = (diseased_pixels / float(total_leaf_pixels)) * 100.0
    severity_pct = round(min(max(severity_pct, 1.0), 100.0), 2)

    # Categorize clinical severity stages
    if severity_pct < 10.0:
        stage = "Mild (Early Stage)"
        color = "#eab308" # Amber
    elif severity_pct < 25.0:
        stage = "Moderate"
        color = "#f97316" # Orange
    elif severity_pct < 50.0:
        stage = "Severe"
        color = "#ef4444" # Red
    else:
        stage = "Critical / Extensive"
        color = "#991b1b" # Dark Red

    # 4. Create visual heatmap overlay highlighting diseased regions in red
    overlay = img.copy()
    overlay[diseased_mask > 0] = [0, 0, 230] # High-visibility red tint on lesions
    blended = cv2.addWeighted(img, 0.65, overlay, 0.35, 0)
    
    # Draw subtle contour around detected lesions
    contours, _ = cv2.findContours(diseased_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(blended, contours, -1, (0, 0, 255), 1)

    blended_rgb = cv2.cvtColor(blended, cv2.COLOR_BGR2RGB)
    overlay_pil = Image.fromarray(blended_rgb)

    return {
        "severity_score": severity_pct,
        "stage": stage,
        "color": color,
        "overlay_image": overlay_pil
    }
