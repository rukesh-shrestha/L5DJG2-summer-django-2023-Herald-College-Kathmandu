from django.urls import path
from .views import registerUser

app_name="users"
urlpatterns = [
    path("register/",registerUser,name="signup")
       
]
