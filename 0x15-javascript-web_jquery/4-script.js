$(function () {
  $('DIV#toggle_header').click(function () {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red').addClass('blue');
    } else if ($('header').hasClass('green')) {
        $('header').removeClass('green').addClass('red');
    }
});
})
;
