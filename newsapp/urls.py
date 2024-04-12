from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path('registration/', views.registration, name='registration'),  # Make sure to update this line with the correct view function
    path('login-page/', views.login, name='login'),  # Make sure to update this line with the correct view function
    path('result/', views.result, name='result'),

   
]
