
def find_conflicting_ports(rules):
    ports = set()
    for rule in rules:
        ports.add(rule[1])

    conflicts = []

    for port in ports:
        first_action = ""
        for rule_id, rule_port, action in rules:
            if rule_port == port:
                first_action = action
                break

        for rule_id, rule_port, action in rules:
            if rule_port == port and action != first_action:
                conflicts.append((port, rule_id))
                break
    
    conflicts.sort()
    return conflicts

rules = [
    (1, 80, "ALLOW"), 
    (2, 443, "ALLOW"), 
    (3, 80, "BLOCK"),
    (4, 22, "BLOCK"), 
    (5, 443, "BLOCK"), 
    (6, 8080, "ALLOW")
]

result = find_conflicting_ports(rules)
print(f"Conflicts: {result}")

rules2 = [
    (1, 80, "ALLOW"), 
    (2, 80, "ALLOW"), 
    (3, 443, "BLOCK")
]

result2 = find_conflicting_ports(rules2)
print(f"Conflicts: {result2}")
