"""commshop URL Configuration

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
from django.contrib import admin
from django.urls import path

from shopcontrol.views import main_page
from deals.views import DealsListView, DealsDetailView
from products.views import ProductsListView, ProductsDetailView


urlpatterns = [
    path('', main_page),
    path('deals/', DealsListView.as_view(), name='deals'),
    path('deals/<int:pk>', DealsDetailView.as_view(), name='deal'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/<int:pk>', ProductsDetailView.as_view(), name='product'),
    path("admin/", admin.site.urls),
]
