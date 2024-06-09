"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from airlineapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addflights', views.addflights, name='addflights'),
    path('searchflights', views.searchflights, name='searchflights'),
    path('admin/', admin.site.urls),
    path('v1/', include('gateway.urls')), # for api gateway
    path('flights/add/', views.add_flight, name='add_flight'),
    path('flights/search/', views.search_flight, name='search_flight'),
    path('flights/buy/', views.buy_ticket, name='buy_ticket'),
    path('miles/add/', views.add_miles, name='add_miles'),


]
