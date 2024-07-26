from django.urls import path
from .views import *

# Base URL ==>>>>>>>>> http://127.0.0.1:8000/kider/

urlpatterns = [
    path("home/", view_home, name="home"),
    path("about/", view_about, name="about"),
    path("contact/", view_contact, name="contact"),
]
