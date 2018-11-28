$(function () {
    flag1 = false;
    flag2 = false;
    flag3 = false;
    $('#user').blur(function () {
        user =  $('#user').val();
        if(/^.{4,}$/.test(user)){
            $.post(/registerajax/, {'user': user}, function (data) {
                if(data.status == '2'){
                    $('#user-tip').html('用户已存在').css('color', 'green')
                }

                else if(data.status == '1'){
                    $('#user-tip').html('');
                    flag1 = true;
                }
                else{
                    $('#user-tip').html('请求方式错误').css('color', 'red')
                }

            });
        }
        else{
            $('#user-tip').html('账号格式不正确').css('color', 'red')
        }
    })

    $('#password').blur(function () {
        password = $('#password').val();
        if (/^.{4,}/.test(password))
        {
            $('#password-tip').html('');
            flag2 = true;
        }
        else{
            $('#password-tip').html('密码格式不正确').css('color', 'red')
        }
            });

    $('#email').blur(function () {
        email = $('#email').val();
        if (/^\w+@\w+(\.\w+)+$/.test(email)){
            $('#email-tip').html('');
            flag3 = true;
        }
        else
        {
$('#email-tip').html('邮箱格式错误').css('color','red')
        }
    });

    $('#login').click(function () {
        if(flag2&&flag1&&flag3){
           $('#password').val(md5($('#password').val()));
        }
        else{
            return false;
        }
    })

});