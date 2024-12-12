import pytest

class TestBooksCollector:

    def test_value_books_genre(self, collector):
        collector.add_new_book(name='Книга_1')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book', (
            '',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        ),
            ids=[
            "empty name",
            "long name",
        ],
        )
    def test_add_new_book_add_books_with_wrong_names(self, collector, book):
        collector.add_new_book(name=book)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_set_genre(self, collector):
        book_name = 'Книга_1'
        genre = 'Фантастика'
        collector.add_new_book(name=book_name)
        collector.set_book_genre(name=book_name, genre=genre)
        assert collector.books_genre[book_name] == genre

    def test_get_book_genre_get_genre(self, collector):
        book_name = 'Книга_1'
        genre = 'Фантастика'
        collector.add_new_book(name=book_name)
        collector.set_book_genre(name=book_name, genre=genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_get_genre_list(self, collector):
        books = ['Книга_1', 'Книга_2', 'Книга_3']
        genres = ['Фантастика', 'Ужасы']
        for book in books:
            collector.add_new_book(name=book)
        for book, genre in [(books[0], genres[0]), (books[1], genres[0]), (books[2], genres[1])]:
            collector.set_book_genre(name=book, genre=genre)

        specific_genre = 'Фантастика'
        expected_books = ['Книга_1', 'Книга_2']
        books_with_specific_genre = collector.get_books_with_specific_genre(specific_genre)
        assert books_with_specific_genre == expected_books

    def test_get_books_genre_get_dict(self, collector):
        books = ['Книга_1', 'Книга_2']
        genres = ['Фантастика', 'Ужасы']
        for book in books:
            collector.add_new_book(name=book)
        for book, genre in [(books[0], genres[0]), (books[1], genres[1])]:
            collector.set_book_genre(name=book, genre=genre)
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_get_list(self, collector):
        books = ['Книга_1', 'Книга_2', 'Книга_3']
        genres = ['Фантастика', 'Ужасы']
        for book in books:
            collector.add_new_book(name=book)
        for book, genre in [(books[0], genres[0]), (books[1], genres[0]), (books[2], genres[1])]:
            collector.set_book_genre(name=book, genre=genre)
        books_for_children = collector.get_books_for_children()
        expected_books = ['Книга_1', 'Книга_2']
        assert books_for_children == expected_books

    def test_add_book_in_favorites_add_book(self, collector):
        book_name = 'Книга_1'
        collector.add_new_book(name=book_name)
        collector.add_book_in_favorites(name=book_name)
        assert collector.favorites == [book_name]

    def test_delete_book_from_favorites_delete_book(self, collector):
        book_name = 'Книга_1'
        collector.add_new_book(name=book_name)
        collector.add_book_in_favorites(name=book_name)
        #делаем проверку что бы удостовериться, что книга добавилась в лист
        assert collector.favorites == [book_name]
        collector.delete_book_from_favorites(book_name)
        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_list(self, collector):
        books = ['Книга_1', 'Книга_2', 'Книга_3']
        books_to_favorite = ['Книга_1', 'Книга_2']

        for book in books:
            collector.add_new_book(name=book)
        for book in books_to_favorite:
            collector.add_book_in_favorites(name=book)

        list_of_favorites = collector.get_list_of_favorites_books()
        assert list_of_favorites == books_to_favorite


