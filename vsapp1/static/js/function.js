function fnMove(){
    var offset = $(this).next().offset();
    $('html, body').animate({scrollTop : offset.top}, 400);
}