from project.student import Student
from unittest import TestCase, main

class StudentTest(TestCase):

    def setUp(self):
        self.student = Student("Carl")

    def test_initialization(self):
        self.assertEqual("Carl", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_when_course_already_enrolled(self):
        self.student.courses["math"] = ["testing"]
        self.expected = self.student.enroll("math", ["more testing"])
        self.assertEqual("Course already added. Notes have been updated.", self.expected)
        self.assertEqual({"math": ["testing", "more testing"]}, self.student.courses)

    def test_enroll_when_notes_are_y_or_none(self):
        self.assertEqual("Course and course notes have been added.",
                         self.student.enroll("math", "even more testing", "Y"))
        self.assertEqual("Course and course notes have been added.",
                         self.student.enroll("literature", "and even more testing", ""))
        self.assertEqual({'literature': 'and even more testing', 'math': 'even more testing'}, self.student.courses)

    def test_enroll_when_no_notes(self):
        self.assertEqual("Course has been added.", self.student.enroll("math",
                                                                       "", "no notes"))
        self.assertEqual({'math': []}, self.student.courses)
    def test_add_notes_return_correct_string_if_course_already_enrolled(self):
        self.student.courses["test"] = ["yes, i am testing yet again"]
        self.assertEqual("Notes have been updated", self.student.add_notes("test", "testy"))

    def test_add_notes_if_course_not_enrolled(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("blabla", "blibli")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_already_enrolled(self):
        self.student.courses["test"] = ["yes, i am testing yet again"]
        self.assertEqual("Course has been removed", self.student.leave_course("test"))

    def test_leave_course_if_course_not_enrolled(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("blabla")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    main()