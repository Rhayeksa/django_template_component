from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import connection
from django.shortcuts import render

from utils.sql_to_json import sql_to_json


# @login_required(login_url="web:login")
def get_all_raw_query(request):
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT
            char_field
            , number_field
            , email_field
            , choice_field
            , text_field
        FROM table_1
        ORDER BY id_field DESC
        """
    )
    page = request.GET.get("page", 1)
    paginator = Paginator(object_list=sql_to_json(cursor=cursor), per_page=2)
    # paginator = Paginator(object_list=model, per_page=5)

    try:
        data = paginator.page(number=page)
    except PageNotAnInteger:
        data = paginator.page(number=1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {"data": data}

    return render(request=request, template_name="pages/page_1/get_all_list.html", context=context)
