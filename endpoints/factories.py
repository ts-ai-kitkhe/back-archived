import factory
import factory.django
import factory.fuzzy

from endpoints.models import Authors, BookPages, Books


class AuthorsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Authors

    full_name = factory.Faker("name")        


class BooksFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Books

    title = factory.Faker("name")
    image_url = factory.Faker("image_url")
    author_id = factory.SubFactory(AuthorsFactory)


class BookPagesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BookPages
    
    book_id = factory.SubFactory(BooksFactory)
    order = factory.Sequence(lambda n: n)
    page_url = factory.Faker("image_url")
    status = factory.fuzzy.FuzzyChoice(choices=[BookPages.ProcessingStep.TO_DO, BookPages.ProcessingStep.IN_PROGRESS, BookPages.ProcessingStep.DONE])

    