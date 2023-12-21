from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info("ВЫ НАХОДИТЕСЬ НА ГЛАВНОЙ СТРАНИЦЕ")
    return HttpResponse("ВЫ НАХОДИТЕСЬ НА ГЛАВНОЙ СТРАНИЦЕ")
def about(request):
    return HttpResponse("ЕЩЕ ОДНА СТРАНИЦА")
logger.info('Index page accessed')
    