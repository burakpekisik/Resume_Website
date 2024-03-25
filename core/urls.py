from django.urls import path
from .views import index, redirect_urls, contact_form

urlpatterns = [
    path('', index, name='index'),
    path('<slug>/', redirect_urls, name='redirect_urls'),
    path('contact_form', contact_form, name='contact_form'),
]
