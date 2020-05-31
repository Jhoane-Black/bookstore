from django.shortcuts import render
from rest_framework import viewsets
from webapp.model import models
from webapp import serializers

# Create your views here.
class AuthorViewset(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

class ClientViewset(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

class GenereViewset(viewsets.ModelViewSet):
    queryset = models.Genere.objects.all()
    serializer_class = serializers.GenereSerializer