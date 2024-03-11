from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ...forms.form_1 import Form1


# @login_required(login_url="auth:login")
def insert_one_raw_query(request):
    # form = Form1(data=request.POST or None)

    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #         return redirect(to="web:get_all_raw_query")

    context = {}

    return render(request=request, template_name="pages/page_1/get_all_raw_query.html", context=context)
