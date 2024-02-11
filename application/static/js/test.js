$(document).ready(function () {
    // Initialize placeholders with their corresponding question
    function initializePlaceholders() {
        $('input, select').each(function() {
            var input = $(this);
            var inputName = input.attr('name');
            var placeholderText = input.attr('placeholder');
            var questionNumber = inputName.split('_')[1];
            var placeholder = $('[data-placeholder="' + questionNumber + '"]');
            
            // Check if the placeholder already has content (from previous input)
            if (!placeholder.text().trim()) {
                placeholder.text(placeholderText);
            }
        });
    }

    // Update placeholders based on input values
    function updatePreviewFromInput(input) {
        var inputName = input.attr('name');
        var questionNumber = inputName.split('_')[1];
        var placeholder = $('[data-placeholder="' + questionNumber + '"]');
        var inputValue = input.val();

        if (inputValue) {
            placeholder.text(inputValue.toUpperCase());
        } else {
            // Revert to showing the question if input is cleared
            placeholder.text(input.attr('placeholder').toUpperCase());
        }
    }

    // Attach event handlers to inputs and selects for any changes
    $('input, select').on('input change', function() {
        updatePreviewFromInput($(this));
    });

    // Call the initialize function when the document is ready
    initializePlaceholders();
});