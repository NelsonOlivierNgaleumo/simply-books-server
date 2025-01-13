from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import Author


class AuthorView(ViewSet):
    """Handles requests about authors"""

    def retrieve(self, request, pk):
        """Handle GET requests for single author"""
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all authors"""
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests for authors"""
        author = Author.objects.create(
            email=request.data["email"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            image=request.data["image"],
            favorite=request.data["favorite"],
            uid=request.data["uid"]
        )
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an author"""
        try:
            author = Author.objects.get(pk=pk)
            author.email = request.data["email"]
            author.first_name = request.data["first_name"]
            author.last_name = request.data["last_name"]
            author.image = request.data["image"]
            author.favorite = request.data["favorite"]
            author.uid = request.data["uid"]

            author.save()

            serializer = AuthorSerializer(author)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Author.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Handle DELETE requests for an author"""
        try:
            author = Author.objects.get(pk=pk)
            author.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for authors"""
    class Meta:
        model = Author
        fields = ('id', 'email', 'first_name', 'last_name', 'image', 'favorite', 'uid')
