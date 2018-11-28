from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from App.alipay.alipay import AliPay
import json


# 首页
def index(request):
    return render(request, 'index.html')


# 支付
def pay(request):
    # 传递参数初始化支付类
    alipay = AliPay(
        appid="2016092100558964",  # 设置签约的appid
        app_notify_url="http://127.0.0.1:8000/notify/",  # "http://projectsedus.com/",  # 异步支付通知url
        app_private_key_path=r"App/alipay/ying_yong_si_yao.txt",  # 设置应用私钥
        alipay_public_key_path=r"App/alipay/zhi_fu_bao_gong_yao.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=True,  # 默认False,            # 设置是否是沙箱环境，True是沙箱环境
        return_url="http://127.0.0.1:8000/result/",  # "http://47.92.87.172:8000/"  # 同步支付通知url
    )

    # 传递参数执行支付类里的direct_pay方法，返回签名后的支付参数，
    url = alipay.direct_pay(
        subject="测试订单",  # 订单名称
        # 订单号生成，一般是当前时间(精确到秒)+用户ID+随机数
        out_trade_no="201810021221",  # 订单号
        total_amount=100,  # 支付金额
        return_url="http://127.0.0.1:8000/result/"  # 支付成功后，跳转url
    )

    # 将前面后的支付参数，拼接到支付网关
    # 注意：下面支付网关是沙箱环境，最终进行签名后组合成支付宝的url请求
    re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
    # print(re_url)
    return JsonResponse({'re_url': re_url})


# 异步支付通知url (上线后使用)
def notify(request):
    print("notify:", dict(request.GET))
    return HttpResponse("支付成功:%s" % (dict(request.GET)))


# 付款成功后跳转的url
def result(request):
    print("result:", dict(request.GET))
    return HttpResponse("支付成功:%s" % (dict(request.GET)))


#