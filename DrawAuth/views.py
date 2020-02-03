from django.http import HttpResponse


# Create your views here.

def index(response):
    return HttpResponse("Index")


def login(response):
    return HttpResponse("Login")
