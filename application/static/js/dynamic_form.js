$(document).ready(function() {
  var animating;

  // Animation speeds
  var animationSpeeds = {
    fadeOut: 900, // Speed of the fadeOut animation
    fadeIn: 900   // Speed of the fadeIn animation
  };

  $(".next").click(function() {
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    // Activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

    // Show the next fieldset
    next_fs.show(); 

    // Hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
      step: function(now, mx) {
        // As the opacity of current_fs reduces to 0 - stored in "now"
        // 1. Scale current_fs down to 80%
        scale = 1 - (1 - now) * 0.2;
        // 2. Bring next_fs from the right(50%)
        left = (now * 50)+"%";
        // 3. Increase opacity of next_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
        next_fs.css({'left': left, 'opacity': opacity});
      }, 
      duration: animationSpeeds.fadeOut, 
      complete: function(){
        current_fs.hide();
        animating = false;
        // Reset previously set styles
        next_fs.css({'left': '0', 'position': 'relative'});
      }, 
      // This easing is optional and can be removed if not desired
      easing: 'easeInOutBack'
    });
  });

  $(".previous").click(function() {
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    // De-activate current step on progressbar
    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

    // Show the previous fieldset
    previous_fs.css({
      'position': 'absolute',
      'opacity': 0,
      'left': '50%',
      'transform': 'scale(0.8)'
    }).show();

    // Hide the current fieldset with style
    current_fs.animate({ opacity: 0 }, {
      step: function(now, mx) {
        // As the opacity of current_fs reduces to 0 - stored in "now"
        // 1. Scale previous_fs from 80% to 100%
        scale = 0.8 + (1 - now) * 0.2;
        // 2. Take current_fs to the right(50%) - from 0%
        left = ((1-now) * 50)+"%";
        // 3. Increase opacity of previous_fs to 1 as it moves in
        opacity = 1 - now;
        current_fs.css({'left': left});
        previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity, 'left': '0'});
      }, 
      duration: animationSpeeds.fadeIn, 
      complete: function(){
        current_fs.hide();
        animating = false;
        // Reset previously set styles
        previous_fs.css({
        'position': 'relative',
        'opacity': 1,
        'left': '',
        'transform': 'scale(1)'
      });
      animating = false;
      },
      //easeInOutBack can be used if you have included jQuery UI for a smoother effect
      easing: 'easeInOutBack'
    });
  });
});