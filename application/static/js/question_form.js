// Function to render the questions
function renderQuestions(title, questions) {
  // Set the title of the document
  document.title = title;

  // Create a form element
  const form = document.createElement('form');

  // Iterate over the questions
  questions.forEach((question) => {
    // Create a div for each question
    const questionDiv = document.createElement('div');

    // Create a label for the question
    const questionLabel = document.createElement('label');
    questionLabel.textContent = question.text;

    // Create an input field for the answer
    const answerInput = document.createElement('input');
    answerInput.type = 'text';
    answerInput.name = question.id;

    // Append the label and input to the question div
    questionDiv.appendChild(questionLabel);
    questionDiv.appendChild(answerInput);

    // Append the question div to the form
    form.appendChild(questionDiv);
  });

  // Create a submit button
  const submitButton = document.createElement('button');
  submitButton.type = 'submit';
  submitButton.textContent = 'Submit';

  // Add an event listener to the form submit event
  form.addEventListener('submit', (event) => {
    event.preventDefault();

    // Create an object to store the answers
    const answers = {};

    // Iterate over the form elements
    for (const element of form.elements) {
      if (element.name) {
        answers[element.name] = element.value;
      }
    }

    // Send the answers to the backend
    // Replace the URL with your backend endpoint
    fetch('/backend/endpoint', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(answers),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the backend
        console.log(data);
      })
      .catch((error) => {
        // Handle any errors
        console.error(error);
      });
  });

  // Append the form and submit button to the document body
  document.body.appendChild(form);
  document.body.appendChild(submitButton);
}

// Usage example
const title = 'Question Form';
const questions = [
  { id: 1, text: 'Cual es el nombre del vendedor?' },
  { id: 2, text: 'Cual es la nacionalidad del vendedor?' },
  { id: 3, text: 'Cual es la cedula del vendedor?' },
  { id: 4, text: 'Cual es el estado civil del vendedor?' },
  { id: 5, text: 'Cual es el domicilio del vendedor?' },
  { id: 6, text: 'El vehiculo me pertenece en virtud de que documento?' },
  { id: 7, text: 'Cual es el numero del titulo del vehiculo?' },
  { id: 8, text: 'Cual es el numero de forma titulo del vehiculo?' },
  { id: 9, text: 'De que fecha es el titulo?' },
  { id: 10, text: 'Que notaria autentico el documento?' },
  { id: 11, text: 'Bajo que numero quedo autenticado el documento?' },
  { id: 12, text: 'Bajo que tomo quedo autenticado el documento?' },
  { id: 13, text: 'En que fecha fue autenticado el documento?' },
  { id: 14, text: 'Cual es el nombre del conyuge del vendedor?' },
  { id: 15, text: 'Cual es la nacionalidad del conyuge del vendedor?' },
  { id: 16, text: 'Cual es la cedula del conyuge del vendedor?' },
  { id: 17, text: 'Cual es el domicilio conyuge del vendedor?' },
  { id: 18, text: 'Cual es el nombre del comprador?' },
  { id: 19, text: 'Cual es la nacionalidad del comprador?' },
  { id: 20, text: 'Cual es la cedula del comprador?' },
  { id: 21, text: 'Cual es el estado civil del comprador?' },
  { id: 22, text: 'Cual es el domicilio del comprador?' },
  { id: 23, text: 'Cual es la marca del vehiculo?' },
  { id: 24, text: 'Cual es el modelo del vehiculo?' },
  { id: 25, text: 'Cual es la placa del vehiculo?' },
  { id: 26, text: 'Cual es el serial motor del vehiculo?' },
  { id: 27, text: 'Cual es el serial de caroceria del vehiculo?' },
  { id: 28, text: 'Cual es el año del vehiculo?' },
  { id: 29, text: 'Cual es el tipo del vehiculo?' },
  { id: 30, text: 'Cual es el color del vehiculo?' },
  { id: 31, text: 'Cual es la clase del vehiculo?' },
  { id: 32, text: 'Cual es el uso del vehiculo?' },
  { id: 33, text: 'Cual es el precio del vehiculo?' },
  { id: 34, text: 'En que moneda se hizo el pago el vehiculo?' },
  { id: 35, text: 'Con que instrumento se pago el vehiculo?' }
];

renderQuestions(title, questions);