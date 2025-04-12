import spacy
from chatbot.faq_data import faq_data

nlp = spacy.load("en_core_web_lg")

def get_response(user_input):
    user_doc = nlp(user_input)
    matches = []

    # Step 1: Collect all matches ≥ 0.80
    for question, answer in faq_data:
        score = user_doc.similarity(nlp(question))
        if score >= 0.80:
            matches.append((score, question, answer))

    # Step 2: Show top 2 if matches found
    if matches:
        matches.sort(reverse=True)  # Sort by similarity
        top_matches = matches[:2]
        response = ""
        for _, q, a in top_matches:
            response += f"{a}\n\n"

        # Step 3: Add relevant test prompt
        user_lower = user_input.lower()
        if "depression" in user_lower:
            response += "||TEST:depression"
        elif "anxiety" in user_lower or "anxious" in user_lower:
            response += "||TEST:anxiety"
        elif "stress" in user_lower:
            response += "||TEST:stress"

        return response.strip()

    # Step 4: Fallback if no match
    if "stress" in user_lower:
        return "It seems you're talking about stress.||TEST:stress"
    elif "anxious" in user_lower or "anxiety" in user_lower:
        return "It seems you're feeling anxious.||TEST:anxiety"
    elif "depressed" in user_lower or "depression" in user_lower:
        return "You mentioned depression.||TEST:depression"

    return "I'm here to listen. Try asking about mental health topics or take a quick test."
