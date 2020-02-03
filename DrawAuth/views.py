import base64
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def index(response):
    return HttpResponse("Index")


def login(response):
    return HttpResponse("Login")

def get_current_time():
    currentDT = datetime.datetime.now()
    return currentDT


def home_view(request, *args, **kwargs):
    print(get_current_time())
    print("LOGGED IN AS: ")
    print(request.user)
    my_context = {
        "title": "Welcome to the home page",
        "user_list": [1, 2, 3, 4, 5, 6, 7],
    }
    return render(request, "home.html", my_context)


def graphical_login_view(request, *args, **kwargs):
    return render(request, "graphical_login.html", {})


def reguser(request, *args, **kwargs):
    return render(request, "reg_select_user.html", {})


def hash_test(request):
    # turns images into base64 and returns it ready for hashing.
    image_id = request.POST.get('password_image_id')
    import base64
    with open("static/images/PasswordImages/" + image_id, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    request.session['password'] = str
    username = request.session.get('username')
    print(get_current_time())
    print("LOGIN:")
    print("Username:")
    print(request.session.get('username'))
    print("Password:")
    print(request.session.get('password'))
    print("Password Image number:")
    print(image_id)
    return render(request, "registration/login.html", {
        'username': username,
        'password': str})


def reg_hash(request):
    image_id = request.POST.get('password_image_id')
    path = "static/images/PasswordImages/" + image_id
    with open(path, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    request.session['password'] = str
    username = request.session.get('username')
    print(get_current_time())
    print("REGISTER:")
    print("Username:")
    print(request.session.get('username'))
    print("Password:")
    print(request.session.get('password'))
    print("Password Image number:")
    print(image_id)

    return render(request, "registration/signup.html", {
        'username': username,
        'password': str})
