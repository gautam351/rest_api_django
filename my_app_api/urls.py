from django.urls import path
from . import views
urlpatterns=[
    path("",view=views.testPoint),
    path("addUser",view=views.addUser),
    path("getAllUser",view=views.getAllUSers),
    path("updateUser",view=views.updateUser),
    path("deleteUser",view=views.deleteUserByid),



]