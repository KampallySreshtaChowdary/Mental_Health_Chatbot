def run_stress_test(answers):
    score = sum(answers)
    if score < 3:
        return "Your stress level is low. Keep up the good work!"
    elif score < 6:
        return "Moderate stress detected. Let's explore coping strategies."
    else:
        return "You seem to be under high stress. Consider reaching out for support."
