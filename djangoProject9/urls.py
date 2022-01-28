"""djangoProject9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from portfolio.views import BaseView, QueryView, QueryListView, ResponseView, SuccessMessage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='BaseView'),
    path('QueryView/', QueryView.as_view(), name='QueryView'),
    path('QueryListView/', QueryListView.as_view(), name='QueryListView'),
    path('ResponseView/<int:pk>/', ResponseView.as_view(), name='ResponseView'),
    path('SuccessMessage/', SuccessMessage.as_view(), name='SuccessMessage'),
]
