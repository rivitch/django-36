from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("ВЫ НАХОДИТЕСЬ НА ГЛАВНОЙ СТРАНИЦЕ")
def about(request):
    return HttpResponse("ЕЩЕ ОДНА СТРАНИЦА")