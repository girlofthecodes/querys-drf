from django.db import models

# Create your models here.

class Author(models.Model): 
	first_name = models.CharField(max_length=50, verbose_name='Nombre')
	last_name = models.CharField(max_length=50, verbose_name='Apellido')
	birth_date = models.DateField(verbose_name='Fecha de nacimiento')
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

	class Meta: 
		db_table = 'authors'
	
	def __str__(self): 
		return self.last_name

class Book(models.Model): 
	name = models.CharField(max_length=120, verbose_name='Nombre del libro')
	lsbn = models.IntegerField(default=0, verbose_name='ISBN')
	published_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')

	class Meta: 
		db_table = 'books'
		
	def __str__(self): 
		return self.nama