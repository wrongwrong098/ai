# Disease symptoms and treatments (with simple symptoms)
disease_symptoms = {
    "Flu": ["fever", "cough", "throat pain", "body pain", "tired"],
    "Cold": ["sneeze", "runny nose", "throat pain", "mild cough", "headache"],
    "Malaria": ["fever", "chills", "sweating", "nausea", "vomit"],
    "Dengue": ["high fever", "headache", "eye pain", "joint pain", "rash"],
    "Typhoid": ["fever", "stomach pain", "weakness", "no hunger", "loose motion"],
    "Asthma": ["wheezing", "breathless", "chest tight", "cough"],
}

disease_treatments = {
    "Flu": "Rest, drink water, and take medicines if needed.",
    "Cold": "Stay warm, drink fluids, and use cold syrup.",
    "Malaria": "Visit doctor and take malaria medicines.",
    "Dengue": "Rest, drink water, avoid aspirin.",
    "Typhoid": "Use antibiotics and drink water.",
    "Asthma": "Use inhaler and avoid dust.",
}

# Get symptoms from user
user_symptoms =[]
print("Enter 4 symptoms")
for i in range(4):
    user_input = input("Enter symptoms").lower()
    user_symptoms.append(user_input)

# Check if user entered enough symptoms
if len(user_symptoms) < 4:
    print("Please enter at least 4 symptoms for better diagnosis.")
else:
    disease_probabilities = {}

    # Calculate probability for each disease
    for disease, symptoms_list in disease_symptoms.items():
        symptoms_lower = [s.lower() for s in symptoms_list]
        matches = sum(1 for symptom in user_symptoms if symptom in symptoms_lower)
        if matches > 0:
            probability = (matches / len(symptoms_list)) * 100
            disease_probabilities[disease] = probability

    # Sort diseases by probability
    sorted_diseases = sorted(disease_probabilities.items(), key=lambda x: x[1], reverse=True)

    # Show results
    if sorted_diseases:
        print("\nDiagnosis Probabilities:")
        for disease, probability in sorted_diseases:
            print(f"\n-> Disease: {disease}")
            print(f"   -> Probability: {probability:.2f}%")
            print(f"   -> Treatment: {disease_treatments[disease]}")
    else:
        print("\nNo matching disease found. Please consult a doctor.")
