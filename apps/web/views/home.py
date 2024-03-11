# from django.urls import get_resolver, path, URLPattern
from django.shortcuts import render


def home(request):
    # print(get_resolver().reverse_dict.keys())
    return render(request=request, template_name="pages/home.html", context={})
