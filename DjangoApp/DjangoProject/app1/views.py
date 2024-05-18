from django.shortcuts import render

# Create your views here.
def index(request):
    employe=[
        (1,'Ali',32),
        (2,'Akram',22),
        (3,'bila',31),
        (4,'Jack',42),
        (5,'Jimi',26)
    ]
    for i in employe:
        print(i)
    
    context={"employe":employe}
    return render(request,'home.html',context)