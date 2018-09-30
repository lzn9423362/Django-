$(function(){
    $('#btn').click(function () {
        username = $('#phone').val()
        password = $('#password1').val()
        console.log(password)
        if (username && password){
            $('#password1').val(md5(password))
        }
        else{
            $('#user-tip').html('用户名或密码不能为空').css('color', 'red');
            return false
        }
    })

});