This project is an AI-powered chatbot built with Python and Flask. It answers mental health-related FAQs and also allows users to take stress, anxiety, and depression assessments.

📦 Prerequisites
Before running the chatbot, make sure you have:

Python 3.7 or higher

pip (Python package manager)

🔧 Installation Steps
1. ✅ Clone or Download the Project
Download the ZIP or clone the repo:

bash
Copy
Edit
git clone <your-repo-url>
cd mental_health_bot
2. ✅ Create a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\\Scripts\\activate     # On Windows
3. ✅ Install Required Python Packages
Run this command to install dependencies:

bash
Copy
Edit
pip install flask spacy
Then download the required Spacy model:

bash
Copy
Edit
python -m spacy download en_core_web_lg
🚀 How to Run the Bot
Once all packages are installed, run the Flask app:

bash
Copy
Edit
python app.py
Then open your browser and go to:

arduino
Copy
Edit
http://localhost:5000
💬 How It Works
Type your mental health question or concern.

If your question matches one or more of the 40+ FAQs (using cosine similarity ≥ 0.70), the bot gives the top 2 answers.

It also suggests a Stress / Anxiety / Depression Test based on your input.

Click the button to take the test directly in the chat window.

📁 Key Files
File	Purpose
app.py	Flask backend entry point
chatbot/logic.py	Handles FAQ matching & test logic
chatbot/faq_data.py	Contains all FAQs and answers
templates/index.html	Frontend chatbot UI
tests/*.py	Logic for stress/anxiety/depression tests
