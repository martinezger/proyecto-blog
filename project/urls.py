"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ejemplo.views import (index, index_dos, index_tres, imc, monstrar_familiares, BuscarFamiliar)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar/<nombre>/<apellido>/', index_dos),
    path('mostrar-notas/', index_tres),
    path('imc/<int:peso>/<int:altura>', imc),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('panel-familia/', include('panel_familia.urls')),
    path('', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
