from django.urls import path
from app2 import views

urlpatterns = [
    path('index/', views.index),
    path('pagina2/', views.pagina2),
]