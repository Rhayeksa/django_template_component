from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from ...models.model_1 import Table1


# @login_required(login_url="auth:login")
def delete_many_by_id_raw_query(id):
    Table1.objects.filter(id=id).delete()
    # return redirect(to="web:get_by_id")
    return redirect(to="web:home")
