from django.shortcuts import render
from .notification import InputForm

def notification_view(request):
    context ={}
    context['form'] = InputForm()
    return render(request, "home.html", context)