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

def about(request):
    head="Welcome To Minhaj University Lahore"
    para="""Minhaj University Lahore was founded in 1986 by Shaykh-ul-Islam Prof. Dr Muhammad Tahir-ul-Qadri, patron-in-chief of Minhaj ul Quran International. It is located in a significant place which is easily approachable from all the main areas of the city. Its campuses are situated at Township & Model Town. Degree awarding status was granted by Govt. of the Punjab vide Act No: XII of 2005. The Higher Education Commission of Pakistan has also recognized Minhaj University, as ‘W3‘ ranking University.

It comprises of nine faculties that of Computer Science & Information Technology, Basic Sciences & Mathematics, Economics & Management Sciences, Social Sciences & Humanities, Languages, Shariah & Islamic Studies, Engineering, Allied Health Sciences, Applied Sciences.
    """
    context={
        "head":head,
        "para":para
    }
    return render(request,"about.html",context)


def contact(request):
    if request.method=="POST":
        name =request.POST.get("name")
        email =request.POST.get("email")
        phone=request.POST.get("phone")
        context={
            "name":name,
            "email":email,
            "phone":phone
        }
        return render(request,"data.html",context)
        
    
        
    return render(request,"contact.html",{})
