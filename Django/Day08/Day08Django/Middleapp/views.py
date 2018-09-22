import random

from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image, ImageFont, ImageDraw
# Create your views here.

import os
import io

from Day08Django.settings import BASE_DIR



def index(request):
    # print('视图函数中的index函数')
    # return HttpResponse('hello middleware')
    # print(id(request))
    # print(request.)
    # print(request.hello)
    # return HttpResponse('嘎嘎')
    # print(1/0)
    if request.method == 'POST':
        if random.random() > 0.9:

            return HttpResponse('恭喜您成功获得价值9999的大保健')
        else:
            return HttpResponse('请充值')
    return render(request, 'middleapp/index.html')



def login(request):
    if request.method == 'POST':
        #检测验证码是否合法
        verify = request.POST.get('verify')
        verify_code = request.session.get('verify_code') #服务器生成的验证码
        if verify.upper() == verify_code.upper():
            return HttpResponse('验证成功')
        else:
            return HttpResponse('验证失败')
    else:
        return render(request, 'middleapp/login.html')







def generater_verify(request):
    #画布
    size = (100,50)
    bgcolor = (200,100,3)
    image = Image.new('RGB',size,bgcolor)

    #画笔
    draw = ImageDraw.Draw(image,'RGB')


    #字体样式
    path = os.path.join(BASE_DIR,r'static/fonts/ADOBEARABIC-BOLD.OTF')
    font = ImageFont.truetype(path,36)

    #画文本
    string = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    verify_code = ""
    for i in range(4):
        ch = string[random.randrange(len(string))]
        verify_code += ch
        draw.text((10+i*20,random.randrange(5,15)),ch,font=font)

    # print("生成的验证码是：",verify_code)
    #保存验证码
    request.session['verify_code'] = verify_code

    #干扰点
    for i in range(1000):
        draw.point((random.randint(0,98),random.randint(0, 50)),fill=random_color())

    #转换陈图片显示
    buff = io.BytesIO()   #创建一个二进制缓冲区
    image.save(buff,'png')  #将画布以图片形式存入缓冲区
    return HttpResponse(buff.getvalue(),"image/png")   #将缓冲区图片以png格式显示

def random_color():
    return random.randint(0,255), random.randint(0,255), random.randint(0,255)

