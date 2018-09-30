$(function () {
    $('.pay').click(function () {
        var li = $(this).parent();
        orderid = $(this).attr('orderid');
        var f = confirm('您确定要收货吗');
        if (f){
        $.post('/axf/orderconfirm/',{'orderid': orderid}, function (data) {
            if (data.status){
                li.remove()
            }
            else{(data.status == 0)

                console.log(data.msg)
            }
        })
            }
    })
})