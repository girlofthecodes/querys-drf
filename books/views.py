
from functools import partial
from yaml import serialize
from books.models import Book, Author
from books.serializers import CreateAuthorSerializer, RetrieveAuthorsSerializer, RetrieveAuthorSerializer, CreatBookSerializer, CreatBooksSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here

class CreateAuthorView(APIView):
    """
    List all author, or create a new author.
    """
    def get(self, request):
        queryset = Author.objects.all()
        serializer = RetrieveAuthorsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateAuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message':'Autor creado exitosamente',
            'data':serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)
    

class RetrieveAuthorsView(APIView): 
    """
    List an author, or update an author.
    """
    def get(self, request, id): 
        queryset = Author.objects.get(id=id)
        serializer = RetrieveAuthorSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id): 
        try: 
            queryset = Author.objects.get(id=id)
            serializer = RetrieveAuthorSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {
                'message':'Autor actualizado exitosamente',
                'data':serializer.data
            }
            return Response(data, status=status.HTTP_302_FOUND)
        except: 
             return Response({'msg':'El libro no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id): 
        try: 
            queryset = Author.objects.get(id=id)
            if queryset.status_delete: 
                queryset.status_delete = True
                return Response({'msg':'El autor ya ha sido eliminado'}, status=status.HTTP_404_NOT_FOUND)
            queryset.status_delete=True
            queryset.save()
            return Response({'msg':'Se ha eliminado el autor exitosamente'}, status=status.HTTP_200_OK)
        except: 
            return Response({'msg':'El autor no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)

class CreateBookView(APIView): 
    def get(self, request): 
        queryset = Book.objects.all()
        serializer = CreatBookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request): 
        serializer = CreatBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message':'Libro registrado exitosamente',
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)

class RetrieveBooksView(APIView): 
    def get(self, request, id): 
        queryset = Book.objects.get(id=id)
        serializer = CreatBooksSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, id): 
        try: 
            queryset = Book.objects.get(id=id)
            serializer = CreatBookSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {
                'message':'Libro actualizado exitosamente',
                'data':serializer.data
            }
            return Response(data, status=status.HTTP_302_FOUND)
        except: 
            return Response({'msg':'El libro no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id): 
        try: 
            queryset = Book.objects.get(id=id)
            if queryset.status_delete: 
                queryset.status_delete = True
                return Response({'msg':'El libro ya ha sido eliminado'}, status=status.HTTP_404_NOT_FOUND)
            queryset.status_delete=True
            queryset.save()
            return Response({'msg':'Se ha eliminado el libro exitosamente'}, status=status.HTTP_200_OK)
        except: 
            return Response({'msg':'El libro no se ha encontrado'}, status=status.HTTP_404_NOT_FOUND)