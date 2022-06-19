from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from endpoints.views import AuthorsViewSet
from endpoints.views import BooksViewSet
from endpoints.views import BookPagesViewSet
from endpoints.views import BoundingBoxesViewSet
from endpoints.views import PredictedLabelsViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"authors", AuthorsViewSet, basename="authors")
router.register(r"books", BooksViewSet, basename="books")
router.register(r"bookpages", BookPagesViewSet, basename="bookpages")
router.register(r"boundingboxes", BoundingBoxesViewSet, basename="boundingboxes")
router.register(r"predictedlabels", PredictedLabelsViewSet, basename="predictedlabels")


urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
]