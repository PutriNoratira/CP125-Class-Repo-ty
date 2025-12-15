''' 
    My name is Tira.
    The problem that I need to solve is to create a function
    that will let the user input the mark and return the grade
'''
def determine_grade (mark):
    if mark >= 80:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"
    
    return grade

mark = float(input( "Enter the student's mark: "))
final_grade = determine_grade(mark)

print (f"Mark: {mark}, Grade: {final_grade}")