$(document).ready(function () {
    
    // Function to update the placeholders in the preview
    function updatePreviewFromInput(input) {
        var inputName = input.attr('name');
        var questionNumber = inputName.split('_')[1];
        var placeholder = $('[data-placeholder="' + questionNumber + '"]');
        var inputValue = input.val();

        if (inputValue) {
            placeholder.text(inputValue.toUpperCase());
        } else {
            // If no input value, use the placeholder attribute from the input field
            placeholder.text(input.attr('placeholder').toUpperCase());
        }
        placeholder.addClass('text-uppercase fw-bold');
    }

    // Attach an event handler to all inputs and selects for any changes
    $('input, select').on('input change', function() {
        updatePreviewFromInput($(this));
    });

    // Initial update of placeholders based on the current input values or their placeholders
    $('input, select').each(function() {
        updatePreviewFromInput($(this));
    });

    // Function to return final preview HTML content
    window.final_preview_document = function() {
        return $('#document-template').html();
    };
});