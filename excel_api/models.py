from django.db import models

class ExcelFile(models.Model):
    file_name = models.CharField(max_length=500)
    sheet_name = models.CharField(max_length=500)
