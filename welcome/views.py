import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())




def get(request):
    if not os.path.exists('get.txt'):
        with open('get.txt', 'w'):
            pass
    with open('get.txt', 'a') as f:
        d = dict(request.GET.items())
        f.write(str(d))
        f.write('\n')

def get_log(request):
    with open('get.txt') as f:
        return HttpResponse(f.read())
