from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Tenth,Inter,Engineering,Personal
# Create your views here.
from .forms import FileForm,StudentForm
from django.http import HttpResponse


def index(request):
    print(request)
    return render(request, "student.html")


def personal(request):
    form = FileForm()
    personals = Personal.objects.filter(user = request.user)
    context = {
        "form":form,
        "personals":personals
    }
    if request.method == "POST":
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            personal_details = Personal()
            personal_details.name = form.cleaned_data["name"]
            personal_details.file = form.cleaned_data["file"]
            personal_details.user = request.user
            personal_details.save()
            return redirect("personal")

    return render(request, "personal.html",context)


def academic(request):
    tenth_marks = Tenth.objects.filter(user=request.user)
    inter_marks = Inter.objects.filter(user=request.user)
    engineer_marks = Engineering.objects.filter(user=request.user)
    context = {
        "tenth_marks": tenth_marks,
        "inter_marks": inter_marks,
        "engineer_marks": engineer_marks
    }
    return render(request, "academic.html",context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("academic")
        else:
            return redirect("login")
    else:
        return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("login_user")


def register(request):
    form = StudentForm()
    context = {
        "form":form
    }
    if request.method == 'POST':
        sub_form = StudentForm(request.POST)
        if not sub_form.is_valid():
            return render(request, 'register.html', {'form':sub_form})
        data = sub_form.cleaned_data
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        error_context = {"form":sub_form}
        username_check = User.objects.filter(username = username)
        if username_check:
            error_context["username"] = {
                "errors": {
                    "already_present": "Username already present"
                }
            }
        if username_check:
            return render(request,"register.html",error_context)
        else:
            user = User.objects.create_user(
            username=username, email=email, password=password)
            user.save()

        return redirect("login_user")
    else:
        return render(request, 'register.html',context)
   
def tests(request):
    return render(request,"test.html")