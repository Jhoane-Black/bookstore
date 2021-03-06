"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .router import router
from django.contrib.auth import views as auth_views
from webapp.view.views import registerPage, loginPage, home, logoutUser, actualizarCliente, generePage, deleteGenere, formCreateGenere, CreateGenere, formUpdateGenere, UpdateGenere
from webapp.view.views import bookPage, formCreateBook, CreateBook, deleteBook, formUpdateBook, UpdateBook, authorPage, deleteAuthor, formCreateAuthor, CreateAuthor, formUpdateAuthor, UpdateAuthor
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('accounts/register',registerPage, name='register'),
    path('accounts/login/',loginPage, name='login'),
    path('logout',logoutUser, name='logout'),
    path('',home,name='home'),
    path('actualizarCliente',actualizarCliente, name='actualizarCliente'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset_form.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirme.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_complete.html"), name="password_reset_complete"),
    path('genere',generePage, name='genere'),
    path('deleteGenere',deleteGenere,name='deleteGenere'),
    path('formCreateGenere', formCreateGenere, name='formCreateGenere'),
    path('CreateGenere', CreateGenere, name='CreateGenere'),
    path('formUpdateGenere', formUpdateGenere, name='formUpdateGenere'),
    path('UpdateGenere', UpdateGenere, name='UpdateGenere'),
    path('bookPage', bookPage, name='bookPage'),
    path('formCreateBook', formCreateBook, name='formCreateBook'),
    path('CreateBook', CreateBook, name='CreateBook'),
    path('deleteBook', deleteBook, name='deleteBook'),
    path('formUpdateBook', formUpdateBook, name='formUpdateBook'),
    path('UpdateBook', UpdateBook, name='UpdateBook'),
    path('authorPage', authorPage, name='authorPage'),
    path('deleteAuthor', deleteAuthor, name='deleteAuthor'),
    path('formCreateAuthor', formCreateAuthor, name='formCreateAuthor'),
    path('CreateAuthor', CreateAuthor, name='CreateAuthor'),
    path('formUpdateAuthor', formUpdateAuthor, name='formUpdateAuthor'),
    path('UpdateAuthor', UpdateAuthor, name='UpdateAuthor'),
]

