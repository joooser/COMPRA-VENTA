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

<script>
    // Function to update the preview text
    function updatePreview() {
      var previewElement = document.getElementById('document-preview');
      var formData = new FormData(document.getElementById('questions-form'));
      var previewText = '{{ processed_text }}'; // Get the initial processed text
  
      // Replace placeholders in the processed text with the form answers
      for (var pair of formData.entries()) {
        var key = pair[0];
        var value = pair[1];
        previewText = previewText.replace('{' + key.split('_')[1] + '}', value);
      }
  
      // Update the preview element with the new text
      previewElement.innerHTML = '<p style="font-size: 16px; color: black; text-align: justify; user-select: none;">' + previewText + '</p>';
    }
  
    // Attach the updatePreview function to the input fields
    var inputFields = document.querySelectorAll('#questions-form input[type="text"]');
    inputFields.forEach(function(input) {
      input.addEventListener('input', updatePreview);
    });
  
    // Existing form submission code...
</script>

<script>
document.getElementById('questions-form').onsubmit = function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    fetch('/create_document', {
        method: 'POST',
        body: formData
    }).then(response => response.json()).then(data => {
        if (data.success) {
            console.log('Answers submitted successfully');
            // Handle success, e.g., redirect or display a message
        } else {
            console.log('Failed to submit answers');
            // Handle failure
        }
    });
};
</script>