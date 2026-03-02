def manage_roster(enrolled, drop_requests, waitlist):
    for student in drop_requests:
        if student in enrolled:
            enrolled.remove(student)

    if len(enrolled) < 5:
        while len(enrolled) < 7 and len(waitlist) > 0:
            new_student = waitlist.pop()
            enrolled.add(new_student)
    
    return len(enrolled)