
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
        queryset = Author.objects.filter(birth_date__range=('1899-08-31', '1950-08-31')).order_by('birth_date')
        serializer = CreateAuthorSerializer(queryset, many=True)
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