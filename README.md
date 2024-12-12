# qa_python
1. collector: фикстура создаёт новый экземпляр BooksCollector перед каждым тестом.
2. test_value_books_genre - init. Проверка заполнения дикта books_genre
3. test_add_new_book_add_books_with_wrong_names - проверка невозможности добавить книги с пустым именем и именем больше 40 символов. Метод add_new_book
3. test_set_book_genre_set_genre - проверка добавления существующего жанра книги. Метод set_book_genre
4. test_get_book_genre_get_genre - проверка получения жанра по имени. Метод get_book_genre
5. test_get_books_with_specific_genre_get_genre_list - проверка вывода списка с определенным жанром. Метод get_books_with_specific_genre
6. test_get_books_genre_get_dict - проверка получения словаря books_genre. Метод get_books_genre
7. test_get_books_for_children_get_list - проверка, что в список книг для детей попадают только разрешенные жанры. Метод get_books_for_children
8. test_add_book_in_favorites_add_book - проверка добавления книги в favorites. Метод add_book_in_favorites
9. test_delete_book_from_favorites_delete_book - проверка удаления книги из favorites. Метод delete_book_from_favorites
10. test_get_list_of_favorites_books_get_list - проверка списка книг добавленных в favorites. Метод get_list_of_favorites_books