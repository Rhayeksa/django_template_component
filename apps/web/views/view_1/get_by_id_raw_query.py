from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# from ...models.model_1 import Table1


# @login_required(login_url="web:login")
def get_by_id_raw_query(request, id):
    # TODO query and execute

    context = {"data": None}

    return render(request=request, template_name="pages/page_1/get_by_id.html", context=context)
