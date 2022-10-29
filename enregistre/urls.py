from django.urls import path

from . import views

urlpatterns = [
   path('', views.verification, name='verification'),
   path('enregistrements/', views.enregistrements, name='enregistrements'),
   
   
   
    
]