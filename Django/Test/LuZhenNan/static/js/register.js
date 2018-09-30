$(function(){
    flag1 = false;
    flag2 = false;
    flag3 = false;
    flag4 = false;
    $('#phone').change(function () {
        let value = $(this).val();
        if(/^1(([3578]\d)|(47))\d{8}$/.test(value)){

                    $('#phone-tip').html('');
                     flag1 = true}

        else{
            $('#phone-tip').html('请输入正确的手机号').css('color', 'red');
            flag1 = false}

    })

    $('#pswd').change(function () {
        let value = $(this).val();
        if(/^.{4,20}$/.test(value)){
            $('#passwd-tip').html('');
            flag2 = true
        }
        else{
            $('#passwd-tip').html('请输入4到20位的密码').css('color', 'red');
            flag2 = false
        }
    })

    $('#pswd-exam').change(function () {
        let value = $(this).val();
        if(value == $('#pswd').val()){
            $('#passwd_exam-tip').html('');
            flag3 = true
        }
        else{
            $('#passwd_exam-tip').html('两次密码不一致').css('color','red')
            flag3 = false
        }
    })

    $('#email1').change(function () {
        let value = $(this).val();
        if (/^\w+@\w+(\.\w+)+$/.test(value)){
            $('#email-tip').html('');
            flag4 = true
        }
        else{
            $('#email-tip').html('邮箱不合法').css('color','red');
            flag4 = false
        }
    })

    $('#btn').click(function () {
        console.log(flag1)
        console.log(flag2)
        console.log(flag3)
        console.log(flag4)
        if(flag4&&flag2&&flag3&&flag1){
            $('#pswd-exam').val(md5($('#pswd-exam').val()))
        }
        else{
            return false
        }
    })
	
});
