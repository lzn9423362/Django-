$(function () {
    $('#pay').click(function () {
        id = $(this).attr('orderid');
        $.post('/axf/pay/', {'id': id}, function (data) {
            if (data.status){
                location.href = '/axf/mine/'
            }
        })
    })
})