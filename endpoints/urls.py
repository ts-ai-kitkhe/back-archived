from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter

from endpoints.views import AuthorsViewSet
from endpoints.views import BooksViewSet
from endpoints.views import BookPagesViewSet
from endpoints.views import BoundingBoxesViewSet
from endpoints.views import PredictedLabelsViewSet
from endpoints.views import BooksList 
from endpoints.views import AddBook


router = DefaultRouter(trailing_slash=False)
router.register(r"authors", AuthorsViewSet, basename="authors")
router.register(r"books", BooksViewSet, basename="books")
router.register(r"bookpages", BookPagesViewSet, basename="bookpages")
router.register(r"boundingboxes", BoundingBoxesViewSet, basename="boundingboxes")
router.register(r"predictedlabels", PredictedLabelsViewSet, basename="predictedlabels")


urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    path('books/list', BooksList.as_view()),
    path('books/', AddBook.as_view()),
]