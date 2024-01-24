from django.db import models

# Create your models here.
# class UploadFile(models.Model):
#     file=models.FileField(upload_to="files/",default=None)
#     uploaded_at=models.DateTimeField(auto_now_add=True)
#
#
#     # def __str__(self):
#     #     return self.file

# models.py


class UploadFileExcel(models.Model):
    sheet_name = models.CharField(max_length=255)
    column_data = models.JSONField()

    def __str__(self):
        return self.sheet_name
