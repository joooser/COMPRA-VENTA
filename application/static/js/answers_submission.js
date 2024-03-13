document.addEventListener('DOMContentLoaded', initializeFormLogic);

document.body.addEventListener('htmx:afterSwap', function(event) {

  // Check if the swapped content includes the form or relevant components
  if (event.detail.target.id === 'formAndQuestions' ||
      event.detail.target.contains(document.getElementById('documentForm'))) {
    initializeFormLogic();
  }
});

function initializeFormLogic() {
  const form = document.getElementById('documentForm');
  
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

  // Collect question answers in an object
  const answers = {};
  document.querySelectorAll('[data-question-id]').forEach(input => {
    formData.append(`answer_${input.getAttribute('data-question-id')}`, input.value);
  });

  // Serialize answers object into JSON and add to formData
  formData.append('answers_json', JSON.stringify(answers));

  // Add plain text version of the document to formData
  const plainText = document.getElementById('templateDisplay') ? document.getElementById('templateDisplay').innerText : '';
  formData.append('plain_text', plainText);

  // Retrieve the template ID and other necessary information
  const templateDisplayElement = document.getElementById('templateDisplay');
  const documentTemplateId = templateDisplayElement ? templateDisplayElement.getAttribute('data-template-id') : '';
  formData.append('document_template_id', documentTemplateId);

  // Assuming you have elements for documentType and documentTypeId, modify as necessary
  const documentTypeId = templateDisplayElement ? templateDisplayElement.getAttribute('data-type-id') : '';
  formData.append('document_type_id', documentTypeId);

  // Log FormData contents for debugging
  for (let [key, value] of formData.entries()) {
    console.log(`${key}: ${value}`);
  }

  // Submit the form data to the server
  fetch('/submit_answers', {
    method: 'POST',
    body: formData,
    headers: {
      // If your server expects JSON, you'll need to handle this differently.
      // 'Content-Type': 'application/json',
      // 'Accept': 'application/json',
    },
  })
  .then(response => {
    if (!response.ok) {
      // If the server response was not ok, throw an error to be caught in the catch block
      throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data.message);
    if (data.success) {
      // Handle success, such as redirecting or opening a download link
      window.location.href = data.redirect_url;
      // If there's a URL for PDF download and the user is subscribed, initiate the download
      if (data.pdf_download_url) {
        window.open(data.pdf_download_url, '_blank');
      }
    } else {
      // Handle failure based on server's response message
      alert(data.message || 'An error occurred while submitting your answers.');
    }
  })
  .catch(error => {
    // Handle any errors that occurred during fetch
    console.error('Submission failed', error);
    alert(`Failed to submit: ${error.message}`);
  });
}