import pandas as pd

def compare_averages(filename):
    df = pd.read_csv(filename)
    math_avg = round(df["Math"].mean(),1)
    science_avg = round(df["Science"].mean(),1)
    english_avg = round(df["English"].mean(),1)
    
    averages = {
        "Math": math_avg,
        "Science": science_avg,
        "English": english_avg
    }

    best_subject = max(averages, key=averages.get)
    worst_subject = min(averages, key=averages.get)

    result = {
        "Math": float(math_avg),
        "Science": float(science_avg),
        "English": float(english_avg),
        "best_subject": best_subject,
        "worst_subject": worst_subject
    }

    return result

result = compare_averages("labs/lab09/data/students.csv")
print(result)