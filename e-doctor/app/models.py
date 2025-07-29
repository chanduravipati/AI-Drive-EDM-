from . import mongo

def recommend_medicine(disease):
    # Looks up a medicine recommendation for a given disease
    record = mongo.db.medicines.find_one({"disease": disease.lower().strip()})
    return record["medicines"] if record else ["No recommendation available"]

def diagnose_disease(symptoms_text):
    # Splits and normalizes the input symptoms
    input_symptoms = set(sym.strip().lower() for sym in symptoms_text.split(","))
    matched_diseases = set()

    # Loops through your current MongoDB structure (symptom + diseases)
    rules = mongo.db.diagnosis_rules.find()
    for rule in rules:
        symptom = rule.get("symptom", "").strip().lower()
        if symptom in input_symptoms:
            matched_diseases.update(rule.get("diseases", []))

    return list(matched_diseases) if matched_diseases else ["Unknown"]
