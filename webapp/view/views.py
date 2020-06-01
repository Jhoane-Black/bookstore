from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from webapp.view.serializers import CreateUserForm
# Create your views here.
from rest_framework import viewsets
from webapp.model import models
from . import serializers
from django.db.models import Q

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

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
   
                messages.success(request, 'La cuenta ha sido creada ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuario o contraseña incorrecta')
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    client = models.Client.objects.get(cli_email = request.user)
    context={'client':client}
    return render(request, 'home.html', context)

def actualizarCliente(request):
    client = models.Client.objects.get(cli_email = request.user)
    print(request.POST)
    if request.method == 'POST':
        client.cli_nom = request.POST['cli_nom']
        client.cli_ape = request.POST['cli_ape']
        client.cli_cc = request.POST['cli_cc']
        client.cli_cc_fecha_expedicion = request.POST['cli_cc_fecha_expedicion']
        client.save()
    context={'client':client}
    return redirect('home')
