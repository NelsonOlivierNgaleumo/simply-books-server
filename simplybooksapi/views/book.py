from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import Book, Author, Genre


class BookView(ViewSet):
    def retrieve(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            genres = Genre.objects.filter(book=book)
            book.genres = genres
            serializer = SingleBookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            author = Author.objects.get(pk=request.data["author_id"])
        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=status.HTTP_400_BAD_REQUEST)

        book = Book.objects.create(
            author=author,
            title=request.data["title"],
            image=request.data["image"],
            price=request.data["price"],
            sale=request.data["sale"],
            uid=request.data["uid"],
            description=request.data["description"]
        )
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            author = Author.objects.get(pk=request.data["author_id"])
            
            book.author = author
            book.title = request.data["title"]
            book.image = request.data["image"]
            book.price = request.data["price"]
            book.sale = request.data["sale"]
            book.uid = request.data["uid"]
            book.description = request.data["description"]
            
            book.save()
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'description')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author_id', 'title', 'image', 'price', 'sale', 'uid', 'description')


class SingleBookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'image', 'price', 'uid', 'description', 'genres')
