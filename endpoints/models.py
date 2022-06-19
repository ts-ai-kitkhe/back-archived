from django.db import models

# Create your models here.


# DB objects : books, authors, Book Pages, Bounding boxes, predicted labels

class Books(models.Model):
    # id, book name, author id
    title = models.CharField(max_length=128, db_column='title')
    image_url = models.URLField(max_length=512)
    author_id = models.ForeignKey('Authors', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Authors(models.Model):
    # id, full_name
    full_name = models.CharField(max_length=128, db_column='full_name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookPages(models.Model):
    # id, book_id, order, page_url, status
    class ProcessingStep(models.IntegerChoices):
        TO_DO = 0 
        IN_PROGRESS = 1
        DONE = 2 

    book_id = models.ForeignKey('Books', on_delete=models.CASCADE)
    order = models.IntegerField(db_column='order')
    page_url = models.URLField(max_length=512)
    status = models.IntegerField(choices=ProcessingStep.choices, db_column='processing_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BoundingBoxes(models.Model):
    # id, page_id, bounding_box
    page_id = models.ForeignKey('BookPages', on_delete=models.CASCADE)
    bounding_box = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PredictedLabels(models.Model):
    # id, bounding_box_id, label, confidence
    bounding_box_id = models.ForeignKey('BoundingBoxes', on_delete=models.CASCADE)
    label = models.CharField(max_length=4, db_column='label')
    confidence = models.FloatField(db_column='confidence')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
