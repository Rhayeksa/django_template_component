from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ...models.model_1 import Table1
from ...forms.form_1 import Form1


# @login_required(login_url="web:login")
def get_by_id(request, id):
    model = Table1.objects.get(id_field=id)
    form = Form1()

    context = {
        "data": {
            "model": model,
            "form": form,
        }
    }

    return render(request=request, template_name="pages/page_1/get_by_id.html", context=context)
