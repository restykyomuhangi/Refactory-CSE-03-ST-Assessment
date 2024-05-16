from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrationform, name='registrationpage'), 
]