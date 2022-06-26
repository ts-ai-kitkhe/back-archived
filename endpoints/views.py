from email.mime import image
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import mixins

from endpoints.models import Authors
from endpoints.serializers import AuthorsSerializer

from endpoints.models import Books
from endpoints.serializers import BooksSerializer

from endpoints.models import BookPages
from endpoints.serializers import BookPagesSerializer

from endpoints.models import BoundingBoxes
from endpoints.serializers import BoundingBoxesSerializer

from endpoints.models import PredictedLabels
from endpoints.serializers import PredictedLabelsSerializer


class AuthorsViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = AuthorsSerializer
    queryset = Authors.objects.all()
    

class BooksViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()


class BookPagesViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BookPagesSerializer
    queryset = BookPages.objects.all()


class BoundingBoxesViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BoundingBoxesSerializer
    queryset = BoundingBoxes.objects.all()    


class PredictedLabelsViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PredictedLabelsSerializer
    queryset = PredictedLabels.objects.all()    


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BooksList(APIView):

    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)


class AddBook(APIView):

    def post(self, request):
        print(request.data)
        author = request.data.get("author")
        title = request.data.get("title")

        if Authors.objects.filter(full_name=author).exists():
            au = Authors.objects.get(full_name=author)
        else:
            au = Authors(full_name=author)
            au.save()
        print(au.id)

        if not Books.objects.filter(title=title, author_id=au.id).exists():
            b = Books(title=title, image_url=request.data.get("image_url"), 
                        author_id=au)
            b.save()
            return Response(f"Book \"{title}\" by {author} added successfully", 
                            status=status.HTTP_201_CREATED)
        else:   
            return Response(f"Book \"{title}\" by {author} already exists", status=status.HTTP_226_IM_USED)