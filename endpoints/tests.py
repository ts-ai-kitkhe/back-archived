from django.test import TestCase

# Create your tests here.
from endpoints.factories  import AuthorsFactory, BookPagesFactory, BooksFactory

class AuthorsModelsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.Authors = AuthorsFactory._meta.model

    def test_author(self):
        # create
        author = AuthorsFactory(full_name='Shota Rustaveli')

        # read
        self.assertEqual(author.full_name, 'Shota Rustaveli')
        self.assertEqual(author.pk, author.id)
        self.assertQuerysetEqual(
            self.Authors.objects.all(),
            ['<Authors: Shota Rustaveli>']
        )

        # update
        author.full_name = 'Shotiko Rustaveli'
        author.save()
        self.assertQuerysetEqual(
            self.Authors.objects.all(),
            ['<Authors: Shotiko Rustaveli>']
        )


class BooksModelsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.Books = BooksFactory._meta.model

    def test_book(self):
        book = BooksFactory(title='Vepkhistkaosani')

        self.assertEqual(book.title, 'Vepkhistkaosani')
        self.assertEqual(book.pk, book.id)
        self.assertQuerysetEqual(
            self.Books.objects.all(),
            ['<Books: Vepkhistkaosani>']
        )

        # update
        book.title = 'Vepxis tkaosani'
        book.save()
        self.assertQuerysetEqual(
            self.Books.objects.all(),
            ['<Books: Vepxis tkaosani>']
        )


class BookPagesModelsTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BookPages = BookPagesFactory._meta.model

    def test_page(self):
        page = BookPagesFactory()
        
        self.assertEqual(page.pk, page.id)
    
    def test_pages(self):
        pages = [BookPagesFactory() for _ in range(10)]

