from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import StudentRegistrationForm
from .models import StudentProfile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import StudentRegistrationForm
from .models import StudentProfile

def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            StudentProfile.objects.create(
                user=user,
                roll_number=form.cleaned_data["roll_number"],
                course=form.cleaned_data["course"],
                semester=form.cleaned_data["semester"],
            )

            login(request, user)

            return redirect("dashboard")
    else:
        form = StudentRegistrationForm()

    return render(
        request,
        "student_portal/register.html",
        {"form": form}
    )


def dashboard(request):
    return render(
        request,
        "student_portal/dashboard.html"
    )
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(
            request,
            "student_portal/login.html",
            {"error": "Invalid username or password."}
        )

    return render(
        request,
        "student_portal/login.html"
    )
def home(request):
    return render(request, "student_portal/home.html")