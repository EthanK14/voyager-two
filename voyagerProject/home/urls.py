from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Jupiter/', views.jupiter, name='jupiter'),
    path('Saturn/', views.saturn, name='saturn'),
    path('Uranus/', views.uranus, name='uranus'),
    path('Neptune/', views.neptune, name='neptune'),
    path('Interstellar/', views.interstellar, name='interstellar'),

]
