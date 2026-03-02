# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id score per line)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    passing_count = 0
    
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')
    
    for line in infile:
        if len(line) >= 7:
            student_id = line[0:4]

            score = int(line[5:])

            if score >= 80:

                outfile.write(student_id + " " + str(score) + "\n")
                passing_count += 1
                
    infile.close()
    outfile.close()
    
    return passing_count

# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/data/passing.txt")
print(f"Passing students: {result}")
