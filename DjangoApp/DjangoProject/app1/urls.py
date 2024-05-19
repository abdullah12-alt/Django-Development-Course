from django.urls import path
from .views import *
urlpatterns = [
    path("home/",index ,name="index"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact")
    
]
