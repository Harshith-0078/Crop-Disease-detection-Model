import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from disease_database import DISEASE_CLASSES, format_class_name, get_disease_details

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
NUM_CLASSES = len(DISEASE_CLASSES)

# Preprocessing transforms (ImageNet normalization)
TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def build_model(num_classes: int = NUM_CLASSES, pretrained: bool = True) -> nn.Module:
    """
    Constructs a MobileNetV3-Large neural network for plant disease classification.
    MobileNetV3 is optimized for high accuracy, low latency, and mobile/edge deployment.
    """
    weights = models.MobileNet_V3_Large_Weights.DEFAULT if pretrained else None
    model = models.mobilenet_v3_large(weights=weights)
    in_features = model.classifier[3].in_features
    
    # Custom classification head
    model.classifier[3] = nn.Sequential(
        nn.Dropout(p=0.3),
        nn.Linear(in_features, num_classes)
    )
    return model

class PlantDiseaseClassifier:
    def __init__(self, model_path: str = "plant_disease_model.pth"):
        self.model_path = model_path
        self.device = DEVICE
        self.classes = DISEASE_CLASSES
        self.model = self._load_model()

    def _load_model(self) -> nn.Module:
        model = build_model(num_classes=len(self.classes), pretrained=False)
        
        if os.path.exists(self.model_path):
            try:
                checkpoint = torch.load(self.model_path, map_location=self.device)
                if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
                    model.load_state_dict(checkpoint["model_state_dict"])
                    if "classes" in checkpoint:
                        self.classes = checkpoint["classes"]
                elif isinstance(checkpoint, dict):
                    model.load_state_dict(checkpoint)
                print(f"[OK] Successfully loaded custom trained model from {self.model_path}")
            except Exception as e:
                print(f"[!] Warning: Could not load checkpoint ({e}). Using initialized backbone.")
        else:
            print(f"[*] No checkpoint found at '{self.model_path}'. Running in evaluation / demo mode.")
            
        model = model.to(self.device)
        model.eval()
        return model

    def predict(self, image_input, topk: int = 3) -> list[dict]:
        """
        Classifies an input image (file path or PIL.Image) and returns top-K predictions with confidence.
        """
        if isinstance(image_input, str):
            image = Image.open(image_input).convert("RGB")
        elif isinstance(image_input, Image.Image):
            image = image_input.convert("RGB")
        else:
            raise ValueError("Input must be a valid file path or PIL Image object.")

        tensor = TRANSFORM(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(tensor)
            probabilities = torch.softmax(outputs, dim=1)[0]
            top_probs, top_indices = torch.topk(probabilities, k=min(topk, len(self.classes)))

        results = []
        for prob, idx in zip(top_probs, top_indices):
            raw_class = self.classes[idx.item()]
            readable_label = format_class_name(raw_class)
            info = get_disease_details(raw_class)
            confidence_pct = float(prob.item() * 100)
            
            results.append({
                "raw_class": raw_class,
                "label": readable_label,
                "confidence": confidence_pct,
                "details": info
            })
        return results
