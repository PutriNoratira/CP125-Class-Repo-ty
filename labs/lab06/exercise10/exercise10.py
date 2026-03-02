def get_unique_attendees(attendance_logs):
    """Extract set of all unique attendee IDs."""
    unique_ids = set()
    for attendee_id, event_name in attendance_logs:
        unique_ids.add(attendee_id)
    return unique_ids

def count_unique_events(attendance_logs, attendee_id):
    """Count how many unique events this attendee attended."""
    events_attended = set()
    # FIX: Iterate through attendance_logs, NOT attendee_id
    for att_id, event_name in attendance_logs:
        if att_id == attendee_id:
            events_attended.add(event_name)
    return len(events_attended)

def filter_by_threshold(attendees, attendance_logs, min_events):
    """Return sorted list of attendees who attended >= min_events."""
    qualified = []
    for attendee_id in attendees:
        count = count_unique_events(attendance_logs, attendee_id)
        if count >= min_events:
            qualified.append(attendee_id)
    return sorted(qualified)

def find_frequent_attendees(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""
    all_attendees = get_unique_attendees(attendance_logs)
    return filter_by_threshold(all_attendees, attendance_logs, min_events)