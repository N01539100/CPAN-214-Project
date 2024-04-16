from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/books',
        'GET /api/books/:id',
    ]

    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(id=pk)

    if book is None:
        return Response({'message': 'Book not found'}, status=404)

    serializer = BookSerializer(book, many=False)

    return Response(serializer.data)
