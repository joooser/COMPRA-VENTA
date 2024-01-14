$(document).ready(function() {

    $('#multistepsform').on('submit', function(e) {

        e.preventDefault();
        var formData = {};

        $('#multistepsform').find('input[type="text"]').each(function() {

          var id = $(this).attr('id').split('_')[1];
          formData[id] = $(this).val();
        });
      
        var documentText = $('#document-template').text();
        var documentTitle = $('#document-title').val();
      
        var dataToSend = {
          formData: formData,
          documentText: documentText,
          documentTitle: documentTitle
        };

        //console.log(dataToSend);
        //console.log(documentTitle);

        $.ajax({

            url: '/handle_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(dataToSend),

            success: function(response) {

              alert('Documento enviado con éxito');
            },
            error: function(xhr, status, error) {

              alert('Ocurrió un error al enviar el formulario');
            }
        });
    });
});