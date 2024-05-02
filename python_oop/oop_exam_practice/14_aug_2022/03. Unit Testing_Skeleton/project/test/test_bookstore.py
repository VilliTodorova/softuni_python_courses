from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):

    def setUp(self):
        self.store = Bookstore(
            10
        )

    def test_correct_init(self):
        self.store.availability_in_store_by_book_titles = {"Harry Potter": 5}

        self.assertEqual(10, self.store.books_limit)
        self.assertEqual({"Harry Potter": 5}, self.store.availability_in_store_by_book_titles)

        self.store.sell_book("Harry Potter", 2)
        self.assertEqual(2, self.store.total_sold_books)

    def test_limit_setter_zero_limit(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        expected = "Books limit of 0 is not valid"

        self.assertEqual(expected, str(ve.exception))

    def test_limit_setter_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = -2

        expected = "Books limit of -2 is not valid"

        self.assertEqual(expected, str(ve.exception))

    def test_len_method_correctly_increments_and_returns_count(self):
        self.store.availability_in_store_by_book_titles = {"Harry Potter": 5}
        result = len(self.store)
        expected = 5

        self.assertEqual(expected, result)

    def test_receiving_books_over_limit_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Harry Potter", 11)

        expected = "Books limit is reached. Cannot receive more books!"

        self.assertEqual(expected, str(ex.exception))

    def test_receiving_books_adding_new_title(self):
        result = self.store.receive_book("Harry Potter", 5)
        expected = "5 copies of Harry Potter are available in the bookstore."

        self.assertEqual(expected, result)

        self.assertEqual(5, len(self.store))

    def test_receiving_books_adding_more_copies_existing_title(self):
        self.store.availability_in_store_by_book_titles = {"Harry Potter": 2}

        result = self.store.receive_book("Harry Potter", 8)
        expected = "10 copies of Harry Potter are available in the bookstore."

        self.assertEqual(expected, result)

        self.assertEqual(10, len(self.store))

    def test_selling_a_book_not_available_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Harry Potter", 1)
        expected = "Book Harry Potter doesn't exist!"

        self.assertEqual(expected, str(ex.exception))

    def test_selling_more_copies_than_available_raises_ex(self):
        self.store.availability_in_store_by_book_titles = {"Harry Potter": 2}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Harry Potter", 3)

        expected = "Harry Potter has not enough copies to sell. Left: 2"

        self.assertEqual(expected, str(ex.exception))

    def test_successful_sale(self):
        self.store.availability_in_store_by_book_titles = {"Harry Potter": 2}
        result = self.store.sell_book("Harry Potter", 1)
        expected = "Sold 1 copies of Harry Potter"

        self.assertEqual(expected, result)

    def test_str_method(self):
        self.store.availability_in_store_by_book_titles = {"Harry Potter": 10}
        self.store.sell_book("Harry Potter", 10)
        result = str(self.store)
        expected = "Total sold books: 10\nCurrent availability: 0\n - Harry Potter: 0 copies"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
