
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('ServicesADomicile.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
