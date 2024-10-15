from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_home),
    path('post', views.api_post),
    path('products/', include('products.urls')),
]