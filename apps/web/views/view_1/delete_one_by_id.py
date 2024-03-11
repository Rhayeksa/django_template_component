from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from apps.web.models.model_1 import Table1


# @login_required(login_url="auth:login")
def delete_one_by_id(request, id):
    Table1.objects.filter(id_field=id).delete()

    # return redirect(to="web:get_all")
    return redirect(to="web:home")
