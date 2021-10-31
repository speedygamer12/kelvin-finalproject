from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeViewWizard.as_view(), name= 'form'),
    
]