from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage),
    path('results', views.Results)
]