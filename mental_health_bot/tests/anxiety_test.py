def interpret_anxiety_score(score):
    if score <= 4:
        return "Minimal anxiety."
    elif score <= 8:
        return "Mild anxiety. Some light coping strategies may help."
    elif score <= 12:
        return "Moderate anxiety. It may help to talk to someone."
    else:
        return "Severe anxiety. Please consider seeking professional support."
