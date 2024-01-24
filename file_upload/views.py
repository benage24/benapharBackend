# views.py
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from .models import UploadFile
# from .serializers import UploadedFileSerializer
from rest_framework import viewsets
import pandas as pd
from .models import UploadFileExcel
from .serializers import SheetSerializer


# class FileUploadView(APIView):
#     parser_classes = (FileUploadParser,)
#
#     def post(self, request, *args, **kwargs):
#         file_serializer = UploadedFileSerializer(data=request.data)
#
#         if file_serializer.is_valid():
#             file_serializer.save()
#
#             # Perform analysis on the uploaded Excel file using pandas or other libraries
#             file_path = file_serializer.data['file']
#             df = pd.read_excel(file_path)
#
#             # Add your analysis logic here
#
#             return Response({'message': 'File uploaded and analyzed successfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class FileUploadView(viewsets.ModelViewSet):
#     queryset = UploadFile.objects.all()
#     serializer_class = UploadedFileSerializer
#     parser_classes = (FileUploadParser,)
#     def perform_create(self, serializer):
#         serializer.save()
#
#         file_path = serializer.data['file']
#         df=pd.read_excel(file_path)

class SheetViewSet(viewsets.ModelViewSet):
    queryset = UploadFileExcel.objects.all()
    serializer_class = SheetSerializer