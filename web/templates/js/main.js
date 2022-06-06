const swiper = new Swiper(".swiper", {
    direction: "horizontal",
    loop: true,

    // Navigation arrows
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
    },

    // If we need pagination
    pagination: {
        el: ".swiper-pagination"
    },

    // And if we need scrollbar
    scrollbar: {
        el: ".swiper-scrollbar"
    }
});