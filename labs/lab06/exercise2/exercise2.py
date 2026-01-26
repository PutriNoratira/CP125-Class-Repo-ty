def match_specialists(candidates_list, project_requirements):
    skill_count = {}

    for name, skills in candidates_list:
        for skill in skills:
            if skill not in skill_count:
                skill_count[skill] = 0
            skill_count[skill] += 1

    rare_skills_pool = set()

    for skill, count in skill_count.items():
        if count < 3:
            rare_skills_pool.add(skill)

    specialist = []

    for name, skills in candidates_list:
        missing_reqs = project_requirements - skills
        if missing_reqs == set():
            my_rare_skills = skills & rare_skills_pool
            if len(my_rare_skills) > 0:
                specialist.append((name, my_rare_skills))
    
    return specialist