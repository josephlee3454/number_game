from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.index),
    path('win/', views.number_guesser),

  
]