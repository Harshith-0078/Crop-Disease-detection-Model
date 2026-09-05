import os
import streamlit as st
from PIL import Image
from model import PlantDiseaseClassifier
from disease_database import DISEASE_INFO, format_class_name

# Page configuration
st.set_page_config(
    page_title="FloraGuard - AI Plant Disease Diagnostic",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for a polished look
st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #2E7D32 0%, #00B4D8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .result-card {
        background-color: #f8fafc;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .badge-healthy {
        background-color: #dcfce7;
        color: #166534;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    .badge-diseased {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_classifier():
    return PlantDiseaseClassifier(model_path="plant_disease_model.pth")

classifier = load_classifier()

# Sidebar
st.sidebar.image("https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?w=500&auto=format&fit=crop&q=60", use_container_width=True)
st.sidebar.title("FloraGuard AI")
st.sidebar.markdown("**AI-Powered Agricultural Crop Disease Detection & Care Guide**")

app_mode = st.sidebar.radio(
    "Navigation",
    ["Disease Diagnostic", "Disease Encyclopedia", "Model Training Guide"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Supported Crops")
crops_list = ["Apple", "Blueberry", "Cherry", "Corn (Maize)", "Grape", "Orange", "Peach", "Pepper (Bell)", "Potato", "Raspberry", "Soybean", "Squash", "Strawberry", "Tomato"]
st.sidebar.write(", ".join(crops_list))

if app_mode == "Disease Diagnostic":
    st.markdown('<div class="main-header">AI Plant Disease Diagnostic</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Upload a plant leaf photo or select a sample image to diagnose crop diseases and get curated organic & chemical treatment plans.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("1. Provide Leaf Image")
        input_source = st.radio("Choose Input Method", ["Upload Image", "Camera Capture", "Try Sample Image"], horizontal=True)

        image_to_process = None

        if input_source == "Upload Image":
            uploaded_file = st.file_uploader("Upload leaf picture (JPG, PNG, JPEG)", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                image_to_process = Image.open(uploaded_file)
                st.image(image_to_process, caption="Uploaded Leaf Image", use_container_width=True)

        elif input_source == "Camera Capture":
            camera_file = st.camera_input("Take a picture of the plant leaf")
            if camera_file is not None:
                image_to_process = Image.open(camera_file)
                st.image(image_to_process, caption="Captured Image", use_container_width=True)

        elif input_source == "Try Sample Image":
            sample_path = "gettyimages-1152373430-612x612.jpg"
            if os.path.exists(sample_path):
                image_to_process = Image.open(sample_path)
                st.image(image_to_process, caption="Sample Leaf from Workspace", use_container_width=True)
            else:
                st.info("No sample image found in workspace folder.")

        analyze_button = st.button("Analyze Leaf Health", type="primary", use_container_width=True, disabled=image_to_process is None)

    with col2:
        st.subheader("2. Diagnostic Report")
        if analyze_button and image_to_process is not None:
            with st.spinner("Analyzing leaf patterns using Deep Convolutional Neural Network..."):
                results = classifier.predict(image_to_process, topk=3)
                top = results[0]
                details = top["details"]
                is_healthy = "healthy" in top["raw_class"].lower()

                # Status Badge
                badge_html = (
                    f'<span class="badge-healthy">Healthy Plant</span>'
                    if is_healthy
                    else f'<span class="badge-diseased">Disease Detected</span>'
                )
                st.markdown(f"### {top['label']} {badge_html}", unsafe_allow_html=True)
                st.progress(min(top["confidence"] / 100.0, 1.0), text=f"Confidence: {top['confidence']:.2f}%")

                st.markdown("---")
                
                # Tabbed Details
                t1, t2, t3 = st.tabs(["Overview & Symptoms", "Prevention", "Treatments"])
                
                with t1:
                    st.markdown(f"**Crop:** `{details.get('crop', 'Unknown')}`")
                    st.markdown(f"**Pathogen:** `{details.get('pathogen', 'N/A')}`")
                    st.markdown(f"**Symptoms:**\n{details.get('symptoms', 'None')}")
                    st.markdown(f"**Primary Cause:**\n{details.get('cause', 'N/A')}")

                with t2:
                    st.info(f"**Recommended Preventative Measures:**\n\n{details.get('prevention', 'N/A')}")

                with t3:
                    st.success(f"**Remedies & Treatment Strategies:**\n\n{details.get('treatment', 'N/A')}")

                # Alternative Possibilities
                if len(results) > 1:
                    with st.expander("View Top Alternative Probabilities"):
                        for alt in results[1:]:
                            col_a, col_b = st.columns([2, 1])
                            col_a.write(f"**{alt['label']}**")
                            col_b.write(f"{alt['confidence']:.2f}%")
                            st.progress(min(alt["confidence"] / 100.0, 1.0))
        elif image_to_process is None:
            st.info("Please upload or select a leaf image on the left to begin diagnosis.")

elif app_mode == "Disease Encyclopedia":
    st.markdown('<div class="main-header">Plant Disease Encyclopedia</div>', unsafe_allow_html=True)
    st.write("Browse symptoms, causes, and treatment protocols for all 38 supported crop conditions.")

    search_query = st.text_input("Search by Crop or Disease Name (e.g., Tomato, Rust, Blight)...", "")
    
    filtered_diseases = {
        k: v for k, v in DISEASE_INFO.items() 
        if search_query.lower() in v["crop"].lower() or search_query.lower() in v["disease"].lower()
    }

    st.write(f"Showing {len(filtered_diseases)} matching conditions:")

    for raw_id, info in filtered_diseases.items():
        with st.expander(f"{info['crop']} — {info['disease']}"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"**Pathogen:** `{info['pathogen']}`")
                st.markdown(f"**Symptoms:** {info['symptoms']}")
                st.markdown(f"**Causes:** {info['cause']}")
            with c2:
                st.markdown(f"**Prevention:** {info['prevention']}")
                st.markdown(f"**Treatment:** {info['treatment']}")

elif app_mode == "Model Training Guide":
    st.markdown('<div class="main-header">How to Train with Custom Datasets</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 1. Download Dataset (e.g., PlantVillage)
    You can download the popular **PlantVillage Dataset** from Kaggle or HuggingFace with 54,000+ labeled images:
    - [PlantVillage on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)

    ### 2. Organize Folder Structure
    Ensure your dataset is organized inside the `dataset/` folder as follows:
    ```text
    dataset/
      ├── train/
      │     ├── Apple___Apple_scab/
      │     ├── Tomato___Early_blight/
      │     └── ... (other classes)
      └── val/
            ├── Apple___Apple_scab/
            ├── Tomato___Early_blight/
            └── ... (other classes)
    ```

    ### 3. Run Training Command
    Execute the high-performance MobileNetV3 transfer learning script:
    ```bash
    python train.py --data_dir ./dataset --epochs 15 --batch_size 32 --lr 0.0005
    ```
    This will save the best model weights to `plant_disease_model.pth` and create `training_history.png`.
    """)
