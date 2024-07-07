document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('startBtn');
    const outputDiv = document.getElementById('output');

    startBtn.addEventListener('click', () => {
        outputDiv.innerHTML = 'Starting Assistant...';

        fetch('/start_assistant', { method: 'POST' })
            .then(response => response.text())
            .then(message => {
                outputDiv.innerHTML = message;
            })
            .catch(error => {
                console.error('Error:', error);
                outputDiv.innerHTML = 'Error starting assistant. Please try again.';
            });
    });
});
