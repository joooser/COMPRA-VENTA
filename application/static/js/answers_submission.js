document.addEventListener('DOMContentLoaded', initializeFormLogic);

<<<<<<< Updated upstream
document.body.addEventListener('htmx:afterSwap', function(event) {

  // Check if the swapped content includes the form or relevant components
  if (event.detail.target.id === 'formAndQuestions' ||
      event.detail.target.contains(document.getElementById('documentForm'))) {
    initializeFormLogic();
=======
let dropdownSelections = {}; // Object to store selections from the first form

document.body.addEventListener('htmx:afterSwap', function(event) {
  if (event.detail.target.id === 'questionsContainer') {
    // Ensure the form event listener is attached only after the first form has been submitted
    // and the questions have been loaded.
    const questionsForm = document.getElementById('questionsContainer');
    if (questionsForm) {
      questionsForm.removeEventListener('submit', submitSecondForm); // Prevent multiple bindings
      questionsForm.addEventListener('submit', submitSecondForm);
    }
>>>>>>> Stashed changes
  }
});

function initializeFormLogic() {
  const form = document.getElementById('documentForm');
<<<<<<< Updated upstream
  
=======
>>>>>>> Stashed changes
  if (!form) {
    console.error('Form not found');
    return;
  }
  
  form.removeEventListener('submit', handleFormSubmit); // Remove existing listener to prevent duplicates
  form.addEventListener('submit', handleFormSubmit);
}

function handleFormSubmit(event) {
  event.preventDefault(); // Prevent the form from submitting traditionally
  const formData = new FormData(event.currentTarget);
  
<<<<<<< Updated upstream
  const formData = new FormData(event.currentTarget);
=======
  // Record the selections from the first form
  formData.forEach((value, key) => {
    dropdownSelections[key] = value;
  });

  console.log('Recorded selections:', dropdownSelections);
  
  // Assuming the use of HTMX for AJAX submission, let HTMX handle the form submission.
}

function submitSecondForm(event) {
  event.preventDefault(); // Prevent the form from submitting traditionally
>>>>>>> Stashed changes

  const questionsAndAnswers = {};
  document.querySelectorAll('[data-question-id]').forEach(input => {
    const questionId = input.getAttribute('data-question-id');
    const questionText = document.querySelector(`label[for="answer_${questionId}"]`)?.innerText || 'Question not found';
    questionsAndAnswers[questionId] = {
      question: questionText,
      answer: input.value
    };
  });

  const templateText = document.getElementById('templateDisplay')?.innerText || '';

  const submissionData = {
    Type: dropdownSelections,
    QA: questionsAndAnswers,
    Document: {
      template: templateText
    }
  };

  // Fetch API with error handling
  fetch('/submit_answers', {
    method: 'POST',
    body: JSON.stringify(submissionData),
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data.message);
    if (data.success) {
      window.location.href = '/home';
    } else {
      alert(data.message || 'An error occurred while submitting your answers.');
    }
  })
  .catch(error => {
    console.error('Submission failed', error);
    alert(`Failed to submit: ${error.message}`);
  });
}
