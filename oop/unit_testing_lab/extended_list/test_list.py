from unittest import TestCase, main

from unit_testing_lab.extended_list.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(12, 10, 12, 54)

    def test_add_returns_list_with_added_element(self):

        self.expected_list = [12, 10, 12, 54, 20]
        self.integer_list.add(20)
        updated_list = self.integer_list.get_data()
        self.assertEqual(self.expected_list, updated_list)

    def test_add_element_is_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add("not a number")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_returns_correct_element(self):
        self.expected_element = self.integer_list.remove_index(1)
        self.assertEqual([12, 12, 54], self.integer_list.get_data())
        self.assertEqual(10, self.expected_element)

    def test_remove_index_in_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(25)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_returns_correct_element(self):
        self.expected_element = self.integer_list.get(0)
        self.assertEqual(12, self.expected_element)
        self.assertEqual(12, self.integer_list.get(0))

    def test_get_index_is_in_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(25)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_element_is_inserted_at_correct_index(self):
        self.expected_list = [10, 12, 10, 12, 54]
        self.integer_list.insert(0, 10)
        self.assertEqual(self.expected_list, self.integer_list.get_data())

    def test_insert_element_is_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(0, "not an integer")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_index_is_in_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(24, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_biggest_returns_biggest_integer(self):
        self.assertEqual(54, self.integer_list.get_biggest())

    def test_get_index_returns_correct_element(self):
        self.assertEqual(1, self.integer_list.get_index(10))

if __name__ == "__main__":
    main()