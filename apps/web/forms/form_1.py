from django import forms

from ..models.model_1 import Table1


class Form1(forms.ModelForm):
    class Meta:
        model = Table1
        fields = "__all__"
        widgets = {
            "char_field": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "autofocus": "autofocus"
                }
            ),
            "number_field": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "email_field": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "choice_field": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "image_field": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "text_field": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),
            "date_time_field": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),
            "date_field": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
            # "time_field": forms.TimeInput(
            #     attrs={
            #         "class": "form-control",
            #         "type": "time"
            #     }
            # ),
        }
