def get_student_courses(enrollments, student_id):
    """Return a set of all unique courses this specific student has completed."""
    completed = set()
    for sid, course in enrollments:
        if sid == student_id:
            completed.add(course)
    return completed

def find_missing_courses(completed_courses, required_courses):
    """Use set difference (-) to efficiently find required courses not yet completed."""
    return required_courses - completed_courses

def build_student_report(students, enrollments, required_courses):
    """Build and return a sorted list of tuples (missing_count, student_id)."""
    report = []
    for student_id in students:
        completed = get_student_courses(enrollments, student_id)
        missing = find_missing_courses(completed, required_courses)
        
        if len(missing) > 0:
            report.append((len(missing), student_id))
    
    return sorted(report, reverse=True)

def find_incomplete_students(enrollments, required_courses):
    """Main orchestrator function to find students with incomplete requirements."""
    all_students = set()
    for student_id, course in enrollments:
        all_students.add(student_id)
        
    return build_student_report(all_students, enrollments, required_courses)