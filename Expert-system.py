diseases = {
    "Flu": (["fever", "cough", "sore throat"], "Drink plenty of fluids and rest."),
    "Cold": (["sneezing", "running nose"], "Stay warm and rest."),
    "Malaria": (["fever", "chills"], "See the doctor immediately."),
    "Covid-19": (["fever", "cough", "loss of taste"], "Isolate yourself and consult a doctor.")
}

def expert_system(symptoms):
    result = ""
    for name, (symptom_list, treatment) in diseases.items():
        if any(s in symptom_list for s in symptoms):
            result += "\n" + "="*40 + "\n"
            result += "Disease  : " + name + "\n"
            result += "Treatment: " + treatment + "\n"
            result += "="*40 + "\n"
    return result if result else "\nNo matching disease or treatment found."

symptoms_input = input("Enter the symptoms (comma-separated): ").lower()
symptoms_list = [s.strip() for s in symptoms_input.split(",")]

print(expert_system(symptoms_list))
