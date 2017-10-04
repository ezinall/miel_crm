$(document).ready(function(){
    $('nav ul li a').click(function(event){
        //remove all pre-existing active classes
        $('nav ul li a.active').removeClass('active');

        //add the active class to the link we clicked
        $(this).addClass('active');

        //Load the content
        //e.g.
        //load the page that the link was pointing to
        $('#content').load($(this).find('a').attr('href'));

        event.preventDefault();
    });
});