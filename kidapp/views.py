from django.shortcuts import render


# Create your views here.
def view_home(request):
    return render(request, "kidapp/home.html")


def view_about(request):
    return render(request, "kidapp/about.html")


def view_classes(request):
    return render(request, "kidapp/classes.html")


def view_facilites(request):
    return render(request, "kidapp/facilites.html")


def view_contact(request):
    return render(request, "kidapp/contact.html")
