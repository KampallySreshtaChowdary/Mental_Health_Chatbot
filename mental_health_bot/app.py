from flask import Flask, render_template, request, session, jsonify
from tests.stress_test import interpret_stress_score
from tests.anxiety_test import interpret_anxiety_score
from tests.depression_test import interpret_depression_score


app = Flask(__name__)
app.secret_key = 'mental-health-secret'

@app.route("/")
def home():
    return render_template("dashboard.html", scores=session.get('scores', {}))

@app.route("/test/<test_type>")
def test_page(test_type):
    test_data = {
        "stress": {
            "title": "Stress Test",
            "questions": [
                ("When you feel overwhelmed, what do you usually do?", [("Go for a walk to clear your mind", 0), ("Talk to someone close", 1), ("Ignore it and bottle it up", 2), ("Get angry or shut down", 3)]),
                ("How do you usually sleep when you're under pressure?", [("I sleep well", 0), ("Toss and turn a bit", 1), ("Wake up often at night", 2), ("Barely sleep at all", 3)]),
                ("You’ve got multiple deadlines tomorrow — what’s your reaction?", [("Plan ahead calmly", 0), ("Feel the pressure but manage", 1), ("Feel panicked but try", 2), ("Break down or avoid it", 3)]),
                ("How does your body respond during stress?", [("Relaxed and grounded", 0), ("Slightly restless", 1), ("Tense and uneasy", 2), ("Chest tight, sweating, can't sit still", 3)]),
                ("How often do people comment you're 'stressed out'?", [("Rarely or never", 0), ("Occasionally", 1), ("Often", 2), ("All the time", 3)])
            ]
        },
        "anxiety": {
            "title": "Anxiety Test",
            "questions": [
                ("You're in a crowd and hear a loud noise. What’s your gut reaction?", [("Ignore it and continue", 0), ("Feel a little on edge", 1), ("Start scanning for danger", 2), ("Panic or freeze", 3)]),
                ("Before an important event, what’s on your mind?", [("I stay focused", 0), ("Mild nervousness", 1), ("What if everything goes wrong?", 2), ("Replay worst-case scenarios", 3)]),
                ("You get a message saying 'we need to talk'. What do you feel?", [("Normal curiosity", 0), ("A bit of worry", 1), ("Anxious thoughts loop", 2), ("Full-on dread", 3)]),
                ("How do you physically feel when anxious?", [("Light flutter in stomach", 0), ("Tense shoulders", 1), ("Heart races, hard to breathe", 2), ("Shaking or sweating", 3)]),
                ("When plans change suddenly, how do you feel?", [("I adapt easily", 0), ("I need a minute", 1), ("I get upset", 2), ("It ruins my whole mood", 3)])
            ]
        },
        "depression": {
            "title": "Depression Test",
            "questions": [
                ("How motivated do you feel to get out of bed most days?", [("Refreshed and ready", 0), ("Neutral", 1), ("Tired but push through", 2), ("Exhausted and unwilling", 3)]),
                ("Someone invites you to a gathering. You think...", [("'Sounds fun!'", 0), ("'Okay, maybe...'", 1), ("'I'd rather stay in'", 2), ("'No way, not going'", 3)]),
                ("How often do you feel like you're failing or not enough?", [("Not really", 0), ("Sometimes", 1), ("More than I'd like", 2), ("Every single day", 3)]),
                ("How’s your energy during the day?", [("Energized and productive", 0), ("Up and down", 1), ("Always low", 2), ("Drained and stuck", 3)]),
                ("Do your favorite hobbies still feel enjoyable?", [("Yes, always", 0), ("Not as much", 1), ("Rarely", 2), ("Not at all anymore", 3)])
            ]
        }
    }

    if test_type not in test_data:
        return "Test not found", 404

    questions = [{"id": i+1, "text": q[0], "options": q[1]} for i, q in enumerate(test_data[test_type]["questions"])]
    return render_template("test_template.html", questions=questions, test_type=test_type, title=test_data[test_type]["title"])

