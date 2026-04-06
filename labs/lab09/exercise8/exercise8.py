import pandas as pd
import matplotlib.pyplot as plt

def plot_subject_maximums(filename):
    df = pd.read_csv(filename)

    subjects = ['Math', 'Science', 'English', 'Physics', 'Chemistry']
    max_scores = [df[subject].max() for subject in subjects]

    plt.plot(subjects, max_scores, marker='o')
    plt.xlabel("Subjects")
    plt.ylabel("Maximum Scores")
    plt.title("Maximum Scores by Subjects")
    #plt.show()

    return len(df)

result = plot_subject_maximums("labs/lab09/data/students.csv")
print(result)