from django.contrib.auth import logout as Dlogout
from django.contrib.auth.models import User
from django.shortcuts import redirect


def logout(request):
    Dlogout(request=request)
    return redirect(to="auth:login")
