import django.urls
from django.urls import path, include
# Importe le fichier views depuis le dossier courant
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/register/', views.register, name='register'),

]