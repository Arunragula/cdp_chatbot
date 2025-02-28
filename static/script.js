document.getElementById('chat-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const questionInput = document.getElementById('question');
    const question = questionInput.value.trim();
    if (!question) return;

    // Add user's message to the chat
    addMessage('user', question);
    questionInput.value = ''; // Clear input

    // Send question to the server
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'question': question
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Parse JSON response
    })
    .then(data => {
        // Add bot's response to the chat using the 'answer' from the JSON
        if (data.answer) {
            addMessage('bot', data.answer);
        } else {
            addMessage('bot', 'Sorry, no answer was received from the server.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        addMessage('bot', 'Sorry, something went wrong. Please try again.');
    });
});

function addMessage(sender, content) {
    const messagesContainer = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);

    const messageContent = document.createElement('div');
    messageContent.classList.add('message-content');
    messageContent.textContent = content;

    messageDiv.appendChild(messageContent);
    messagesContainer.appendChild(messageDiv);

    // Auto-scroll to the latest message
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}