@app.route("/submit/<test_type>", methods=["POST"])
def submit_test(test_type):
    score = sum(int(request.form.get(f"q{i+1}", 0)) for i in range(5))
    if test_type == "stress":
        interpretation = interpret_stress_score(score)
    elif test_type == "anxiety":
        interpretation = interpret_anxiety_score(score)
    elif test_type == "depression":
        interpretation = interpret_depression_score(score)
    else:
        return "Invalid test type", 400

    if 'scores' not in session:
        session['scores'] = {}
    session['scores'][test_type.capitalize()] = f"{score}"
    session.modified = True

    return render_template("result_redirect.html")

@app.route("/reset")
def reset():
    session.clear()
    return render_template("result_redirect.html")



@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "").lower()
    scores = session.get('scores', {})

    if "therapist" in message or "should i see" in message or "need help" in message:
        response = ""
        for test in ["Stress", "Anxiety", "Depression"]:
            if test in scores:
                try:
                    score_val = int(scores[test])
                except:
                    score_val = 0
                if score_val <= 4:
                    response += f"{test}: ✅ Looks good<br>"
                elif score_val <= 8:
                    response += f"{test}: ⚠️ Moderate — keep monitoring<br>"
                else:
                    response += f"{test}: ❗ High — consider seeking a therapist<br>"
            else:
                response += f"{test}: ❓ Test not taken yet<br>"
        return jsonify({"response": response})

    elif "overthinking" in message:
        return jsonify({"response": "🧠 Overthinking is common. Try journaling your thoughts, setting a 10-minute worry timer, or practicing mindfulness to let go of looping thoughts."})

    elif "panic" in message or "anxious" in message:
        return jsonify({"response": "🫁 When you panic, try the 5-4-3-2-1 grounding technique or do a 4-7-8 breathing cycle. It really helps."})

    elif "can't sleep" in message or "sleep better" in message:
        return jsonify({"response": "😴 Create a calming bedtime routine: avoid screens before bed, dim lights, and try a guided sleep meditation or herbal tea like chamomile."})

    elif "lonely" in message:
        return jsonify({"response": "💙 Feeling lonely? Try reaching out to someone you trust, join an online community, or do something creative that makes you feel connected."})

    elif "how to meditate" in message or "meditation" in message:
        return jsonify({"response": "🧘‍♀️ Find a quiet spot, sit comfortably, close your eyes, and focus on your breath. Try inhaling for 4s, hold 7s, exhale 8s.<br><br><img src='/static/mindfulness.svg' width='150'>"})

    elif "sleep" in message:
        return jsonify({"response": "😴 Trouble sleeping? Limit screens before bed, try breathing exercises, and keep your room cool and dark."})
    elif "overthink" in message:
        return jsonify({"response": "🧠 Try journaling, mindfulness, or setting a 'worry time' to manage overthinking."})
    elif re.search(r"panic|anxiety|anxious", message):
        return jsonify({"response": "😰 Use 5-4-3-2-1 grounding or deep breathing during panic or anxiety episodes."})
    elif re.search(r"lonely|alone", message):
        return jsonify({"response": "🤗 You're not alone. Reach out to someone, go outside, or try journaling your feelings."})
    elif "depressed" in message or "depression" in message:
        return jsonify({"response": "🫂 Depression is hard. Be kind to yourself and take small steps like showering, walking, or talking to a trusted person."})
    elif "calm" in message or "breathe" in message:
        return jsonify({"response": "🫁 Try the 4-7-8 technique: Inhale 4s, hold 7s, exhale 8s. It relaxes your nervous system."})
    elif "motivate" in message or "motivation" in message:
        return jsonify({"response": "💡 Start with one small task. Progress fuels motivation. Also, reward yourself after completing something hard."})
    elif "worthless" in message or "fail" in message:
        return jsonify({"response": "🧡 You are not your thoughts. Try to reframe failures as learning and talk kindly to yourself as you would to a friend."})
    else:
        return jsonify({"response": "I'm here to support you 💬. You can ask me about meditation, stress, sleep, or anything you're struggling with."})


if __name__ == "__main__":
    app.run(debug=True)


