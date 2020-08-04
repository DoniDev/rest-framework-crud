from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book
    serializer_class = BookSerializer


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookDestroyView(generics.DestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer
    lookup_field = 'id'

