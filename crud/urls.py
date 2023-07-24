from django.urls import path
from .views import homepage,create,particularData,contacts

urlpatterns = [
    path("",homepage,name="home"),
    path("create/",create),
    path("<int:id>/",particularData,name="particular"),
    path("contacts/",contacts)

    
]