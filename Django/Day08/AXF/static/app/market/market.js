// $(document).ready(function () {
//
//     var alltype = document.getElementById('all_type')
//     var showsort = document.getElementById('sort_rule')
//     var typediv = document.getElementById('typeid')
//     var sortdiv = document.getElementById('sortdiv')
//
//     typediv.style.display = 'none'
//     sortdiv.style.display = 'none'
//
//
//     alltype.addEventListener('click',function(){
//
//         typediv.style.display = 'block'
//         sortdiv.style.display = 'none'
//     },false)
//     showsort.addEventListener('click',function(){
//
//         typediv.style.display = 'none'
//         sortdiv.style.display = 'block'
//     },false)
//    typediv.addEventListener('click',function(){
//
//         typediv.style.display = 'none'
//     },false)
//     sortdiv.addEventListener('click',function(){
//
//         sortdiv.style.display = 'none'
//     },false)
//
// })
//
//


$(function () {
    $('#all_type').click(function () {
        $('#typeid').toggle()
        $('#all_type_icon').toggleClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
         $('#sortdiv').hide()
        $('#sort_rule_icon').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')

    })

    $('#typeid').click(function () {
        $('#typeid').hide()
        $('#all_type_icon').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    })

    $('#sort_rule').click(function () {
        $('#sortdiv').toggle()
        $('#sort_rule_icon').toggleClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
         $('#typeid').hide()
        $('#all_type_icon').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    })

    $('#sortdiv').click(function () {
        $('#sortdiv').hide()
        $('#sort_rule_icon').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    })

    $('.addtocart').click(function () {

        let goodid = $(this).attr('goodid');
        let num = parseInt($(this).prev().find('.num').html());
        $.post('/axf/cartaddto/', {'goodid': goodid,'num': num},function(data){
            if (data.status == 1 ){
                alert('添加成功')
            }
            else if (data.status == 0){
                 location.href = '/axf/login/';
                // location.assign('/axf/login/')
                // window.open('')
            }
        })

    })

    $('.add').click(function () {
        // let index = $(this).index('.add');
        // let num = $('.num').eq(index);
        // num.html(parseInt(num.html()) + 1)
        let num = $(this).prev();
        let goodid = $(this).parent().next().attr('goodid')

        // num.html(parseInt(num.html()) + 1)
        $.post('/axf/cartadd/', {'num':num.html(), 'goodid': goodid}, function (data) {
            if(data.status == 2){
                num.html(parseInt(num.html()) + 1)
                // 如果还有库存
            }
        } )
    })

    $('.reduce').click(function () {
        let num = $(this).next();
        if (num.html() >1) {
            num.html(parseInt(num.html()) - 1)
        }
        })
})

