// script.js
document.getElementById('question-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const question = document.getElementById('question').value;
    const responseElement = document.getElementById('response');

    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question })
        });
        const data = await response.json();
        responseElement.textContent = `Response: ${data.response}`;
    } catch (error) {
        responseElement.textContent = 'An error occurred. Please try again.';
    }
});
