from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class Mymiddle(MiddlewareMixin):
    def process_request(self,request):
        # print('中间件方法被调用')
        # print(request.path)
        # print(request.META['REMOTE_ADDR'])
        request.hello = '或许'
        # return HttpResponse('哈哈')
        ip = request.META['REMOTE_ADDR']

        #黑名单
        if ip == '127.0.0.10':
            return HttpResponse('你没有权限访问')

        #白名单
        # print('中间件', id(request))
        user = request.POST.get('user')
        if user == '习大大':
            return HttpResponse('好家伙')

    def process_exception(self,request,exception):
        print('捕获到异常')
        return redirect(reverse('Middleapp:verify'))