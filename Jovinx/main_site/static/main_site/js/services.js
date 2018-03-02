$(document).ready(function () {
    $('#service-list .container .row .thumbnail .btn-container button').click(function() {
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
});