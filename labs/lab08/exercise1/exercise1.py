# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id and score on alternating lines)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    passing_count = 0
    
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')
    
    student_id = infile.readline()
    
    while student_id != "":
        score_line = infile.readline()
        
        student_id = student_id.strip()
        score = int(score_line.strip())
        
        if score >= 80:
            outfile.write(student_id + " " + str(score) + "\n")
            passing_count += 1
        
        student_id = infile.readline()
    
    infile.close()
    outfile.close()
    
    return passing_count

# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/data/passing.txt") 
print(f"Passing students: {result}")
