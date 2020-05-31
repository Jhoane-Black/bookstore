from rest_framework import serializers
from .models import Author, Book, Client, Genere

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'  

class GenereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genere
        fields = '__all__'  