from rest_framework import serializers
from endpoints.models import Authors, Books, BookPages, BoundingBoxes, PredictedLabels


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class BookPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPages
        fields = '__all__'


class BoundingBoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoundingBoxes
        fields = '__all__'


class PredictedLabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictedLabels
        fields = '__all__'
