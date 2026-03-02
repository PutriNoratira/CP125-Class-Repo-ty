def apply_upgrade(current, upgrade):
    final_permissions = current.copy()
    
    for permission, new_level in upgrade.items():
        if permission not in final_permissions:
            final_permissions[permission] = new_level
        elif new_level > final_permissions[permission]:
            final_permissions[permission] = new_level
            
    return final_permissions

current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result) 
print(current) 