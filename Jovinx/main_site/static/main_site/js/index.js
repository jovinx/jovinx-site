$(document).ready(function() {

    //why jovinx slide

    //service slide

    //client slide
    $('#client-slide').owlCarousel({
        items: 7,
        autoPlay: true,
        stopOnHover: true,
        itemsDesktop: false,
        itemsDesktopSmall: [1200, 5],
        itemsTablet: [800, 4],
        itemsTabletSmall: false,
        itemsMobile: [500, 3],
        slideSpeed: 100,
        responsiveRefreshRate: 50
    })
    //testimony slide
    $('#testimony-slide').owlCarousel({
        singleItem : true,
        autoPlay: true,
        stopOnHover: true,
        responsiveRefreshRate: 50,
        pagination: true      
    })
    

    //sliders controls
    $('.slide-wrapper .slide-navs i.fa-arrow-left').click(function() {
        $(this).parent().prev().trigger('owl.prev');
    })

    $('.slide-wrapper .slide-navs i.fa-arrow-right').click(function() {
        $(this).parent().prev().trigger('owl.next');
    })

    $('#services #service-slide .item .btn-container button').click(function() {
        var title = $(this).data('title');
        var description = $(this).data('info');
        var icon = $(this).data('icon');
        var image_url = $(this).data('img-url');
        var sub_services = $(this).data('subservices');



        $('.modal .modal-header h4').html('<i class="fa '+icon+' fa-fw"></i>'+title);
        $('.modal .modal-body img').attr('src', '/uploads/'+image_url);
        $('.modal .modal-body .caption p').text(description)

        sub_services = sub_services.split(",");
        var html_list = '';
        
        for(item of sub_services) {
            var regex = /[\[\]\'\']+/g
            item = item.replace(regex, "")
            html_list += '<li><i class="fa '+ icon +'"></i>'+item+'</li>'   
        }
        $('.modal .modal-body ul').html(html_list);

        

    })

    $('#our_works ul li.thumbnail .caption a').click(function() {
        var image = $(this).data('img-url');
        var category = $(this).data('category');

        $('#our_works_modal .modal-content .modal-body img').attr('src', '/uploads/'+image);
        $('#our_works_modal .modal-content .modal-header h4').html('<i class="fa fa-paint-brush fa-fw" ></i> '+category);
    })
})