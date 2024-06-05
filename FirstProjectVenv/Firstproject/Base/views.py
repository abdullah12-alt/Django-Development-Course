from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm



def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password1")
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect("post")
    else:
        form = RegistrationForm()
        return render(request,"register.html",{"form":form})
            











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


