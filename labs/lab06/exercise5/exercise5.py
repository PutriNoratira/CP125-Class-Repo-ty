def audit_zero_trust(baseline_set, current_log_list):
    logs_set = set(current_log_list)

    authorized = baseline_set & logs_set

    alerts = logs_set - baseline_set

    inactive = baseline_set - logs_set

    return (authorized, alerts, inactive)
