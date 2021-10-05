from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('map', views.default_map, name="default")
]