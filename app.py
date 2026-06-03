from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ─── Medical Knowledge Base ───────────────────────────────────────────────────

MEDICAL_DATA = {

    # Symptoms
    "fever": (
        "**Detailed Overview:** A fever (pyrexia) is a clinical sign of an underlying process, "
        "most commonly an infection. It is the body's natural immunological response to pathogens.\n\n"
        "**Management Protocol:**\n"
        "1. **Hydration:** Consume at least 2-3 liters of fluids daily to prevent dehydration.\n"
        "2. **Environment:** Maintain a cool room temperature and wear light clothing.\n\n"
        "**Clinical Red Flags:** Seek immediate medical evaluation if temperature persists above "
        "103°F, or if you experience confusion or a stiff neck."
    ),
    "cough": (
        "**Detailed Overview:** A cough is a protective reflex. It can be categorized as "
        "'acute' (under 3 weeks) or 'chronic' (over 8 weeks).\n\n"
        "**Therapeutic Steps:**\n"
        "- **Humidification:** Use a cool-mist humidifier to soothe irritated lung tissue.\n"
        "- **Fluid Intake:** Warm liquids help break up mucus in the respiratory tract.\n\n"
        "**Clinical Warning Signs:** Contact a healthcare provider immediately if you experience "
        "coughing up blood or persistent wheezing."
    ),
    "cold": (
        "**Detailed Overview:** The common cold is a viral upper respiratory tract infection. "
        "Over 200 viruses can cause a cold, with rhinoviruses being the most common.\n\n"
        "**Comprehensive Care Plan:**\n"
        "- **Rest:** Allow the immune system to prioritize fighting the virus.\n"
        "- **Symptom Management:** Use saline nasal drops for congestion.\n\n"
        "**When to see a doctor:** If symptoms do not improve after 10 days."
    ),
    "headache": (
        "**Detailed Overview:** Headaches range from tension-type to migraines. "
        "Primary headaches are not caused by underlying diseases.\n\n"
        "**Structured Management:**\n"
        "- **Environmental Control:** Dim lights and reduce noise levels during an attack.\n"
        "- **Hydration:** Dehydration is a leading cause of tension headaches.\n\n"
        "**Critical Alert:** Seek emergency care for 'worst headache of life' or vision changes."
    ),
    "nausea": (
        "**Detailed Overview:** Nausea is the subjective feeling of a need to vomit. "
        "It is a symptom of many conditions.\n\n"
        "**Recovery Steps:**\n"
        "- **Dietary Control:** Stick to the BRAT diet (Bananas, Rice, Applesauce, Toast).\n"
        "- **Ginger/Peppermint:** Natural remedies clinically shown to settle stomach lining."
    ),
    "vomiting":         "Vomiting causes rapid dehydration. Sip electrolyte solutions frequently. Seek emergency care if you cannot keep fluids down for 24 hours.",
    "fatigue":          "Persistent fatigue can result from stress, anemia, or thyroid issues. Focus on sleep hygiene. If it persists for weeks, consult a doctor for bloodwork.",
    "dizziness":        "Dizziness requires sitting or lying down immediately. Hydrate well. Seek emergency care if accompanied by sudden numbness or speech changes.",
    "weakness":         "Generalized weakness may indicate viral illness or low blood sugar. If localized to one side of the body, seek emergency care immediately as it may be a stroke.",
    "chills":           "Chills often accompany fever. Dress in light layers and monitor your temperature.",
    "sore throat":      "Gargle with warm salt water and rest your voice. See a doctor if you have difficulty swallowing or a persistent high fever.",
    "diarrhea":         "Focus on rehydration with water or broths. Eat bland foods. See a physician if it lasts more than 2 days or shows blood.",
    "constipation":     "Increase dietary fiber and water intake. If chronic or accompanied by severe pain, consult a professional.",
    "stomach pain":     "Can stem from indigestion or viruses. Seek urgent care for severe, sudden localized pain, especially in the lower right abdomen.",
    "chest pain": (
        "**Detailed Overview:** Chest pain can be a symptom of anything from indigestion to a heart attack.\n\n"
        "**Immediate Action:** If the pain is severe, crushing, or radiating to the left arm or jaw, call **108** immediately.\n\n"
        "**Management:** Rest and avoid exertion until evaluated by a professional."
    ),
    "shortness of breath": "Difficulty breathing can indicate serious cardiac or respiratory conditions. Seek emergency medical services immediately.",
    "back pain":        "Often muscular. Apply ice for 48 hours, then switch to heat. See a doctor if pain radiates down your leg or causes numbness.",
    "ear pain":         "Can be caused by infections or pressure. Apply a warm compress. See a doctor if there is drainage or hearing loss.",
    "eye pain":         "Requires professional evaluation if severe or accompanied by vision loss. Avoid rubbing the eyes.",
    "joint pain":       "Protect and rest the joint. Apply ice compresses. Persistent swelling requires medical evaluation.",

    # Diseases
    "diabetes":         "A chronic condition affecting blood sugar regulation. Requires consistent monitoring, a balanced diet, and strict adherence to medication.",
    "hypertension":     "High blood pressure often has no symptoms. Manage it by reducing sodium intake and exercising regularly.",
    "asthma":           "Requires adherence to a management plan. Use rescue inhalers for wheezing. Seek emergency care if symptoms do not improve rapidly.",
    "tuberculosis":     "A bacterial infection primarily affecting lungs. Requires a long course of antibiotics prescribed by a specialist.",
    "dengue":           "A viral infection spread by mosquitoes. Focus on hydration and pain management. Avoid ibuprofen/aspirin; use paracetamol.",
    "malaria":          "Requires immediate medical diagnosis and specific anti-malarial medication.",
    "typhoid":          "A bacterial fever. Requires antibiotics and careful hygiene. Seek medical attention immediately.",
    "anemia":           "Low red blood cell count. Often treated with iron supplements and dietary changes after a blood test.",
    "arthritis":        "Chronic joint inflammation. Managed through low-impact exercises and anti-inflammatory therapies.",
    "thyroid":          "Disorders causing metabolism issues. Requires professional evaluation via TSH blood tests and prescription medication.",
    "covid":            "Viral respiratory illness. Isolate and monitor oxygen levels. Seek emergency care for trouble breathing or persistent chest pain.",
    "pneumonia":        "A serious lung infection causing cough and fever. Requires professional diagnosis and often antibiotics.",
    "hepatitis":        "Inflammation of the liver. Avoid alcohol and seek specialist care for long-term management.",
    "obesity":          "Increases risk for many health issues. Focus on sustainable lifestyle changes involving nutrition and physical activity.",
    "migraine":         "Severe throbbing pain with light sensitivity. Rest in a dark room and use prescribed migraine medication.",
    "osteoporosis":     "Weakens bones. Support health with calcium, Vitamin D, and weight-bearing exercises.",
    "eczema":           "Causes dry, itchy skin. Hydrate skin frequently with thick, fragrance-free creams.",
    "psoriasis":        "Chronic autoimmune condition. Keep skin moisturized and manage stress levels.",
    "kidney disease":   "Affects blood filtration. Requires low-sodium diet and careful monitoring by a nephrologist.",
    "heart disease":    "Requires a heart-healthy diet, regular exercise, and strict adherence to specialist-prescribed medications.",

    # Nutrition & Mental Health
    "protein":          "Essential for muscle repair. Sources include lean meats, beans, tofu, and dairy.",
    "vitamin":          "Essential micronutrients. A diverse diet of fruits and vegetables usually provides adequate amounts.",
    "calcium":          "Vital for bone health. Found in dairy, leafy greens, and fortified plant milks.",
    "water":            "Essential for all body functions. Aim for 8 glasses a day, more if active.",
    "healthy diet":     "A balance of lean protein, healthy fats, and complex carbohydrates with plenty of vegetables.",
    "stress":           "Chronic stress impacts health. Practice deep breathing, regular exercise, and set boundaries.",
    "anxiety":          "Can cause racing thoughts and rapid heartbeat. Grounding techniques and professional therapy are highly effective.",
    "depression":       "A medical condition causing persistent sadness. Please reach out to a doctor or a mental health professional.",
    "insomnia":         "Difficulty sleeping. Maintain a consistent schedule and avoid screens before bed.",

    # First Aid
    "burn":             "For minor burns, run cool water over the area for 10 minutes. Do not use ice or butter.",
    "cut":              "Apply pressure to stop bleeding, clean with soap and water, and cover with a sterile bandage.",
    "fracture":         "Immobilize the area and seek medical attention immediately. Do not try to realign the bone.",
    "choking":          "Perform the Heimlich maneuver if the person cannot breathe or speak. Call 108.",
    "emergency":        "In any life-threatening situation, call your local emergency number (**108**) immediately.",
    "cpr":              "Push hard and fast in the center of the chest (100-120 bpm). Call **108** first.",
}

EMERGENCIES = [
    "heart attack", "stroke", "unconscious", "severe bleeding",
    "suicide", "overdose", "chest pain", "difficulty breathing"
]

DEFAULT_RESPONSE = (
    "I'm not sure I understand that specific term. Could you describe your symptom using "
    "keywords like 'fever', 'asthma', or 'stress'? Remember, I am an AI assistant, not a doctor. "
    "In an emergency, call **108**."
)

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower().strip()

    is_emergency = any(keyword in user_message for keyword in EMERGENCIES)

    response_text = ""
    if is_emergency:
        response_text += (
            "⚠️ **EMERGENCY WARNING:** Your symptoms may indicate a life-threatening condition. "
            "Please call **108** or your local emergency services immediately.\n\n"
        )

    matched_key = next((key for key in MEDICAL_DATA if key in user_message), None)
    response_text += MEDICAL_DATA.get(matched_key, DEFAULT_RESPONSE)

    return jsonify({
        "response": response_text,
        "isEmergency": is_emergency
    })


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
