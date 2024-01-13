$(document).ready(function () {

    // Load questions and create input fields
    // This should be done by retrieving questions from the database
    var questions = [
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
    
    // Assume we have a JSON object with questions and answers
    var answers = {};

    // Function to update placeholders with answers
    function updatePlaceholders() {
        $('[data-placeholder]').each(function() {

            var questionId = $(this).data('placeholder');
            var question = questions.find(q => q.id == questionId);

            if (question) {

                var questionText = question.text;

                if (answers[questionId]) {

                    $(this).text(answers[questionId].toUpperCase()); // Convert text to uppercase
                    $(this).addClass('text-uppercase fw-bold'); // Add Bootstrap classes for styling

                } else {

                    $(this).text(questionText.toUpperCase()); // Display the question text in uppercase when the answer is empty
                    $(this).addClass('text-uppercase fw-bold'); // Add Bootstrap classes for styling

                }
            } else {
                console.error('Question not found for questionId:', questionId); // Error if question not found           
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

    updatePlaceholders();

    window.final_preview_document = function() {
        return $('#document-template').html();
    };
});