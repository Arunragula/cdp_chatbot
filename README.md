# cdp_chatbot

![image](https://github.com/user-attachments/assets/0a789d2d-ebc2-4696-a920-eec576857ae2)
Overview

This is a chatbot application designed to provide support for Customer Data Platforms (CDPs) like Segment, mParticle, Lytics, and Zeotap. It answers user queries based on predefined documentation.

Features

Flask-based API for handling queries

Chat interface for user interaction

Supports CDP-specific queries

Implements fuzzy matching for better responses

Allows feature comparison between CDPs

Installation & Setup

Install dependencies:

pip install flask flask-cors

Run the application:

python app.py

Open http://127.0.0.1:5000/ in a web browser.

Usage

Type a query in the chat interface related to Segment, mParticle, Lytics, or Zeotap.

The chatbot will provide relevant responses based on available documentation.

File Structure

app.py: Backend logic (Flask API)

index.html: Frontend chat interface

style.css: Styling for the UI

script.js: Handles client-side interactions

License

This project is for educational purposes only.
