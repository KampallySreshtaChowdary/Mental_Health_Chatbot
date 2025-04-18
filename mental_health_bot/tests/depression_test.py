def interpret_depression_score(score):
    if score <= 4:
        return "Minimal depression symptoms. Great job!"
    elif score <= 8:
        return "Mild depression symptoms. Keep checking in with yourself."
    elif score <= 12:
        return "Moderate depression symptoms. Consider reaching out to a professional."
    else:
        return "Severe depression symptoms. Please seek professional support."
