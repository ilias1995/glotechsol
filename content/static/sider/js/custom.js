
 jQuery(document).ready(function(){

  // slick slider call 
    $('.slick_slider').slick({
      dots: true,
      infinite: true,      
      speed: 2200,      
      slidesToShow: 1,
      slide: 'div',
      autoplay: true,
      autoplaySpeed: 7000,
      cssEase: 'linear'
    });  

    // latest post slider call 
    $('.latest_postnav').newsTicker({
    row_height: 90,
    speed: 2000,
    duration: 7000,
    prevButton:  $('#prev-button'),
    nextButton:  $('#next-button')   
});



});



  
