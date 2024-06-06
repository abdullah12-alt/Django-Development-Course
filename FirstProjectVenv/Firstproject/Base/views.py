from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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
        return render(request,"accounts/register.html",{"form":form})
    
    
def login_view(request):
    if request.method=='POST':
        
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password1")
            user=authenticate(username=username,password=password)
            if user is not None:
                 login(request,user)
            return redirect("post")
    else:
        form = AuthenticationForm()
        return render(request,"accounts/login.html",{"form":form})
    
def logout_view(request):
    # Log out the user
    logout(request)
    
    # Create an empty authentication form
    form = AuthenticationForm()
    
    # Render the login page with the empty authentication form
    return render(request, "accounts/login.html", {"form": form})









@login_required
def post(request):
    post=Post.objects.all()
    context={'post':post}
   
    return render(request,"post.html",context)

@login_required
def details(request,id):
    post_detail=Post.objects.get(id=id)
    print(post_detail.content)
    context={"post_detail":post_detail}
    return render(request,"details.html",context)
    
    
@login_required
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


