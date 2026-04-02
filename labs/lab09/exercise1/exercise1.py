import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)
    total = len(df)
    subject = ["Math", "Science", "English"]
    math_average = round(df["Math"].mean(),1)
    highest_score = df["Math"].max()
    top_student = df.loc[df["Math"] == highest_score, "Name"].values[0]
    
    return {
        "total subjects": total,
        "subjects": subject,
        "math_average": math_average,
        "top_scorer": top_student
    }

result = explore_data("labs/lab09/data/students.csv")
print(result)