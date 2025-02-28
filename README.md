# CDP Chatbot

![CDP Chatbot Screenshot](https://github.com/user-attachments/assets/0a789d2d-ebc2-4696-a920-eec576857ae2)

## Overview

The CDP Chatbot is a web-based application designed to provide support and answers for Customer Data Platforms (CDPs) such as Segment, mParticle, Lytics, and Zeotap. Built with Flask, this chatbot offers an interactive chat interface where users can ask "how-to" questions related to setting up, configuring, or comparing these CDPs. It uses predefined documentation and implements fuzzy matching to deliver relevant responses, making it a valuable tool for developers and businesses working with CDPs.

## Features

- **Flask-based API**: A robust backend for handling user queries and generating responses.
- **Interactive Chat Interface**: A user-friendly frontend built with HTML, CSS, and JavaScript for real-time interaction.
- **CDP-Specific Support**: Answers questions about Segment, mParticle, Lytics, and Zeotap, including setup, tracking, audience creation, and more.
- **Fuzzy Matching**: Implements fuzzy logic to match user queries to documentation, improving response accuracy.
- **Feature Comparison**: Allows users to compare features between CDPs (e.g., "How does Segment compare to Lytics?").

## Installation & Setup

To run the CDP Chatbot locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Arunragula/cdp_chatbot.git
   cd cdp_chatbot

Install Dependencies:
Install the required Python packages using pip:
bash

pip install -r requirements.txt

If requirements.txt isn’t present, create it by running:
bash

pip freeze > requirements.txt

Ensure the following packages are included:
Flask==3.0.3 (or your version)

flask-cors==4.0.0 (or your version)

gunicorn==22.0.0 (for production deployment)

Run the Application:
Start the Flask server locally:
bash

python app.py

Alternatively, use Gunicorn for testing production-like behavior:
bash

gunicorn --bind 0.0.0.0:5000 wsgi:app

Access the Chatbot:
Open your web browser and navigate to http://127.0.0.1:5000/ to interact with the chatbot.

Usage
Open the chat interface in your browser.

Type a query in the input field, such as:
"How do I set up a new source in Segment?"

"How does Lytics compare to mParticle?"

The chatbot will provide a response based on its documentation for the specified CDP.


Deployment
To deploy the CDP Chatbot, you can use platforms like Heroku, Render, or Google Cloud Run. Below is an example for deploying to Heroku:
Install Heroku CLI:
Follow instructions at heroku.com.

Log In to Heroku:
bash

heroku login

Create a Heroku App:
bash

heroku create cdp-chatbot-app

Push to Heroku:
bash

git push heroku main

Open the App:
bash

heroku open

For other platforms (e.g., Render, Google Cloud Run), refer to their documentation and adjust the configuration (e.g., Dockerfile for Google Cloud Run).
License
This project is for educational purposes only and is not intended for commercial use without modification or permission. Feel free to fork, contribute, or use it as a learning resource.
Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you’d like to change.
Contact
For questions or feedback, contact Arun Ragula via GitHub or email (if available). You can also open an issue in this repository.

---

### Why This Enhanced README?
- **GitHub Markdown**: Uses Markdown syntax (`#`, `##`, `![image]`, etc.) for formatting on GitHub.
- **Detailed Instructions**: Provides clear steps for installation, usage, and deployment, making it easier for others (or future you) to understand and use the project.
- **Professional Look**: Includes sections like “Overview,” “Features,” “File Structure,” “Deployment,” “License,” and “Contributing,” which are standard for open-source projects.
- **Image Integration**: Embeds the screenshot you provided, enhancing visual appeal on GitHub.
- **Deployment Guidance**: Adds deployment instructions for Heroku (based on our previous discussions) and mentions alternatives, helping users deploy the app.

---

### Steps to Push This README to GitHub

1. **Create or Update `README.md`**:
   - Save the enhanced README above as `README.md` in your project root directory (e.g., `C:\Users\USER\arun\myenv\cdp_chatbot\`).

2. **Add and Commit the File**:
   - In your terminal, navigate to the project directory and run:
     ```bash
     git add README.md
     git commit -m "Add enhanced README for GitHub"
     ```

3. **Push to GitHub**:
   - Ensure you’ve resolved the `unrelated histories` issue from your previous error (as discussed earlier). If you’ve already merged or rebased, push the changes:
     ```bash
     git push origin main
     ```
   - If you encounter the same error again, use:
     ```bash
     git pull origin main --allow-unrelated-histories
     ```
     Then resolve any conflicts and push again.

4. **Verify on GitHub**:
   - Visit `https://github.com/Arunragula/cdp_chatbot` and confirm the `README.md` appears on the repository’s main page with the formatted text and image.

---

### Deploying the Flask App
Since you mentioned deployment, here’s a quick recap of deploying your Flask app to Heroku (or another platform) after pushing to GitHub:

#### Deploy to Heroku
1. **Install Heroku CLI** and log in:
   ```bash
   heroku login

Create requirements.txt (if not already done):
bash

pip freeze > requirements.txt

Create Procfile and wsgi.py (as shown in the README):
Procfile:

web: gunicorn --bind 0.0.0.0:5000 wsgi:app

wsgi.py:
python

from app import app

if __name__ == "__main__":
    app.run()

Create a Heroku App and Push:
bash

heroku create cdp-chatbot-app
git push heroku main
heroku open

Alternative Platforms
Render: Connect your GitHub repo, configure a Python web service, and deploy (see Render’s docs at render.com).

Google Cloud Run/AWS: Requires Docker and more advanced configuration (see their docs for details).

Additional Tips
Image Hosting: Ensure the image URL (https://github.com/user-attachments/assets/0a789d2d-ebc2-4696-a920-eec576857ae2) is publicly accessible on GitHub or another service. If it’s a GitHub attachment, it should work as-is, but test it in the README preview.

Version Control: Keep your requirements.txt, Procfile, and wsgi.py in Git to simplify deployment for others.

Contributing Guidelines: If you plan to invite contributions, consider adding a CONTRIBUTING.md file with more detailed instructions.


