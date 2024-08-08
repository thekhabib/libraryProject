from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


# class BooksListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BooksListApiView(APIView):

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        context = {
            'status': f'Returned {len(books)} books',
            'books': serializer_data,
        }
        return Response(context)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailApiView(APIView):

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        serializer = BookSerializer(book).data
        context = {
            'status': True,
            'book': serializer,
        }
        return Response(context)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        context = {
            'status': True,
            'message': f'{book_saved} updated',
        }
        return Response(context)


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDeleteApiView(APIView):

    def delete(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(pk=kwargs['pk'])
            book.delete()
            return Response({
                'stattus': True,
                'message': 'Book successfully deleted',
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': False,
                'message': 'Book not found',
            }, status=status.HTTP_404_NOT_FOUND)


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            context = {
                'status': "Book Created",
                'book': serializer.data,
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
