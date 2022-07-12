from django.shortcuts import render
from .notification import InputForm
from django.http import HttpResponse

def notification_view(request):
    context ={}
    context['form'] = InputForm()
    return render(request, "notification.html", context)

def home(request):
    return HttpResponse('Hello World')
