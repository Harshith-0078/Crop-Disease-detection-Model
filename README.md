# FloraGuard - AI Plant Disease Detection & Diagnosis

FloraGuard is an end-to-end Machine Learning system for automated plant leaf disease detection and actionable treatment recommendation using Deep Learning (PyTorch & MobileNetV3).

---

## Project Structure

- [`app.py`](file:///c:/Users/kappa/OneDrive/Desktop/Python/PLANT/app.py) : Interactive Web Application (Streamlit) for photo diagnosis & disease encyclopedia.
- [`predict.py`](file:///c:/Users/kappa/OneDrive/Desktop/Python/PLANT/predict.py) : Fast CLI tool to predict disease and view treatment remedies for any leaf image.
- [`model.py`](file:///c:/Users/kappa/OneDrive/Desktop/Python/PLANT/model.py) : PyTorch MobileNetV3 model architecture, preprocessing, and inference pipeline.
- [`disease_database.py`](file:///c:/Users/kappa/OneDrive/Desktop/Python/PLANT/disease_database.py) : Comprehensive knowledge base of 38 plant diseases, symptoms, causes, organic and chemical treatments.
- [`train.py`](file:///c:/Users/kappa/OneDrive/Desktop/Python/PLANT/train.py) : Full training script with data augmentation, Cosine Annealing LR scheduling, and metric plots.
- [`requirements.txt`](file:///c:/Users/kappa/OneDrive/Desktop/Python/PLANT/requirements.txt) : Python dependencies.

---

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run CLI Diagnosis on an Image
```bash
python predict.py --image gettyimages-1152373430-612x612.jpg
```

### 3. Launch the Web Interface
```bash
streamlit run app.py
```

---

## Training with a Custom Dataset (e.g. PlantVillage)

1. Download the [PlantVillage dataset from Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease).
2. Arrange the folders as follows:
   ```text
   dataset/
     ├── train/
     │     ├── Tomato___Early_blight/
     │     └── ...
     └── val/
           ├── Tomato___Early_blight/
           └── ...
   ```
3. Run training:
   ```bash
   python train.py --data_dir ./dataset --epochs 15 --batch_size 32
   ```
4. The best model will automatically be saved as `plant_disease_model.pth`.
