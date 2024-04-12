"""
URL configuration for myproject project.

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
from django.urls import path, include
from newsapp import views as newsapp_views
from register import views as rv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', newsapp_views.index, name='index'),  # Example for the home page
    path('search/', newsapp_views.search, name='search'),
    path('cricket/', newsapp_views.cricket, name='cricket'),
    path('football/', newsapp_views.football, name='football'),
    path('baseball/', newsapp_views.baseball, name='baseball'),
    path('tennis/', newsapp_views.tennis, name='tennis'), 
    path('golf/', newsapp_views.golf, name='golf'),   
    path('badminton/', newsapp_views.badminton, name='badminton'), 
    path('kabadii/', newsapp_views.kabadii, name='kabadii'), 
    path('boxing/', newsapp_views.boxing, name='boxing'), 
    path('athletics/', newsapp_views.athletics, name='athletics'), 
    path('chess/', newsapp_views.chess, name='chess'), 
    path('swimming/', newsapp_views.swimming, name='swimming'),
    path('shooting/', newsapp_views.shooting, name='shooting'), 
    path('wrestling/', newsapp_views.wrestling, name='wrestling'), 
    path('tabletennis/', newsapp_views.tabletennis, name='tabletennis'),  
    path('other/', newsapp_views.other, name='other'),  
    path('ipl/countries/', newsapp_views.get_ipl_countries, name='ipl_countries'),
    path('ipl/series/', newsapp_views.get_ipl_series, name='ipl_countries'),
    
    

    path('register/',rv.register, name="register"),
    path('login/', rv.user_login, name='login'),
    
]
