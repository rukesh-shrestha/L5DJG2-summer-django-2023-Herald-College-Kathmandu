from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def registerUser(request):
    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        print(username,email,firstname,lastname,password,confirmpassword)

        if password==confirmpassword:
            users = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password

        )
        users.save()
        return redirect("crud:home")
       
    return render(request,"users/register.html")