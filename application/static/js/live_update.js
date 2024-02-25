document.addEventListener('htmx:afterSwap', function() {
    // Attach event listener to the entire document, but only handle events if they come from input fields within `questionsContainer`
    document.addEventListener('input', function(e) {
        // Check if the event target is one of our inputs
        if (e.target.matches('[data-question-id]')) {
            const questionId = e.target.getAttribute('data-question-id');
            const answer = e.target.value;

            // Find the corresponding placeholder and update its text
            const placeholders = document.querySelectorAll(`[data-placeholder="${questionId}"]`);
            placeholders.forEach(function(placeholder) {
                placeholder.textContent = answer;
            });
        }
    });
});
