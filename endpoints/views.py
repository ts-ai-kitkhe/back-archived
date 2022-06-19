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
