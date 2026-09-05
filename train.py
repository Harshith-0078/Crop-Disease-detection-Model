import os
import argparse
import time
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
from model import build_model

def get_transforms(img_size: int = 224):
    train_transform = transforms.Compose([
        transforms.RandomResizedCrop(img_size, scale=(0.8, 1.0)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.2),
        transforms.RandomRotation(degrees=20),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.05),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    val_transform = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return train_transform, val_transform

def plot_history(history: dict, save_path: str = "training_history.png"):
    epochs = range(1, len(history["train_loss"]) + 1)
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(epochs, history["train_loss"], 'o-', label="Train Loss", color="royalblue")
    plt.plot(epochs, history["val_loss"], 's--', label="Val Loss", color="crimson")
    plt.title("Loss vs. Epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Cross-Entropy Loss")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.subplot(1, 2, 2)
    plt.plot(epochs, history["train_acc"], 'o-', label="Train Acc", color="royalblue")
    plt.plot(epochs, history["val_acc"], 's--', label="Val Acc", color="green")
    plt.title("Accuracy vs. Epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy (%)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    print(f"[OK] Saved training metrics plot to {save_path}")

def train_model(data_dir: str, epochs: int, batch_size: int, lr: float, output_path: str):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[*] Training on device: {device}")

    train_dir = os.path.join(data_dir, "train")
    val_dir = os.path.join(data_dir, "val")

    if not os.path.exists(train_dir) or not os.path.exists(val_dir):
        print(f"[!] Error: Expected dataset folder structure at '{data_dir}':")
        print(f"    {data_dir}/train/<class_name>/<images...>")
        print(f"    {data_dir}/val/<class_name>/<images...>")
        return

    train_tf, val_tf = get_transforms()

    print("[*] Loading datasets...")
    train_dataset = datasets.ImageFolder(train_dir, transform=train_tf)
    val_dataset = datasets.ImageFolder(val_dir, transform=val_tf)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=2, pin_memory=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=True)

    classes = train_dataset.classes
    num_classes = len(classes)
    print(f"[OK] Found {len(train_dataset)} training images and {len(val_dataset)} validation images across {num_classes} classes.")

    model = build_model(num_classes=num_classes, pretrained=True).to(device)
    criterion = nn.CrossEntropyLoss(label_smoothing=0.1)
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)

    best_val_acc = 0.0
    history = {"train_loss": [], "train_acc": [], "val_loss": [], "val_acc": []}

    print("\n--- Starting Training Loop ---")
    start_time = time.time()

    for epoch in range(1, epochs + 1):
        # Training Phase
        model.train()
        running_loss = 0.0
        running_corrects = 0

        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()

            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            _, preds = torch.max(outputs, 1)
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data).item()

        epoch_train_loss = running_loss / len(train_dataset)
        epoch_train_acc = (running_corrects / len(train_dataset)) * 100

        # Validation Phase
        model.eval()
        val_loss = 0.0
        val_corrects = 0

        with torch.no_grad():
            for inputs, labels in val_loader:
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = model(inputs)
                loss = criterion(outputs, labels)

                _, preds = torch.max(outputs, 1)
                val_loss += loss.item() * inputs.size(0)
                val_corrects += torch.sum(preds == labels.data).item()

        epoch_val_loss = val_loss / len(val_dataset)
        epoch_val_acc = (val_corrects / len(val_dataset)) * 100

        scheduler.step()

        history["train_loss"].append(epoch_train_loss)
        history["train_acc"].append(epoch_train_acc)
        history["val_loss"].append(epoch_val_loss)
        history["val_acc"].append(epoch_val_acc)

        print(f"Epoch [{epoch:02d}/{epochs:02d}] "
              f"Train Loss: {epoch_train_loss:.4f} | Train Acc: {epoch_train_acc:.2f}% "
              f"|| Val Loss: {epoch_val_loss:.4f} | Val Acc: {epoch_val_acc:.2f}% "
              f"|| LR: {scheduler.get_last_lr()[0]:.6f}")

        if epoch_val_acc > best_val_acc:
            best_val_acc = epoch_val_acc
            torch.save({
                "epoch": epoch,
                "model_state_dict": model.state_dict(),
                "classes": classes,
                "val_acc": epoch_val_acc
            }, output_path)
            print(f"  [*] Best model saved with Val Acc: {best_val_acc:.2f}% to '{output_path}'")

    total_time = time.time() - start_time
    print(f"\n[OK] Training complete in {total_time/60:.2f} mins. Peak Val Accuracy: {best_val_acc:.2f}%")
    plot_history(history)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train MobileNetV3 Plant Disease Classifier")
    parser.add_argument("--data_dir", type=str, default="./dataset", help="Path to dataset containing 'train' and 'val'")
    parser.add_argument("--epochs", type=int, default=15, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for training")
    parser.add_argument("--lr", type=float, default=0.0005, help="Initial learning rate")
    parser.add_argument("--output", type=str, default="plant_disease_model.pth", help="Path to save best checkpoint")
    args = parser.parse_args()

    train_model(args.data_dir, args.epochs, args.batch_size, args.lr, args.output)
