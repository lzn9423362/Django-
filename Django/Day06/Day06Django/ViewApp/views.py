from django.http import *
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse('哈哈')
    # return JsonResponse({"name": "范冰冰"})
    return HttpResponseNotFound('Not found')