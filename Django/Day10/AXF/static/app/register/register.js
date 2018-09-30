// $(document).ready(function () {
//     var account = document.getElementById('account')
//     var accounterr = document.getElementById('accounterr')
//     var checkerr = document.getElementById('checkerr')
//     var passerr = document.getElementById('passerr')
//     var pass = document.getElementById('pass')
//     var passwd = document.getElementById('passwd')
//     var success = document.getElementById('success')
//     account.addEventListener('click', function () {
//         accounterr.style.display = 'none'
//         checkerr.style.display = 'none'
//         success.style.display = 'none'
//     }, false)
//
//     account.addEventListener('blur', function () {
//         var valuelen = this.value
//         if (valuelen.length < 6 || valuelen.length >12){
//             accounterr.style.display = 'block'
//         }
//         else{
//         $.post('/axf/checkuserid/',{'userid': valuelen}, function (data) {
//             if (data.statu == "error"){
//                 checkerr.style.display = 'block'
//             }
//
//             else{
//                 success.style.display = 'block's
//             }
//         }) }
//     }, false)
// })


$(function () {
    flag1 = false;
    flag2 = false;
    flag3 = false;
    flag4 = false;

    $('#account').change(function () {
        var valuelen = $('#account').val();
        if (/^[a-zA-Z_]\w{5,17}$/.test(valuelen)) {
            $.post('/axf/checkuserid/', {'userid': valuelen}, function (data) {
                if (data.statu == 'error') {
                    $('#msg').html('用户已经存在').css('color', 'red');
                    flag1 = false
                }

                else {
                    flag1 = true;
                    $('#msg').html('用户名可以使用').css('color', 'green')
                }
            })
        }
        else {
            flag1 = false;
            $('#msg').html('用户名格式不正确').css('color', 'red')

        }
    })

    $('#pass').change(function () {
        var pass = $("#pass").val();
        if (pass.length < 8) {
            flag2 = false;
            $('#passwdmsg').html('密码长度需要8位数以上').css('color', 'red').show()
        }
        else {
            flag2 = true;
            $('#passwdmsg').hide()

        }
    });

    $('#passwd').change(function () {
        var passwd = $('#passwd').val();
        var pass = $("#pass").val();
        if (pass != passwd) {
            flag3 = false;
            $('#pswdmsg').html('两次密码不相同').css('color', 'red').show()
        }
        else {
            flag3 = true;
            $('#pswdmsg').hide()

        }
    })

    $('#email').change(function () {
        var email = $('#email').val();
        if (/^\w+@\w+(\.\w+)+$/.test(email)) {
            flag4 = true
                $('#emailmsg').hide()
        }
        else {
            flag4 = false;
            $('#emailmsg').html('邮箱格式不正确').css('color', 'red').show()
        }
    })

    // $('#register').click(function () {
    //     // if (flag3 && flag2 && flag1 && flag4){
    //
    //     }
    //     // else{
    //         // return false
    //     // }
    // })


})

