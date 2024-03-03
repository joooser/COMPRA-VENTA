document.addEventListener('DOMContentLoaded', function() {

  let questions = document.querySelectorAll('.question');
  let currentQuestionIndex = 0;

  function showQuestion(index) {

    questions.forEach((question, i) => {

      if (i === index) {
        question.style.display = 'block';
        question.classList.remove('d-none');
        question.classList.add('d-block');
      } else {
        question.style.display = 'none';
        question.classList.add('d-none');
        question.classList.remove('d-block');
      }
    });

    updateNavigationButtons(index);
  }

  function updateNavigationButtons(index) {

    document.querySelectorAll('.navigation-button').forEach(button => button.remove());


    if (index > 0) {

      let prevButton = document.createElement('button');
      prevButton.innerText = 'Anterior';
      prevButton.className = 'btn btn-secondary navigation-button me-2';
      prevButton.addEventListener('click', function() {
        currentQuestionIndex--;
        showQuestion(currentQuestionIndex);
      });
      questions[index].appendChild(prevButton);
    }
  
    let nextButton = document.createElement('button');
    nextButton.className = 'btn btn-primary navigation-button ms-2';
    if (index === questions.length - 1) {

      nextButton.innerText = 'Submit';
      nextButton.addEventListener('click', function() {

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

  document.body.addEventListener('htmx:afterSwap', function() {

    questions = document.querySelectorAll('.question');
    if(questions.length > 0) {
        showQuestion(currentQuestionIndex);
    }
  });

  if(questions.length > 0) {

    showQuestion(currentQuestionIndex);
  }
});