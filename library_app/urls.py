from django.urls import path
from .views import *

urlpatterns = [

    path('home', home, name='library_app'),
    path('readers', readers_tab, name="readers_tab"),
    path('readers/add',save_reader),

    

    
]