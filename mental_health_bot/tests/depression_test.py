def run_depression_test(answers):
    score = sum(answers)
    if score < 3:
        return "Minimal depression symptoms. Great job!"
    elif score < 5:
        return "Mild depression symptoms. Keep checking in with yourself."
    elif score < 7:
        return "Moderate depression symptoms. You might benefit from additional support."
    else:
        return "Severe depression symptoms. Please consider seeking professional help."
