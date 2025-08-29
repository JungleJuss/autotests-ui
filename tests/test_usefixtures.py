import pytest

@pytest.fixture
def clear_book_database():
    print('[FIXTURE] Удаляем все данные с базы данных')


@pytest.fixture
def fill_book_database():
    print('[FIXTURE] Создаём новые данные в базе данных')

@pytest.mark.usefixtures('fill_book_database')
def test_read_all_books_in_library():
    print("Reading all books")

@pytest.mark.usefixtures(
    "clear_book_database",
    "fill_book_database"
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...


    def test_delete_book_from_library(self):
        ...