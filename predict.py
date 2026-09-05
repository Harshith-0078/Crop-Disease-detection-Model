import sys
import os
import argparse

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from model import PlantDiseaseClassifier
from severity import calculate_disease_severity

def run_prediction(image_path: str, model_path: str = "plant_disease_model.pth", topk: int = 3):
    if not os.path.exists(image_path):
        print(f"[!] Error: Image file '{image_path}' not found.")
        sys.exit(1)

    print(f"\nLoading model and analyzing image: {image_path} ...")
    classifier = PlantDiseaseClassifier(model_path=model_path)
    predictions = classifier.predict(image_path, topk=topk)

    top_pred = predictions[0]
    is_healthy = "healthy" in top_pred["raw_class"].lower()
    severity = calculate_disease_severity(image_path, is_healthy=is_healthy)

    print("\n" + "=" * 60)
    print("PLANT HEALTH DIAGNOSIS REPORT")
    print("=" * 60)

    print(f"\nPrimary Diagnosis : {top_pred['label']}")
    print(f"Confidence Score  : {top_pred['confidence']:.2f}%")
    print(f"Disease Severity  : {severity['severity_score']:.2f}% ({severity['stage']})\n")

    details = top_pred["details"]
    print(f"Target Crop       : {details.get('crop', 'N/A')}")
    print(f"Pathogen / Cause  : {details.get('pathogen', 'N/A')}")
    print(f"\nKey Symptoms:\n   {details.get('symptoms', 'N/A')}")
    print(f"\nPreventative Measures:\n   {details.get('prevention', 'N/A')}")
    print(f"\nRecommended Treatment:\n   {details.get('treatment', 'N/A')}")

    if len(predictions) > 1:
        print("\n" + "-" * 60)
        print("Alternative Possibilities:")
        for idx, alt in enumerate(predictions[1:], start=2):
            print(f"   {idx}. {alt['label']} ({alt['confidence']:.2f}%)")

    print("=" * 60 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plant Disease Classifier CLI")
    parser.add_argument("--image", type=str, default="gettyimages-1152373430-612x612.jpg", help="Path to input leaf image")
    parser.add_argument("--model", type=str, default="plant_disease_model.pth", help="Path to trained model checkpoint")
    parser.add_argument("--topk", type=int, default=3, help="Number of top predictions to display")
    args = parser.parse_args()

    run_prediction(args.image, args.model, args.topk)
