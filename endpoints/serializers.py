from rest_framework import serializers
from endpoints.models import Authors, Books, BookPages, BoundingBoxes, PredictedLabels


class AuthorsSerializer(serializers.ModelSerializer):
    pass


class BooksSerializer(serializers.ModelSerializer):
    pass


class BookPagesSerializer(serializers.ModelSerializer):
    pass


class BoundingBoxesSerializer(serializers.ModelSerializer):
    pass


class PredictedLabelsSerializer(serializers.ModelSerializer):
    pass
