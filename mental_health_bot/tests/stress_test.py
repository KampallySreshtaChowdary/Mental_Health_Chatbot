def interpret_stress_score(score):
    if score <= 4:
        return "Low stress level. You're managing things well!"
    elif score <= 8:
        return "Moderate stress level. Be mindful and consider relaxing activities."
    elif score <= 12:
        return "High stress level. You might benefit from stress-reduction techniques."
    else:
        return "Severe stress. Please consider talking to a counselor or professional."
