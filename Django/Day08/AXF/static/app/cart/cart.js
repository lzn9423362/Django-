$(function () {
    $('.add').click(function(){
        var v = $(this).prev();
        let cartid = $(this).parents('li').attr('id');
        $.post('/axf/cartnumadd/', {'cartid': cartid}, function (data) {
            if (data.status == 1){
                v.html(data.num)}
                calculate()
        })

    });

    $('.reduce').click(function(){
        var v = $(this).next();
        let cartid = $(this).parents('li').attr('id');
        $.post('/axf/cartnumreduce/', {'cartid': cartid}, function (data) {
            if (data.status == 1){
                v.html(data.num)}
            else if (data.status == 0){
                location.href = '/axf/login/'
            }
            else{
                console.log(data.msg)
            }
            calculate()
        })


    });


    $('.delbtn').click(function () {
        var li = $(this).parent();
        let cartid = $(this).parents('li').attr('id');
        f = confirm('您确定要删除吗')
        if (f) {
            $.post('/axf/cartdel/', {'cartid': cartid}, function (data) {
                if (data.status == 1) {

                    li.remove()
                }
                else if (data.status == 0) {
                    location.href = '/axf/login/'
                }
                else {
                    console.log(data.msg)
                }
                isAllSelect();

            })
        }

    });


    $('.select').click(function () {
        let cartid = $(this).parents('li').attr('id');
        var li = $(this).parents('li');
        $.post('/axf/cartselect/', {'cartid': cartid}, function (data) {
            if (data.status == 1) {
                    li.find('.select').children().html(data.select ? '√': '')
            }


            else if (data.status == 0) {
                location.href = '/axf/login/'
            }
            else {
                console.log(data.msg)
            }
            isAllSelect();
        })
    });

    $('#allselect').click(function () {
        let select = []; //保存勾选商品所在购物车的cartid
        let unSelect = []; //保存未勾选商品的所在购物车的cartid
        // 遍历购物车所有商品节点
        $('.menuList').each(function () {
            let isSelect = $(this).find('.select').children('span').html();
            if (isSelect){
                select.push($(this).attr('id'))
            }
            else{
                unSelect.push($(this).attr('id'))
            }
        });

        if (unSelect.length == 0){
            $.post('/axf/cartallselect/', function (data) {
                if(data.status == 1){
                    $('.select').find('span').html('')
                }
                else{
                console.log(data.msg)}
                isAllSelect()
            })
        }

        else  {
             $.post('/axf/cartallselect/', function (data) {
                if(data.status == 1){
                    $('.select').find('span').html('√')

                }
                else{
                console.log(data.msg)}
                isAllSelect()
            })

        }
    });

     function calculate() {

        //计算总价
        let total = 0; //总价

        $('.menuList').each(function () {
            //如果勾选了
            if ($(this).find('.select').find('span').html() == '√'){

                let price = $(this).find('.price').html();  //单价
                let num = $(this).find('.num').html();  //数量
                total += parseFloat(price) * parseInt(num);
            }
        });

        // 显示总价
        $('#totalPrice').html(total.toFixed(2));  // 保留两位小数

    }
    isAllSelect();
    function isAllSelect() {
        var s = 0;
        $('.select').each(function () {
            if ($(this).find('span').html()){
                s++
            }
        });

        if (s == $('.select').length){
            $('#allselect').find('span').html('√')
        }//打钩

        else{
            $('#allselect').find('span').html('')
        } //不打勾
        calculate();
    }



    $('#calculate').click(function () {
        num = $('#totalPrice').html()
        var f = confirm('是否确认下单')
        if(f){
        $.post('/axf/orderadd/', {'num': num}, function (data) {
            console.log(data.orderid)
            if(data.status == 1){
                window.location.href = '/axf/order/' + data.orderid + '/'
            }
        })}
    })


});