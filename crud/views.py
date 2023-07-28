from django.shortcuts import render,redirect
from .models import Blog,Contact #manager->objects

from .forms import BlogForm

# Create your views here.
def homepage(request):
    blog=Blog.objects.all()
    return render(request,"crud/index.html",{"blogs":blog})

def particularData(request,id):
    blog=Blog.objects.get(id=id)
    context ={"blog":blog}
    return render(request,"crud/index.html",context)

def create(request):
    forms = BlogForm(request.POST or None)

    if(forms.is_valid()):
        forms.save()
        return redirect("crud:home")

    return render(request,"crud/creates.html",{"forms":forms})



def contacts(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        # cont = Contact(           
        #     name=name,
        #     email=email,
        #     message=message
        # )
        cont =Contact.create(name,message,email)
        cont.save()
        
    return render(request,"crud/contact.html")

def deleteData(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return redirect("crud:home")

def updateData(request,id):
    blog=Blog.objects.get(id=id)
    forms=BlogForm(request.POST or None,instance=blog)

    if forms.is_valid():
        forms.save()
        return redirect("crud:home")

    return render(request,"crud/create.html",{"forms":forms})
   