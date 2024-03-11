from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ...forms.form_1 import Form1
from ...models.model_1 import Table1


# @login_required(login_url="auth:login")
def update_one_by_id(request, id):
    model = Table1.objects.get(id_field=id)

    initial = {
        "char_field": model.char_field,
        "number_field": model.number_field,
        "email_field": model.email_field,
        "choice_field": model.choice_field,
        "text_field": model.text_field,
        "image_field": model.image_field,
        "date_time_field": model.date_time_field,
        "date_field": model.date_field,
    }

    form = Form1(
        data=request.POST or None,
        initial=initial,
        instance=model
    )

    if request.method == "POST":
        if "save" in request.POST and form.is_valid():
            form.save()
            return redirect(to="web:get_by_id", id=model.id_field)

    return render(request=request, template_name="pages/page_1/update_one_by_id.html", context={"data": form})
