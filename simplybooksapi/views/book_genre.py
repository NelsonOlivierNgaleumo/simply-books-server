from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import BookGenre, Book, Genre


class BookGenreView(ViewSet):
    """Simplybooks api Book genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Book
        Returns:
            Response -- JSON serialized Book
        """
        try:
            book_genre = BookGenre.objects.get(pk=pk)
            serializer = BookGenreSerializer(book_genre)
            return Response(serializer.data)
        except BookGenre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all books
        Returns:
            Response -- JSON serialized list of books
        """
        book_genres = BookGenre.objects.all()
        serializer = BookGenreSerializer(book_genres, many=True)
        return Response(serializer.data)
    
    def create(self, request):
      bookId = Book.objects.get(pk=request.data["book_id"])
      genreId = Genre.objects.get(pk=request.data["genre_id"])
      bookGenre = BookGenre.objects.create(
          book=bookId,
          genre=genreId,
      )
      serializer = BookGenreSerializer(bookGenre)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  
    def update(self, request, pk):
      bookId = Book.objects.get(pk=request.data["book"])
      genreId = Genre.objects.get(pk=request.data["genre"])
      
      bookGenre = BookGenre.objects.get(pk=pk)
      bookGenre.book_id = bookId
      bookGenre.genre_id = genreId
      bookGenre.save()
      serializer = BookGenreSerializer(bookGenre)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
      bookGenre = BookGenre.objects.get(pk=pk)
      bookGenre.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class BookGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for Book genres
    """
    class Meta:
        model = BookGenre
        fields = ('book', 'genre')
