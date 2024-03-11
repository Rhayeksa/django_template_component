from django.contrib.auth import authenticate, login as Dlogin
from django.shortcuts import redirect, render


def login(request):
    context = {"alert": "hidden"}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user != None:
            Dlogin(request=request, user=user)
            return redirect(to="web:home")
        else:
            context = {
                "alert": "",
                "msg": "username atau password salah",
            }

    return render(request=request, template_name="pages/auth/login.html", context=context)
