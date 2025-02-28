from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for local testing (remove in production if not needed)

# Simulated documentation index (unchanged for now, but could be expanded)
documentation_index = {
    "segment": {
        "set up a new source": "To set up a new source in Segment: 1. Log in to your Segment workspace. 2. Navigate to 'Sources' in the left sidebar. 3. Click 'Add Source', choose your source type (e.g., JavaScript), and follow the setup instructions.",
        "track events": "To track events in Segment: 1. Use the Segment SDK or API. 2. Call the `track` method with event name and properties. 3. Ensure the source is set up.",
        "audience creation": "Segment’s audience creation uses Personas. Go to 'Personas', define criteria using the visual builder, and sync to downstream tools."
    },
    "mparticle": {
        "create a user profile": "To create a user profile in mParticle: 1. Ensure event data is sent via SDK or API. 2. mParticle automatically unifies events into profiles using identity resolution. 3. View profiles in the 'Audience' section.",
        "send data": "To send data to mParticle: 1. Use the mParticle SDK or API. 2. Send events with user IDs and attributes. 3. Configure your data plan.",
        "audience creation": "mParticle’s Audiences feature lets you build segments. Go to 'Audiences', set criteria (e.g., event attributes), and distribute to tools."
    },
    "lytics": {
        "build an audience segment": "To build an audience in Lytics: 1. Go to 'Audiences' in the dashboard. 2. Use the builder to set behavioral criteria (e.g., 'likely to buy'). 3. Save and export to marketing tools.",
        "export data": "To export data from Lytics: 1. Go to 'Data Exports'. 2. Select your audience or dataset. 3. Choose the destination (e.g., CSV, API).",
        "audience creation": "Lytics uses AI-driven segmentation. In 'Audiences', define rules or use pre-built options, and it updates in real-time."
    },
    "zeotap": {
        "integrate my data": "To integrate data with Zeotap: 1. Access the 'Data Sources' module. 2. Add a new source (e.g., CRM or app data). 3. Map fields to unify into customer profiles.",
        "create a segment": "To create a segment in Zeotap: 1. Go to 'Audiences'. 2. Use condition blocks to define criteria. 3. Activate across platforms.",
        "audience creation": "Zeotap’s Audience Module simplifies this. Go to 'Audiences', use condition blocks to define segments, and activate across platforms."
    }
}

FALLBACK_RESPONSE = "Sorry, I can only help with questions about Segment, mParticle, Lytics, or Zeotap. Please ask a 'how-to' question related to one of these CDPs!"

def normalize_question(question):
    return question.lower().strip()

def parse_question(question):
    question = normalize_question(question)
    cdps = ["segment", "mparticle", "lytics", "zeotap"]
    detected_cdp = None
    for cdp in cdps:
        if cdp in question:
            detected_cdp = cdp
            break
    if not detected_cdp:
        return None, None
    
    # Improve task extraction by removing common phrases and focusing on key actions
    task = re.sub(r'how (do|can|to|should) i ', '', question)
    task = re.sub(r'in ' + detected_cdp, '', task).strip()
    task = re.sub(r'\?$', '', task).strip()  # Remove trailing question mark
    
    # Simplify task to key phrases (focus on verbs and nouns)
    task_words = [word for word in task.split() if word not in ['a', 'an', 'the', 'and', 'or']]
    task = ' '.join(task_words)
    
    return detected_cdp, task

def find_answer(cdp, task):
    if cdp not in documentation_index:
        return "Sorry, I couldn’t find information for that CDP."
    
    # Use fuzzy matching or broader keyword search
    best_match = None
    best_score = -1
    
    for key in documentation_index[cdp]:
        # Calculate a simple score based on word overlap
        key_words = set(key.split())
        task_words = set(task.split())
        overlap = len(key_words.intersection(task_words))
        total_words = len(key_words.union(task_words))
        
        if total_words > 0:
            score = overlap / total_words  # Simple similarity score
            if score > best_score:
                best_score = score
                best_match = key
    
    if best_match and best_score > 0.3:  # Threshold for a reasonable match
        return documentation_index[cdp][best_match]
    return f"Sorry, I couldn’t find instructions for '{task}' in {cdp.capitalize()}."

def process_question(question):
    cdp, task = parse_question(question)
    if not cdp:
        return FALLBACK_RESPONSE
    if "compare to" in question or "difference between" in question:
        return handle_comparison(question)
    return find_answer(cdp, task)

def handle_comparison(question):
    cdps = ["segment", "mparticle", "lytics", "zeotap"]
    detected_cdps = [cdp for cdp in cdps if cdp in question]
    if len(detected_cdps) < 2:
        return "Please specify two CDPs to compare (e.g., 'How does Segment compare to Lytics?')."
    cdp1, cdp2 = detected_cdps[0], detected_cdps[1]
    task = "audience creation"  # Default task for comparison
    return (f"Comparing {cdp1.capitalize()} and {cdp2.capitalize()} for '{task}':\n"
            f"- {cdp1.capitalize()}: {find_answer(cdp1, task)}\n"
            f"- {cdp2.capitalize()}: {find_answer(cdp2, task)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    answer = process_question(question)
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)