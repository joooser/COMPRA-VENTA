document.body.addEventListener('htmx:load', function() {
  // Select all question elements
  let questions = document.querySelectorAll('.question');
  let currentQuestionIndex = 0;

  // Function to show the current question
  function showQuestion(index) {
    questions.forEach((question, i) => {
      question.style.display = i === index ? 'block' : 'none';
    });
    updateNavigationButtons(index);
  }

  // Function to create navigation buttons with Bootstrap classes
  function updateNavigationButtons(index) {
    // Clear existing buttons
    document.querySelectorAll('.navigation-button').forEach(button => button.remove());

    // Previous button if not the first question
    if (index > 0) {
      let prevButton = document.createElement('button');
      prevButton.innerText = 'Anterior';
      prevButton.className = 'btn btn-secondary navigation-button me-2'; // Bootstrap classes added here
      prevButton.addEventListener('click', function() {
        currentQuestionIndex--;
        showQuestion(currentQuestionIndex);
      });
      questions[index].appendChild(prevButton);
    }

    // Next or submit button
    let nextButton = document.createElement('button');
    nextButton.className = 'btn btn-primary navigation-button ms-2'; // Bootstrap classes added here
    if (index === questions.length - 1) {
      nextButton.innerText = 'Submit';
      nextButton.addEventListener('click', function() {
        // Form submission logic here
      });
    } else {
      nextButton.innerText = 'Siguiente';
      nextButton.addEventListener('click', function() {
        currentQuestionIndex++;
        showQuestion(currentQuestionIndex);
      });
    }
    questions[index].appendChild(nextButton);
  }

  // Initial call to show the first question
  showQuestion(currentQuestionIndex);
});
