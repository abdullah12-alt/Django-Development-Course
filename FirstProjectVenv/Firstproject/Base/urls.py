from django.urls import path
from .views import *
urlpatterns = [
    path('post/', post, name="post"),
    path('post-detail/<int:id>', details, name="post-details"),
    path('create-post/', create_post, name="create-post"),
    path("register/",register,name="register"),
    path("accounts/login/",login_view,name="login"),
    path('logout/', logout_view, name='logout'),
]