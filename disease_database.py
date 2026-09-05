"""
Plant Disease Knowledge Database
Contains 38 standard plant & disease classes from the PlantVillage taxonomy,
including symptoms, causes, organic remedies, and chemical treatments.
"""

DISEASE_CLASSES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease": "Apple Scab",
        "pathogen": "Fungus (Venturia inaequalis)",
        "symptoms": "Olive-green to velvety brown spots on leaves and scabby lesions on fruit.",
        "cause": "High humidity and continuous leaf wetness during warm spring temperatures (15-24°C).",
        "prevention": "Prune trees to improve air circulation, clear fallen infected leaves in autumn, and choose scab-resistant apple cultivars.",
        "treatment": "Apply sulfur or copper-based organic fungicides early in the season, or systemic fungicides like Myclobutanil / Captan."
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "disease": "Black Rot",
        "pathogen": "Fungus (Botryosphaeria obtusa)",
        "symptoms": "Circular brown leaf spots ('frog-eye' pattern) and dark sunken cankers on limbs/fruit.",
        "cause": "Overwintering fungal spores in dead wood and mummified fruit.",
        "prevention": "Prune out dead or infected branches and remove mummified fruit from the orchard.",
        "treatment": "Apply copper fungicides at bud break and captan or strobilurin-based fungicides during growing season."
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "disease": "Cedar Apple Rust",
        "pathogen": "Fungus (Gymnosporangium juniperi-virginianae)",
        "symptoms": "Bright yellow-orange spots on leaves with small black fruiting bodies in the center.",
        "cause": "Proximity to Eastern Red Cedar / Juniper trees which act as alternate hosts.",
        "prevention": "Remove nearby juniper trees if possible; plant rust-immune apple varieties.",
        "treatment": "Apply preventative fungicides like Immunox, Myclobutanil, or sulfur when leaf buds break."
    },
    "Apple___healthy": {
        "crop": "Apple",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Leaves are vibrant green with no visible spots, discolorations, or lesions.",
        "cause": "Optimal plant nutrition, sun exposure, and pest management.",
        "prevention": "Maintain regular watering, balanced N-P-K fertilization, and seasonal pruning.",
        "treatment": "No treatment required. Continue standard plant care."
    },
    "Blueberry___healthy": {
        "crop": "Blueberry",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Vibrant foliage with rich green color and robust vigor.",
        "cause": "Acidic soil (pH 4.5-5.5) and good drainage.",
        "prevention": "Maintain soil acidity with pine bark mulch or elemental sulfur.",
        "treatment": "No treatment required."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "disease": "Powdery Mildew",
        "pathogen": "Fungus (Podosphaera clandestina)",
        "symptoms": "White powdery fungal patches on new foliage, curling leaves, stunted shoots.",
        "cause": "Warm days with high relative humidity and dry leaf surfaces.",
        "prevention": "Prune dense canopies for airflow and avoid excess nitrogen fertilization.",
        "treatment": "Spray neem oil, potassium bicarbonate, or sulfur sprays at first sign of infection."
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Leaves are lush green, glossy, with no powdery coating or leaf spots.",
        "cause": "Good care and optimal environment.",
        "prevention": "Maintain adequate moisture and regular pruning.",
        "treatment": "No treatment required."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "disease": "Gray Leaf Spot",
        "pathogen": "Fungus (Cercospora zeae-maydis)",
        "symptoms": "Rectangular, brown to gray lesions bound by leaf veins.",
        "cause": "Warm temperatures (25-32°C) combined with prolonged high humidity and morning dew.",
        "prevention": "Rotate crops with non-host plants (e.g., soybeans), till crop residue, plant tolerant hybrids.",
        "treatment": "Apply foliar fungicides (QoI/strobilurins or DMI/triazoles) before tasseling."
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "disease": "Common Rust",
        "pathogen": "Fungus (Puccinia sorghi)",
        "symptoms": "Small, powdery cinnamon-brown pustules scattered across both leaf surfaces.",
        "cause": "Cool to moderate temperatures (16-25°C) and high humidity carried by wind currents.",
        "prevention": "Plant resistant corn hybrids; ensure proper field drainage.",
        "treatment": "Foliar fungicides such as Pyraclostrobin or Azoxystrobin when pustules appear on upper leaves."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "disease": "Northern Corn Leaf Blight",
        "pathogen": "Fungus (Exserohilum turcicum)",
        "symptoms": "Long, elliptical cigar-shaped grayish-green to tan lesions on leaves.",
        "cause": "Cool, wet weather with extended periods of dew.",
        "prevention": "Crop rotation, burying infected crop residue, and selecting resistant hybrids.",
        "treatment": "Apply fungicides containing propiconazole or pyraclostrobin if disease reaches upper canopy early."
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Broad, green, uniform leaves free of lesions or pustules.",
        "cause": "Balanced soil nutrition and moisture.",
        "prevention": "Consistent watering and soil testing.",
        "treatment": "No treatment required."
    },
    "Grape___Black_rot": {
        "crop": "Grape",
        "disease": "Black Rot",
        "pathogen": "Fungus (Guignardia bidwellii)",
        "symptoms": "Small reddish-brown leaf spots with dark borders; fruit shrivels into black mummies.",
        "cause": "Warm rainy weather during spring shoot growth and flowering.",
        "prevention": "Remove mummified berries, prune canopies, and orient rows toward prevailing wind.",
        "treatment": "Apply mancozeb, captan, or myclobutanil fungicides starting at bud break."
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "disease": "Esca (Black Measles)",
        "pathogen": "Fungal complex (Phaeomoniella, Phaeoacremonium, Fomitiporia)",
        "symptoms": "'Tiger-stripe' leaf discoloration (interveinal yellowing and necrosis) and spotted berries.",
        "cause": "Fungal infection entering through winter pruning wounds in old wood.",
        "prevention": "Protect pruning wounds with sealing paste; avoid pruning during wet weather.",
        "treatment": "No direct cure; practice trunk renewal, remedial surgery, or replace severely affected vines."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "disease": "Leaf Blight",
        "pathogen": "Fungus (Pseudocercospora vitis)",
        "symptoms": "Dark brown circular spots on leaves that turn necrotic, causing premature defoliation.",
        "cause": "High humidity and wet canopies late in the season.",
        "prevention": "Ensure good canopy ventilation, remove fallen diseased leaves.",
        "treatment": "Copper-based fungicides or broad-spectrum protectants."
    },
    "Grape___healthy": {
        "crop": "Grape",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Healthy green foliage and robust vine vigor.",
        "cause": "Proper trellis training and disease management.",
        "prevention": "Regular pruning and balanced watering.",
        "treatment": "No treatment required."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange / Citrus",
        "disease": "Citrus Greening (Huanglongbing)",
        "pathogen": "Bacterium (Candidatus Liberibacter asiaticus)",
        "symptoms": "Asymmetrical yellow mottling on leaves, small lopsided bitter fruit that stays green at base.",
        "cause": "Vectored by the Asian Citrus Psyllid (Diaphorina citri).",
        "prevention": "Use certified disease-free nursery trees; eradicate psyllid vectors through biological/chemical controls.",
        "treatment": "No known chemical cure; remove infected trees to prevent orchard-wide transmission."
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "disease": "Bacterial Spot",
        "pathogen": "Bacterium (Xanthomonas arboricola pv. pruni)",
        "symptoms": "Water-soaked polygonal leaf spots that drop out creating 'shot-hole' appearance.",
        "cause": "Wind-driven rain, warm temperatures, and sandy soils.",
        "prevention": "Plant resistant cultivars; plant windbreaks to minimize wind/sand abrasions.",
        "treatment": "Copper sprays at dormancy and oxytetracycline sprays during early leaf stages."
    },
    "Peach___healthy": {
        "crop": "Peach",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Long vibrant green leaves with no lesions or shot-hole perforations.",
        "cause": "Good nutrition and orchard care.",
        "prevention": "Pruning for sunshine and routine pest monitoring.",
        "treatment": "No treatment required."
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper",
        "disease": "Bacterial Spot",
        "pathogen": "Bacterium (Xanthomonas campestris pv. vesicatoria)",
        "symptoms": "Small, water-soaked brown spots on leaves with yellow halos, leading to leaf drop.",
        "cause": "Splashing water, warm humid conditions (24-30°C), and contaminated seeds.",
        "prevention": "Use certified disease-free seed, drip irrigation instead of overhead watering, and crop rotation.",
        "treatment": "Apply copper bactericides combined with mancozeb to slow spread."
    },
    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Uniform deep green foliage and vigorous flower/fruit production.",
        "cause": "Full sun, balanced organic nutrients, well-draining soil.",
        "prevention": "Mulching and steady watering.",
        "treatment": "No treatment required."
    },
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "pathogen": "Fungus (Alternaria solani)",
        "symptoms": "Concentric rings ('target-board' pattern) within dark brown leaf spots.",
        "cause": "Alternating wet and dry weather conditions; plant stress from high yield or poor nutrition.",
        "prevention": "Maintain plant vigor with balanced nitrogen, avoid overhead irrigation, 3-year crop rotation.",
        "treatment": "Apply copper fungicides, chlorothalonil, or mancozeb at first sign of symptoms."
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "pathogen": "Oomycete (Phytophthora infestans)",
        "symptoms": "Water-soaked dark lesions on leaf tips and margins with white mold on leaf undersides in humid air.",
        "cause": "Cool (15-20°C), continuously damp weather.",
        "prevention": "Plant certified seed tubers; destroy cull piles; avoid sprinkler irrigation at night.",
        "treatment": "Apply protectant fungicides (e.g., Mancozeb) or systemic fungicides (e.g., Metalaxyl/Mefenoxam, Dimethomorph)."
    },
    "Potato___healthy": {
        "crop": "Potato",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Lush green canopy without concentric leaf spots or water-soaked lesions.",
        "cause": "Healthy seed and well-draining soil.",
        "prevention": "Proper hilling, adequate spacing, and balanced fertilizer.",
        "treatment": "No treatment required."
    },
    "Raspberry___healthy": {
        "crop": "Raspberry",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Vibrant serrated green leaves and clean canes.",
        "cause": "Proper airflow and sun exposure.",
        "prevention": "Pruning spent floricanes after harvest.",
        "treatment": "No treatment required."
    },
    "Soybean___healthy": {
        "crop": "Soybean",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Dense trifoliate green leaves with no rust pustules or yellow mottling.",
        "cause": "Adequate soil Rhizobium inoculation and pest control.",
        "prevention": "Crop rotation and soil aeration.",
        "treatment": "No treatment required."
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "disease": "Powdery Mildew",
        "pathogen": "Fungus (Podosphaera xanthii)",
        "symptoms": "White talcum powder-like spots covering both upper and lower leaf surfaces.",
        "cause": "High humidity combined with shaded, crowded conditions.",
        "prevention": "Plant in full sun, space vines widely, choose PM-resistant varieties.",
        "treatment": "Spray neem oil, potassium bicarbonate, diluted milk spray (10-20%), or sulfur."
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "disease": "Leaf Scorch",
        "pathogen": "Fungus (Diplocarpon earlianum)",
        "symptoms": "Small purple spots that enlarge into irregular dark purple-brown blotches with scorched leaf edges.",
        "cause": "Frequent rainfall or overhead sprinkler irrigation keeping foliage wet.",
        "prevention": "Use drip irrigation, remove older infected leaves after harvest, ensure good bed drainage.",
        "treatment": "Apply copper-based fungicides or captan during active spring growth."
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Glossy green leaves and healthy crowns.",
        "cause": "Good straw mulching and drip irrigation.",
        "prevention": "Clean straw mulch to prevent soil-borne fungal splash.",
        "treatment": "No treatment required."
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "pathogen": "Bacterium (Xanthomonas spp.)",
        "symptoms": "Small, greasy/water-soaked dark spots on leaves that turn brown with yellow halos.",
        "cause": "Warm temperatures (24-30°C) with rain splashes or overhead watering.",
        "prevention": "Use drip irrigation, avoid touching wet plants, sanitize gardening stakes and tools.",
        "treatment": "Apply copper spray combined with Mancozeb."
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "pathogen": "Fungus (Alternaria solani)",
        "symptoms": "Brown to black spots with concentric rings ('bullseye' target pattern) starting on lowest leaves.",
        "cause": "High humidity, rain splashes from infected soil onto bottom leaves.",
        "prevention": "Mulch around base of plants, prune bottom 12 inches of foliage, rotate crops annually.",
        "treatment": "Apply copper fungicide, Bacillus subtilis, or Chlorothalonil."
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "pathogen": "Oomycete (Phytophthora infestans)",
        "symptoms": "Large, dark water-soaked spots on leaves and stems with white fuzzy spore growth on leaf undersides.",
        "cause": "Cool, damp weather (15-22°C with fog/rain). Highly destructive and fast-spreading.",
        "prevention": "Plant in full sun with maximum ventilation, destroy infected debris immediately, plant resistant varieties (e.g., Defiant, Mountain Magic).",
        "treatment": "Copper fungicides as protectant; remove and bag severely infected plants to prevent airborne spread."
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "pathogen": "Fungus (Passalora fulva)",
        "symptoms": "Pale greenish-yellow spots on upper leaf surface, with olive-brown velvety mold directly underneath.",
        "cause": "High relative humidity (>85%) and poor air movement, common in greenhouses and tunnels.",
        "prevention": "Improve greenhouse ventilation, reduce humidity, water at soil level.",
        "treatment": "Copper fungicides, biofungicides (Bacillus amyloliquefaciens), or difenoconazole."
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "pathogen": "Fungus (Septoria lycopersici)",
        "symptoms": "Numerous small circular spots with grayish-white centers and dark brown borders.",
        "cause": "Extended wet foliage and warm weather (20-25°C). Overwinters in garden debris.",
        "prevention": "Mulch soil surface, water via drip system, prune diseased lower leaves.",
        "treatment": "Copper sprays or broad-spectrum fungicides like Chlorothalonil."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "disease": "Two-Spotted Spider Mites",
        "pathogen": "Pest (Tetranychus urticae)",
        "symptoms": "Fine yellow stippling/speckling on leaves, fine webbing on undersides, yellowing leaves.",
        "cause": "Hot, dry, and dusty conditions.",
        "prevention": "Maintain soil moisture, rinse dust off foliage, introduce predatory mites (Phytoseiulus persimilis).",
        "treatment": "Apply insecticidal soap, neem oil, or horticultural oils to leaf undersides."
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "pathogen": "Fungus (Corynespora cassiicola)",
        "symptoms": "Brown lesions with light brown centers and dark concentric rings on leaves and fruit.",
        "cause": "Warm temperatures (20-28°C) and high humidity.",
        "prevention": "Wider plant spacing, remove weeds, stake and tie plants for optimal airflow.",
        "treatment": "Apply copper-based fungicides or azoxystrobin."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "pathogen": "Virus (Begomovirus)",
        "symptoms": "Upward curling and cupping of leaves, yellow margins, severe stunting of plant growth.",
        "cause": "Transmitted by silverleaf whiteflies (Bemisia tabaci).",
        "prevention": "Install fine insect netting, use yellow sticky traps, plant TYLCV-resistant hybrids.",
        "treatment": "No cure once infected; manage whitefly populations with neem oil/imidacloprid and rogue out infected plants."
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "pathogen": "Virus (Tobamovirus)",
        "symptoms": "Mottled light and dark green mosaic patterns on leaves, 'shoestring' leaf distortion, stunted growth.",
        "cause": "Mechanical transmission via tools, hands, tobacco smoke, and infected seed.",
        "prevention": "Wash hands with soap before handling plants, sterilize pruners in 10% bleach, avoid tobacco use near plants.",
        "treatment": "No chemical cure. Remove and burn/dispose of infected plants; do not compost."
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "disease": "Healthy Plant",
        "pathogen": "None",
        "symptoms": "Deep green vibrant foliage, sturdy stems, and unblemished fruit.",
        "cause": "Good garden management, balanced nutrition, and appropriate sunlight.",
        "prevention": "Mulching, staking, and drip irrigation.",
        "treatment": "No treatment required. Maintain standard plant care."
    }
}

def format_class_name(class_name: str) -> str:
    """Format standard class identifier into human-readable label."""
    if class_name in DISEASE_INFO:
        info = DISEASE_INFO[class_name]
        return f"{info['crop']} - {info['disease']}"
    return class_name.replace("___", " - ").replace("_", " ")

def get_disease_details(class_name: str) -> dict:
    """Retrieve detailed info, symptoms, and remedies for a disease class."""
    if class_name in DISEASE_INFO:
        return DISEASE_INFO[class_name]
    return {
        "crop": class_name.split("___")[0].replace("_", " "),
        "disease": class_name.split("___")[-1].replace("_", " ") if "___" in class_name else "Unknown",
        "pathogen": "N/A",
        "symptoms": "Symptoms details not available.",
        "cause": "Unknown",
        "prevention": "Ensure good ventilation, proper watering, and clean soil.",
        "treatment": "Consult a local agricultural extension specialist."
    }
