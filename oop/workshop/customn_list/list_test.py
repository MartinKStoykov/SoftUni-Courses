from workshop.customn_list.custom_list import CustomList
from unittest import TestCase, main

class TestList(TestCase):
    def setUp(self):
        self.curr_list = CustomList(98989, 99.42, "abs", True)


    def test_initialization(self):
        self.assertEqual([98989, 99.42, "abs", True], self.curr_list)

    def test_append_adds_value_at_end_of_list(self):
        self.curr_list.append("abc")
        self.assertEqual([98989, 99.42, "abs", True, "abc"], self.curr_list())

    def test_remove_removes_element_at_index(self):
        self.assertEqual("abs", self.curr_list.remove(2))
        self.assertEqual([98989, 99.42, True], self.curr_list())
        with self.assertRaises(IndexError) as ie:
            self.curr_list.remove(5)
        self.assertEqual("Index 5 does not exist.", str(ie.exception))

    def test_get_returns_correct_element(self):
        self.assertEqual("abs", self.curr_list.get(2))
        with self.assertRaises(IndexError) as ie:
            self.curr_list.remove(5)
        self.assertEqual("Index 5 does not exist.", str(ie.exception))

    def test_extend_returns_extended_list(self):
        self.assertEqual([98989, 99.42, "abs", True, 25, 10, 200], self.curr_list.extend([25, 10, 200]))

    def test_insert_returns_new_list_and_error(self):
        self.assertEqual([98989, 99.42, 21, True], self.curr_list.insert(2, 21))
        with self.assertRaises(IndexError) as ie:
            self.curr_list.remove(5)
        self.assertEqual("Index 5 does not exist.", str(ie.exception))

    def test_pop_removes_last_element_and_returns_it(self):
        self.assertEqual(True, self.curr_list.pop())
        self.assertEqual([98989, 99.42, "abs"], self.curr_list())

    def test_clear_makes_list_empty(self):
        self.assertEqual(None, self.curr_list.clear())

    def test_index_element_at_correct_index(self):
        self.assertEqual(2, self.curr_list.index("abs"))

    def test_count_returns_correct_count_of_inputted_value(self):
        self.curr_list = [98989, "abs", 99.42, "abs", "abs", True]
        self.assertEqual(3, self.curr_list.count("abs"))

    def test_reverse_returns_reversed_list(self):
        self.assertEqual([True, "abs", 99.42, 98989], self.curr_list.reverse())

    def test_copy_returns_copied_list(self):
        copied_list = self.curr_list.copy()
        self.curr_list = ["abs"]
        self.assertEqual([98989, 99.42, "abs", True], copied_list)

    def test_size_returns_correct_size_of_list(self):
        self.assertEqual(4, self.curr_list.size())

    def test_add_first_adds_element_at_first_index(self):
        self.curr_list.add_first("test")
        self.assertEqual(["test", 98989, 99.42, "abs", True], self.curr_list())

    def test_dictionalize_returns_dict_with_correct_elements(self):
        self.assertEqual({98989: 99.42, "abs": True}, self.curr_list.dictionalize())
        self.curr_list.append(123)
        self.assertEqual({98989: 99.42, "abs": True, 123: " "}, self.curr_list.dictionalize())
        self.assertEqual([98989, 99.42, "abs", True, 123], self.curr_list())

    def test_move_moves_correctly_the_specified_elements(self):
        self.assertEqual(["abs", True, 98989, 99.42], self.curr_list.move(2))


    def test_sum_sums_up_elements_correctly_and_returns_the_sum(self):
        self.assertEqual(99092.42, self.curr_list.sum())

    def test_overbound_returns_element_with_highest_value(self):
        self.assertEqual(98989, self.curr_list.overbound())

    def test_underbound_returns_element_with_lowest_value(self):
        self.assertEqual(3, self.curr_list.underboard())
