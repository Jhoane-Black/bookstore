from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(primary_key=True, max_length=10)
    book_title = models.CharField(max_length=50)
    book_editorial = models.CharField(max_length=50)
    book_saga = models.CharField(max_length=50)
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    book_price_dis = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.book_title

class Genere(models.Model):
    gen_id = models.CharField(primary_key=True, max_length=10)
    gen_name = models.CharField(max_length=50)

    def __str__(self):
        return self.gen_name

class Book_Genere(models.Model):
    bxg_book = models.ForeignKey(Book, on_delete=models.PROTECT)
    bxg_gen = models.ForeignKey(Genere, on_delete=models.PROTECT)

class Author(models.Model):
    aut_id = models.CharField(primary_key=True, max_length=10)
    aut_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.aut_name

class Book_Author(models.Model):
    bxa_aut = models.ForeignKey(Author, on_delete=models.PROTECT)
    bxa_book = models.ForeignKey(Book, on_delete=models.PROTECT)

class Client(models.Model):
    cli_id = models.CharField(primary_key=True, max_length=20)
    cli_nom = models.CharField(max_length=30, null=True)
    cli_ape = models.CharField(max_length=150, null=True)
    cli_email = models.CharField(max_length=254)
    cli_cc = models.CharField(max_length=20, null=True)
    cli_cc_fecha_expedicion = models.DateField(null=True)
    def __str__(self):
        return self.cli_nom

class Payment(models.Model):
    pay_id = models.CharField(primary_key=True, max_length=10)
    pay_type = models.CharField(max_length=20)
    pay_allow = models.BooleanField()

class Orden(models.Model):
    ord_id = models.CharField(primary_key=True, max_length=10)
    ord_cli = models.ForeignKey(Client, on_delete=models.PROTECT)
    ord_pay_id = models.CharField(max_length=10)
    ord_ord_date = models.DateField(auto_now=True)
    ord_pay_date = models.DateField(auto_now=False)

class Orden_Details(models.Model):
    od_id = models.CharField(primary_key=True, max_length=10)
    od_book = models.ForeignKey(Book, on_delete=models.PROTECT)
    od_ord = models.ForeignKey(Orden, on_delete=models.PROTECT)

