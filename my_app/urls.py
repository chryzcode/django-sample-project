from django.urls import path
from my_app.views import *

urlpatterns = [
    path('', customHomePage, name='custom_home_page')
]
