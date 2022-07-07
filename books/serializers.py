from rest_framework import serializers
from books.models import Author, Book

class CreateAuthorSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Author 
		fields = '__all__'

class RetrieveAuthorsSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Author 
		exclude = ('created_date',)

class RetrieveAuthorSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Author 
		fields = ('id', 'first_name', 'last_name')

class CreatBookSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Book
		fields = '__all__'

class CreatBooksSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Book
		exclude = ('created_date',)

		def to_representation(self, instance): 
			response = super().to_representation(instance)
			response['author'] = RetrieveAuthorsSerializer(instance.author).data
			return response  

