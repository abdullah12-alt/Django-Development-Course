from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    return render(request,'pages/home.html',{})


def project_index(request):
    project=Project.objects.all()
    context={
        "project":project
    }
    print(project)
    return render(request,"projects/project_index.html",context)


def project_detail(request, pk):

    project = Project.objects.get(pk=pk)

    context = {

        "project": project

    }

    return render(request, "projects/project_details.html", context)