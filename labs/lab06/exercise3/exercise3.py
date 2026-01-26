def audit_blocklists(list_a, list_b, list_c):
    universal = list_a & list_b & list_c

    redundant = (list_a & list_b) | (list_b & list_c) | (list_c & list_a)

    unique_a = list_a - list_b - list_c

    return (universal, redundant, unique_a)