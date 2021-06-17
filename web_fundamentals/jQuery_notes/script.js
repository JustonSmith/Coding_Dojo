// jQuery Selector Syntax

$('#fadeout').click(function(){
    $('#box1').fadeOut( 3000, function(){
        // animation complete
    });
});

$('#fadeIn').click(function(){
    $('#box1').fadeIn( 3000, function(){
        // animation complete
    });
});

$('#fadeToggle').click(function(){
    $('#box1').fadeToggle( 3000, function(){
        // animation complete
    });
});