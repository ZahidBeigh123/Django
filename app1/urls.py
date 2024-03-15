from django.urls import path
from . import views


#URLConf
urlpatterns=[
    path('salam/',views.say_salam)   #here we passing the reference to the function  and not actually calling the function
]
