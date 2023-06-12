from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm, UserForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# from basic_app.models import UserProfileInfo


# Create your views here.
def index(request):
    context_dict = {"number": 20, "text": "Hello World!"}
    return render(request, "basic_app/index.html", context_dict)


@login_required
def other(request):
    return render(request, "basic_app/other.html")


def relative(request):
    return render(request, "basic_app/relative_url_templates.html")


def register(request):
    registered = False

    if request.method == "POST":
        profile_form = UserProfileInfoForm(request.POST)
        user_form = UserForm(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(
        request,
        "basic_app/registration.html",
        context={
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
        },
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed!")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid login details!")

    return render(request, "basic_app/login.html", {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
