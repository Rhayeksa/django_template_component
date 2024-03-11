import uuid
from django.db import models


class Table1(models.Model):
    GENDER = (
        ("Pria", "Pria"),
        ("Wanita", "Wanita"),
    )

    id_field = models.AutoField(primary_key=True, editable=False)
    char_field = models.CharField(max_length=45)
    number_field = models.BigIntegerField(null=True, blank=True)
    email_field = models.EmailField(max_length=225, unique=True)
    choice_field = models.CharField(
        max_length=9, choices=GENDER, null=False, blank=False)
    text_field = models.TextField()
    image_field = models.ImageField(
        upload_to="images/", null=True, blank=True)
    date_time_field = models.DateTimeField(null=True, blank=True)
    # time_field = models.TimeField(null=True, blank=True)
    # file_field = models.FileField(null=True, blank=True)
    date_field = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "table_1"
