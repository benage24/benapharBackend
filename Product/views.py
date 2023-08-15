from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from.serializers import ProductSerializer
# Create your views here.
from .models import Product


def get_object(pk):
    try:
        return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
class ProductListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)

        return Response(serializer.data)

class ProductCreateView(APIView):
    serializer_class = ProductSerializer
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get(self, request, pk, format=None):
        snippet = get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDelete(APIView):
    def delete(self, request, pk, format=None):
        snippet = get_object(pk)
        print(snippet)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductUpdate(APIView):

    def put(self, request, pk, format=None):
        snippet = get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
