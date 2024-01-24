
# serializers.py
from rest_framework import serializers
from .models import UploadFileExcel

# class UploadedFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UploadFile
#         fields = ('id', 'file', 'uploaded_at')
#
class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFileExcel
        fields = ['id', 'sheet_name', 'column_data']
