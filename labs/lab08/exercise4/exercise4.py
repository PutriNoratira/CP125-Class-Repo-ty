# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:
import csv

def calculate_final_grades(input_file, output_file):
    """
    Calculate final grades from midterm and final scores.

    Args:
        input_file: path to scores CSV (student_id,midterm,final)
        output_file: path to output CSV file

    Returns:
        float: average of all final grades
    """
    total_final_grades = 0
    student_count = 0
    
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w', newline='')
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    writer.writerow(["student_id", "final_grade"])
    
    is_header = True
    for row in reader:
        if is_header:
            is_header = False
            continue
            
        student_id = row[0]
        midterm = float(row[1])
        final_exam = float(row[2])
        
        # Weighted formula calculation
        final_grade = (midterm * 0.4) + (final_exam * 0.6)
        
        # Accumulate totals for the average
        total_final_grades += final_grade
        student_count += 1
        
        writer.writerow([student_id, f"{final_grade:.2f}"])
        
    infile.close()
    outfile.close()
    
    return total_final_grades / student_count

# Test your code here
result = calculate_final_grades("labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")
