import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)
    
    math_criteria = df['Math'] > 85
    science_criteria = df['Science'] > 85
    english_criteria = df['English'] > 85

    high_performers_df = df.loc[math_criteria & science_criteria & english_criteria, 'Name']
    names_set = set(high_performers_df)
    count = len(names_set)
    
    return {
        "count": count,
        "names": names_set
    }

result = high_performers("labs/lab09/data/students.csv")
print(result)