import pandas as pd

def promotion_candidates(filename):
    df = pd.read_csv(filename)

    avg_perf = round(df['PerformanceScore'].mean(), 1)
    perf_criteria = df['PerformanceScore'] > avg_perf
    exp_criteria = df['YearsOfService'] > 2
    candidate_names = df.loc[perf_criteria & exp_criteria, 'EmployeeName']

    candidate_names_set = set(candidate_names)
    count_candidates = len(candidate_names_set)

    return {
        "average_performance": float(avg_perf),
        "min_years_required": 2,
        "candidate_count": count_candidates,
        "candidate_names": candidate_names_set
    }

result = promotion_candidates("labs/lab09/data/employees.csv")
print(result)