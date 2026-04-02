import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)
    total = len(df)
    subject = ["Math", "Science", "English"]
    math_average = round(df["Math"].mean(),1)
    highest_score = df["Math"].max()
    top_student = df.loc[df["Math"] == highest_score, "Name"].values[0]
    print(math_average)
    return {
        "total_students": total,
        "subjects": subject,
        "math_average": float(math_average),
        "highest_math_student": top_student
    }

result = explore_data("labs/lab09/data/students.csv")
print(result)