from django.urls import path
from . import views


#URLConf
urlpatterns=[
    path('',views.home,name="home")   #here we passing the reference to the function  and not actually calling the function
]
