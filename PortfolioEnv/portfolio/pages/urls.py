from django.urls import path,include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path("",home,name='home'),
    path("projects/",project_index, name="project_index"),
    path("projects/<int:pk>/",project_detail, name="project_detail"),
]
