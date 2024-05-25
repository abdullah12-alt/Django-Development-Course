from django.shortcuts import render
from .models import Post
# Create your views here.

def post(request):
    post=Post.objects.all()
    context={'post':post}
    for i in post:
        print(i.post_img.url)
    return render(request,"post.html",context)

