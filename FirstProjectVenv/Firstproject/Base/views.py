from django.shortcuts import render
from .models import Post
# Create your views here.

def post(request):
    post=Post.objects.all()
    context={'post':post}
   
    return render(request,"post.html",context)


def details(request,id):
    post_detail=Post.objects.get(id=id)
    print(post_detail.content)
    context={"post_detail":post_detail}
    return render(request,"details.html",context)
    
