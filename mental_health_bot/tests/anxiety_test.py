def run_anxiety_test(answers):
    score = sum(answers)
    if score < 3:
        return "Minimal anxiety. Stay mindful and healthy."
    elif score < 6:
        return "Mild anxiety. Some light coping strategies may help."
    elif score < 9:
        return "Moderate anxiety. It may help to talk to someone."
    else:
        return "Severe anxiety. Consider consulting a mental health professional."
