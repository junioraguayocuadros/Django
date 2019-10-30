from django.http import HttpResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello, world!, Current server time is {now}'.format(now=str(now)))


def hi(request):
    return HttpResponse('Hi!')
