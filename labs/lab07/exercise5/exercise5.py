def find_at_risk_departments(departments, threshold):
    at_risk = []
    
    for dept_name, students_dict in departments.items():
        scores = list(students_dict.values())
        below_threshold_count = sum(1 for score in scores if score < threshold)

        if below_threshold_count > (len(scores) / 2):
            at_risk.append(dept_name)
            
    at_risk.sort()
    return at_risk

departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}

print(find_at_risk_departments(departments, 65))