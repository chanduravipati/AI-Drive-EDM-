from flask import Blueprint, request, jsonify
from .models import recommend_medicine, diagnose_disease

# Create a blueprint
main = Blueprint('main', __name__)

@main.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        print("POST /recommend → Received JSON:", data)  # Debug

        if not data or not isinstance(data, dict):
            return jsonify({"detail": "Invalid JSON body"}), 400

        disease = data.get('disease', '').strip().lower()
        if not disease:
            return jsonify({"detail": "Disease is required"}), 400

        medicines = recommend_medicine(disease)
        print("→ Recommended Medicines:", medicines)  # Debug

        return jsonify({"medicines": medicines}), 200

    except Exception as e:
        print("ERROR in /recommend:", str(e))  # Debug
        return jsonify({"detail": f"An error occurred: {str(e)}"}), 500


@main.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        data = request.get_json()
        print("POST /diagnose → Received JSON:", data)  # Debug

        if not data or not isinstance(data, dict):
            return jsonify({"detail": "Invalid JSON body"}), 400

        symptoms = data.get('symptoms', '').strip().lower()
        if not symptoms:
            return jsonify({"detail": "Symptoms are required"}), 400

        diagnosis = diagnose_disease(symptoms)
        print("→ Diagnosis Result:", diagnosis)  # Debug

        return jsonify({"diagnosis": diagnosis}), 200

    except Exception as e:
        print("ERROR in /diagnose:", str(e))  # Debug
        return jsonify({"detail": f"An error occurred: {str(e)}"}), 500
