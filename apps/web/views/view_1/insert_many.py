from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ...forms.form_1 import Form1


# @login_required(login_url="auth:login")
def insert_many(request):
    # form = Form1(data=request.POST or None)

    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #         # return redirect(to="web:get_all")
    #         return redirect(to="web:home")

    context = {"data": None}

    return render(request=request, template_name="pages/page_1/insert_many.html", context=context)
