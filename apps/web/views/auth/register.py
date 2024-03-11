from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def register(request):
    context = {"alert": "hidden"}
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        check_username = User.objects.filter(username=username).exists()
        check_email = User.objects.filter(email=email).exists()
        if check_username:
            context = {
                "alert": "",
                "msg": "Username sudah terdaftar"
            }
        elif check_email:
            context = {
                "alert": "",
                "msg": "Email sudah terdaftar"
            }
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect(to="web:login")
    return render(request=request, template_name="pages/auth/register.html", context=context)
