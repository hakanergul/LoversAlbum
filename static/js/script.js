$(document).ready(function() {
  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay: true,
    autoplayTimeout: 1000,
    autoplayHoverPause: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 2,
        nav: true
      },
      600: {
        items: 4,
        nav: false
      },
      1000: {
        items: 6,
        nav: true,
        loop: false
      }
    }
  });

  var waterfall = new Waterfall({
    containerSelector: ".wf-container",
    boxSelector: ".wf-box",
    minBoxWidth: 200
  });

  $(document).on("scroll", onScroll);
  //smoothscroll
  $('.navbar-nav li a[href^="#"]').on("click", function(e) {
    e.preventDefault();
    $(document).off("scroll");
    $(".navbar-nav li a").each(function() {
      $(this).removeClass("active");
    });
    $(this).addClass("active");
    var target = this.hash,
      menu = target;
    target = $(target);
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: target.offset().top + 2
        },
        1000,
        "swing",
        function() {
          window.location.hash = target;
          $(document).on("scroll", onScroll);
        }
      );
  });
});

function onScroll(event) {
  var scrollPos = $(document).scrollTop();
  $(".navbar-nav li a").each(function() {
    var currLink = $(this);
    var refElement = $(currLink.attr("href"));
    if (
      refElement.position().top <= scrollPos &&
      refElement.position().top + refElement.height() > scrollPos
    ) {
      $(".navbar-nav li a").removeClass("active");
      currLink.addClass("active");
    } else {
      currLink.removeClass("active");
    }
  });
}
