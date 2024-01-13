//$('#myForm').submit();
//$.post('/', $('#myForm').serialize());
/*
$(document).on('submit','#myForm',function() {
    $.post('/', $('#myForm').serialize());
    return false;
   });
   */
/*
$(document).on('submit','#myForm',function() {
   $.post('/', $('#myForm').serialize()), function(result) {
    console.log(result);
   }
});
*/

$(document).ready(function() {
   $('#myForm').on('submit', function(e) {
       e.preventDefault();
       $.ajax({
           type: "POST",
           url: "/test",
           data: $(this).serialize(),
           success: function(response) {
               // Handle response here
               console.log(response);
               if (response.success) {
                   alert("Form submitted successfully: " + response.message);
               }
           },
           error: function(error) {
               // Handle error here
               console.error("Error submitting form: ", error);
           }
       });
   });
});

/*
$(document).ready(function() {
   $('#myForm').on('submit', function(e) {
       var isValid = true;

       $('input[type="text"]').each(function() {
           if ($(this).val().trim() === '') {
               alert('Please fill out the ' + $(this).attr('placeholder') + ' field.');
               isValid = false;
               return false;
           }
       });

       if (!isValid) {
         alert("Form submitted successfully: " + response.message);
           e.preventDefault();
       }
   });
});
*/