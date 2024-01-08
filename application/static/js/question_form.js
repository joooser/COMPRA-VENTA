<script>
$(document).ready(function() {

  // Existing modal and AJAX code...

  // Add submit handler to send response
  $('#question-form').submit(function(e) {
    e.preventDefault();
    
    // Get response value
    var response = $('#response').val();
    
    // Send AJAX request to submit response
    $.ajax({
      url: '/submit-response',
      method: 'POST',
      data: {
        response: response
      },
      success: function(data) {
        // Update preview with returned text
        $('#preview-text').text(data.text);
        
        // Disable submit button
        $('#submit-response').prop('disabled', true);
      }
    });

  });

  // Real-time preview update on input event
  $('#response').on('input', function() {
    var currentResponse = $(this).val().toUpperCase();

    // Update preview paragraph with id
    $('#preview-text').text(currentResponse);
  });

  // Handle the "Create PDF" button click
  $('#create-pdf').click(function() {
    // Show the confirmation modal
    $('#confirmationModal').modal('show');
  });

  // Handle the confirmation for PDF creation
  $('#confirm-pdf').click(function() {
    // Implement the AJAX call to save the document and generate the PDF
    // ...
  });

});
</script>