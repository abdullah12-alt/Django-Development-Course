from django.shortcuts import render
from .models import Post
# Create your views here.
from .forms import PostForm
def post(request):
    post=Post.objects.all()
    context={'post':post}
   
    return render(request,"post.html",context)


def details(request,id):
    post_detail=Post.objects.get(id=id)
    print(post_detail.content)
    context={"post_detail":post_detail}
    return render(request,"details.html",context)
    
    
    
def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        post=Post.objects.all()
        context={'post':post}
        return render(request,"post.html",context)
    else:
        form=PostForm()
    return render(request,"create-post.html",{"form":form})


