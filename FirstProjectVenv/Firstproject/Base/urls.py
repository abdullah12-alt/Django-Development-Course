from django.urls import path
from .views import *
urlpatterns = [
    path('post/', post, name="post"),
    path('post-detail/<int:id>', details, name="post-details")
]