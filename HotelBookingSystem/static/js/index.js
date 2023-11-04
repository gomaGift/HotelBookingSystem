
      var swiper = new Swiper(".swiper-container", {
        spaceBetween: 30,
        effect: "fade",
        loop: true,
        autoplay: {
        	delay: 3500,
        	disableOnInteraction: false,
        }
      });

      var swiper = new Swiper(".swiper-testimonials", {
        effect: "coverflow",
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: "auto",
        slidesPerView: "3",
        loop: true,
        coverflowEffect: {
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows: false,
        },
        pagination: {
          el: ".swiper-pagination",
        },
        breakpoints: {
        	320: {
        		slidesPerView: 1,
        	},
        	640: {
        		slidesPerView: 1,
        	},
        	768: {
        		slidesPerView: 2,
        	},
        	1024: {
        		slidesPerView: 3,
        	},
        }
      });
     
  
    $(document).ready(function () {
        $("#numberInput").on("input", function () {
            // Show the input field when user starts typing
            $("#numberInput").show();
            $("#numberSelect").hide();
        });

        $("#numberSelect").on("change", function () {
            // Show the select field when user selects a value
            $("#numberSelect").show();
            $("#numberInput").hide();
        });
    });