jQuery( document ).ready(function( $ ) {

    "use strict";

    $(function() {
        // Initialize tabs with enhanced animations
        $("#tabs").tabs({
            show: { 
                effect: "fadeIn",
                duration: 400,
                easing: "easeOutCubic"
            },
            hide: { 
                effect: "fadeOut",
                duration: 300,
                easing: "easeInCubic"
            },
            activate: function(event, ui) {
                // Add slide effect to content
                ui.newPanel.css('opacity', 0)
                    .animate({ opacity: 1 }, 400, 'easeOutCubic');
                
                // Scroll image effect
                ui.newPanel.find('img').css({
                    transform: 'translateY(20px)',
                    opacity: 0
                }).animate({
                    transform: 'translateY(0)',
                    opacity: 1
                }, 600, 'easeOutCubic');
            }
        });
    });    // Page loading animation
    $("#preloader").animate({
        'opacity': '0'
    }, 600, function(){
        setTimeout(function(){
            $("#preloader").css("visibility", "hidden").fadeOut();
        }, 300);
    });
    
    // Simplified header state management
    function updateHeader() {
        var header = $('header');
        var scroll = $(window).scrollTop();
        var isHomePage = $('body').hasClass('home');

        if (isHomePage) {
            // On the homepage, the header becomes solid after scrolling past a certain point
            if (scroll > 50) {
                header.addClass('background-header');
            } else {
                header.removeClass('background-header');
            }
        } else {
            // On all other pages, the header is always solid
            header.addClass('background-header');
        }
    }

    // Set header state on page load and on scroll/resize
    $(window).on('scroll resize', function() {
        updateHeader();
    });

    // Set initial state on page load
    updateHeader();
    

    if ($('.owl-testimonials').length) {
        $('.owl-testimonials').owlCarousel({
            loop: true,
            nav: false,
            dots: true,
            items: 1,
            margin: 30,
            autoplay: false,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 2,
                    margin: 20
                },
                992: {
                    items: 2,
                    margin: 30
                }
            }
        });
    }
    if ($('.owl-partners').length) {
        $('.owl-partners').owlCarousel({
            loop: true,
            nav: false,
            dots: true,
            items: 1,
            margin: 30,
            autoplay: false,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 2,
                    margin: 20
                },
                992: {
                    items: 4,
                    margin: 30
                }
            }
        });
    }

    $(".Modern-Slider").slick({
        autoplay:true,
        autoplaySpeed:10000,
        speed:600,
        slidesToShow:1,
        slidesToScroll:1,
        pauseOnHover:false,
        dots:true,
        pauseOnDotsHover:true,
        cssEase:'linear',
       // fade:true,
        draggable:false,
        prevArrow:'<button class="PrevArrow"></button>',
        nextArrow:'<button class="NextArrow"></button>', 
    });

    function visible(partial) {
        var $t = partial,
            $w = jQuery(window),
            viewTop = $w.scrollTop(),
            viewBottom = viewTop + $w.height(),
            _top = $t.offset().top,
            _bottom = _top + $t.height(),
            compareTop = partial === true ? _bottom : _top,
            compareBottom = partial === true ? _top : _bottom;

        return ((compareBottom <= viewBottom) && (compareTop >= viewTop) && $t.is(':visible'));

    }

    $(window).scroll(function(){

      if(visible($('.count-digit')))
        {
          if($('.count-digit').hasClass('counter-loaded')) return;
          $('.count-digit').addClass('counter-loaded');
          
    $('.count-digit').each(function () {
      var $this = $(this);
      var text = $this.text();
      var isPercentage = text.indexOf('%') > -1;
      var number = parseFloat(text.replace(/[^0-9.-]/g, ''));
      
      jQuery({ Counter: 0 }).animate({ Counter: number }, {
        duration: 3000,
        easing: 'swing',
        step: function () {
          var value = Math.ceil(this.Counter);
          $this.text(isPercentage ? value + '%' : value);
        }
      });
    });
    }
})

});
