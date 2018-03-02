//service slide
$('.owl-carousel').owlCarousel({
    items: 4,
    pagination: false
})



//slider for graphics gallery



//general for all slides
$('.slide-wrapper .slide-navs i.fa-arrow-left').click(function() {
    $(this).parent().prev().trigger('owl.prev');
})

$('.slide-wrapper .slide-navs i.fa-arrow-right').click(function() {
    $(this).parent().prev().trigger('owl.next');
})