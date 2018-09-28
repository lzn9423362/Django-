$(function () {
    $('.pay').click(function () {
        let that = this;
        orderid = $(this).attr('orderid');
        var f = confirm('您确定要支付吗');
        if (f){
        $.post('/axf/ordernopayhandle/', {'orderid': orderid}, function (data) {
            if (data.status){
                $(that).parent().remove()
            }
        })
            }
    })
})