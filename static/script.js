$(document).ready(function() {
  var waterfall = new Waterfall({
    containerSelector: ".wf-container",
    boxSelector: ".wf-box",
    minBoxWidth: 250
  });

  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
        nav: true
      },
      600: {
        items: 3,
        nav: false
      },
      1000: {
        items: 5,
        nav: true,
        loop: false
      }
    }
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
