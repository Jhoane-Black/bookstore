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

@login_required(login_url='login')
def actualizarCliente(request):
    client = models.Client.objects.get(cli_email = request.user)
    if request.method == 'POST':
        client.cli_nom = request.POST['cli_nom']
        client.cli_ape = request.POST['cli_ape']
        client.cli_cc = request.POST['cli_cc']
        client.cli_cc_fecha_expedicion = request.POST['cli_cc_fecha_expedicion']
        client.save()
    context={'client':client}
    return redirect('home')

@login_required(login_url='login')
def generePage(request):
    generos = models.Genere.objects.all()
    context={'generos':generos}
    print(context['generos'])
    return render(request, 'genere.html', context)

@login_required(login_url='login')
def deleteGenere(request):
    if request.method == 'POST':
        models.Genere.objects.get(gen_id = request.POST['gen_id']).delete()
    return redirect('genere')

@login_required(login_url='login')
def formCreateGenere(request):
    context={}
    return render(request, 'formCreateGenere.html',context )

@login_required(login_url='login')
def CreateGenere(request):
    if request.method == 'POST':
        genere = models.Genere(
            gen_id = request.POST['gen_id'],
            gen_name = request.POST['gen_name']
        )
        genere.save()
    return redirect('genere')

@login_required(login_url='login')
def formUpdateGenere(request):
    genere = models.Genere.objects.get(gen_id=request.POST['gen_id'])
    context = {'genere':genere}
    return render(request, 'formUpdateGenere.html',context)

@login_required(login_url='login')
def UpdateGenere(request):
    print(request.POST['gen_id'])
    if request.method == 'POST':
        genere = models.Genere.objects.get(gen_id=request.POST['gen_id'])
        genere.gen_name = request.POST['gen_name']
        genere.save()
    return redirect('genere')

@login_required(login_url='login')
def bookPage(request):
    books = models.Book.objects.all()
    context = {'books':books}
    return render(request, 'book.html', context)

@login_required(login_url='login')
def formCreateBook(request):
    context={}
    return render(request, 'formCreateBook.html',context )

@login_required(login_url='login')
def CreateBook(request):
    if request.method == 'POST':
        Book = models.Book(
            book_id = request.POST['book_id'],
            book_title = request.POST['book_title'],
            book_editorial = request.POST['book_editorial'],
            book_saga = request.POST['book_saga'],
            book_price = request.POST['book_price'],
            book_price_dis = request.POST['book_price_dis']
        )
        Book.save()
    return redirect('bookPage')

@login_required(login_url='login')
def deleteBook(request):
    if request.method == 'POST':
        models.Book.objects.get(book_id = request.POST['book_id']).delete()
    return redirect('bookPage')

@login_required(login_url='login')
def formUpdateBook(request):
    book = models.Book.objects.get(book_id=request.POST['book_id'])
    context = {'book': book}
    return render(request, 'formUpdateBook.html',context)

@login_required(login_url='login')
def UpdateBook(request):
    print(request.POST['book_id'])
    if request.method == 'POST':
        book = models.Book.objects.get(book_id=request.POST['book_id'])
        book.book_title = request.POST['book_title']
        book.book_editorial = request.POST['book_editorial']
        book.book_saga = request.POST['book_saga']
        book.book_price = request.POST['book_price']
        book.book_price_dis = request.POST['book_price_dis']
        book.save()
    return redirect('bookPage')