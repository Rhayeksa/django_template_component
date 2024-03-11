import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from ...models.model_1 import Table1


# @login_required(login_url="web:login")
def get_all(request):
    model = Table1.objects.all().order_by("-id_field")
    # model = Table1.objects.using('asdf').all().order_by("-id")
    page = request.GET.get("page", 1)

    paginator = Paginator(object_list=model, per_page=2)
    # paginator = Paginator(object_list=model, per_page=5)

    try:
        data = paginator.page(number=page)
    except PageNotAnInteger:
        data = paginator.page(number=1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {"data": data}

    return render(request=request, template_name="pages/page_1/get_all_list.html", context=context)
