
 jQuery(document).ready(function(){

  // slick slider call 
    $('.slick_slider').slick({
      dots: true,
      infinite: true,      
      speed: 800,      
      slidesToShow: 1,
      slide: 'div',
      autoplay: true,
      autoplaySpeed: 2000,
      cssEase: 'linear'
    });  

    // latest post slider call 
    $('.latest_postnav').newsTicker({
    row_height: 90,
    speed: 800,
    prevButton:  $('#prev-button'),
    nextButton:  $('#next-button')   
});



});



  