from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BookSerializer
from .models import Book
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
