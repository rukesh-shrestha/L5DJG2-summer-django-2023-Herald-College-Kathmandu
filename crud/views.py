from django.shortcuts import render,redirect
from .models import Blog #manager->objects

from .forms import BlogForm

# Create your views here.
def homepage(request):
    blog=Blog.objects.all()
    return render(request,"crud/index.html",{"blogs":blog})



def create(request):
    forms = BlogForm(request.POST or None)

    if(forms.is_valid()):
        forms.save()
        return redirect("home")

    return render(request,"crud/create.html",{"forms":forms})