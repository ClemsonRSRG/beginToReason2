from django.urls import path
from django.conf.urls import include, url

from . import views


app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('tutor', views.tutor, name='tutor'),
    path('login', views.login, name='login')

]