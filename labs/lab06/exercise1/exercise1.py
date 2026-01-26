def get_legit_power_users(log_data, bot_ids, threshold):
    user_actions = {}

    for timestamps, user_id, action_type in log_data:
        if user_id in bot_ids:
            continue
        if user_id not in user_actions:
            user_actions[user_id] = set()
        user_actions[user_id].add(action_type)

    power_users = []
    for user_id, actions in user_actions.items():
        if len(actions) > threshold:
            power_users.append(user_id)
    
    return sorted(power_users)