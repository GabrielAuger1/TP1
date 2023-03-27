from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import *

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})


def service(request):
    if request.method == 'GET':
        service_page = request.GET['service']
        s = Service.objects.get(nom=service_page)
        s = ProfessionnelService.objects.get(service_id=s.pk)
    else:
        return
    return render(request, 'service.html', {'service': s})


def logout(request):
    return render(request, 'registration/logout.html')


def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

