//$('#myForm').submit();
//$.post('/', $('#myForm').serialize());
/*
$(document).on('submit','#myForm',function() {
    $.post('/', $('#myForm').serialize());
    return false;
   });
   */

$(document).on('submit','#myForm',function() {
   $.post('/', $('#myForm').serialize()), function(result) {
    console.log(result);
   }
});