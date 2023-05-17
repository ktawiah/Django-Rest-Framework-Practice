from django.shortcuts import render
from .models import Book, Category, Progress
from .serializers import BookSerializer, ProgressSerializer, CategorySerializer
from rest_framework import viewsets

# Create your views here.


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProgressViewset(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
