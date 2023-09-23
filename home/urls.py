from django.urls import path
from home.views import home , listemploye

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('listemploye/', listemploye, name='listemploye')
]
