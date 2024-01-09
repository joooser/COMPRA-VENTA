$(document).ready(function () {
    // Assume we have a JSON object with questions and answers
    var answers = {};

    // Function to update placeholders with answers
    function updatePlaceholders() {
    $('[data-placeholder]').each(function() {
            var questionId = $(this).data('placeholder');
            if (answers[questionId]) {
                $(this).text(answers[questionId]);
            } else {
                $(this).text('________');
            }
        });
    }

    // Event listener for input changes
    $(document).on('input', 'input', function() {
        var questionId = $(this).attr('name').split('_')[1];
        var answer = $(this).val();
        answers[questionId] = answer;
        updatePlaceholders();
    });

    // Load questions and create input fields
    // This should be done by retrieving questions from the database
    var questions = [
        { id: 1, text: 'Cual es el nombre del vendedor?' },
        // ... other questions
    ];

    // Create input fields for each question
    questions.forEach(function(question) {
        var input = $('<input>').attr('data-question-id', question.id);
        $('body').append(input); // Append input to the body or a specific form
    });

    // Initialize placeholders
    updatePlaceholders();

  // No need to create input fields manually as they are already created in the HTML
  // So the following code is not needed:
  // var questions = [{ id: 1, text: 'Cual es el nombre del vendedor?' }, ... ];
  // questions.forEach(function(question) { ... });

    // AJAX call to save the document
    // If the save-button is part of your implementation, keep this part.
    // Otherwise, you may not need this AJAX call here.
    $('#questions-form').on('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
    
        var formData = $(this).serialize(); // Serialize the form data
        
        $.ajax({
            url: '/create-document', // The route that handles the form submission
            type: 'POST',
            data: formData,
            success: function(response) {
                // Update the placeholders with the answers
                updatePlaceholders();
            },
            error: function(xhr, status, error) {
                // Handle any errors here
                console.error("Error occurred: " + error);
            }
        });
    });
});