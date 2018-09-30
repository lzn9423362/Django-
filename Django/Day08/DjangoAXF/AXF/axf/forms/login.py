#定制表单类
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=12, min_length=6,
    required=True, error_messages={'required': '用户账号不能为空', 'invalid': '格式错误'},
    widget=forms.TextInput(attrs={'class':'form-control'}))

    passwd = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput, required=True, error_messages={'required': '密码不能为空'})











