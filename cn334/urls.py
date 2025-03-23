"""
URL configuration for cn334 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from ecommerce import views as ecom_views
from ecommerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ecommerce/", ecom_views.ecommerce_index_view),
    path('user/<str:username>/', views.get_user, name='get_user'),
    path('product/all/', views.get_all_products, name='get_all_products'),
    path('product/byId/<int:id>/', views.get_product_by_id, name='get_product_by_id'),
    path('comment/byProductId/<int:id>/', views.get_comments_by_product, name='get_comments_by_product'),
    path('summarize/', views.summarize, name='summarize'),
]
