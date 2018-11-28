$(function () {
    flag1 = false;
    flag2 = false;
    flag3 = false;
    flag4 = false;

    $('#phone').change(function () {
        value = $("#phone").val();
        if(/^1(([3578]\d)|(47))\d{8}$/.test(value)){
            $.post('/phoneajax/', {'phone': value}, function (data) {
                if(data.status == '1'){
                    $('#phone-tip').html('')
                    flag1 = true
                }
                else{
                    $('#phone-tip').html('该手机号已经存在').css('color', 'green')
                }
            })
        }
        else{
            $('#phone-tip').html('手机号码格式不正确').css('color', 'red')
        }
    });


  $('#user').change(function () {
      value = $('#user').val();
      if (/^.{4,}$/.test(value)){
          $('#user-tip').html('')
          flag2 = true
      }
      else {
          $('#user-tip').html('账号必须大于４位数').css('color', 'red')
      }
  });


   $('#password1').change(function () {
       value = $('#password1').val();
       if (/^.{4,}$/.test(value)){
          $('#password1-tip').html('');
            flag3 = true
      }
      else {
          $('#password1-tip').html('密码必须大于４位数').css('color', 'red')
      }
   });

   $('#password2').blur(function () {
       value1 = $('#password1').val();
       value2 = $('#password2').val();
       if (value1 == value2){
          $('#password2-tip').html('');
            flag4 = true
      }
      else {
          $('#password2-tip').html('两个密码不一致').css('color', 'red')
      }
   })

    $('#login').click(function () {
        if(flag1&&flag2&&flag3&&flag4){
            $('#password1').val( md5($('#password1').val()))
        }
        else{
            return false
        }
    })
});













// /^1(([3578]\d)|(47))\d{8}$/.test(value)