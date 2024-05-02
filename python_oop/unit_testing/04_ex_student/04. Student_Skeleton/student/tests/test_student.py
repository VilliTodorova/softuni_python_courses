from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student(
            "test1",
            {},
        )
        self.student_enrolled_courses = Student(
            "test2",
            {"Maths": ["1 + 2 = 3"]}
        )

    def test_correct_init(self):
        self.assertEqual("test1", self.student.name)
        self.assertEqual({}, self.student.courses)

        self.assertEqual("test2", self.student_enrolled_courses.name)
        self.assertEqual({"Maths": ["1 + 2 = 3"]}, self.student_enrolled_courses.courses)

    def test_enrolling_course_already_in_updating_notes(self):
        result = self.student_enrolled_courses.enroll("Maths", ["2 + 2 = 4"])
        expected = "Course already added. Notes have been updated."

        self.assertEqual(expected, result)

        self.assertEqual(["1 + 2 = 3", "2 + 2 = 4"], self.student_enrolled_courses.courses["Maths"])

    def test_enrolling_no_such_course_yet_no_third_parameter(self):
        result = self.student.enroll("Maths", ["1 + 2 = 3"])
        expected = "Course and course notes have been added."

        self.assertEqual(expected, result)

        self.assertEqual(["1 + 2 = 3"], self.student.courses["Maths"])

    def test_enrolling_no_such_course_yet_third_parameter_y(self):
        result = self.student.enroll("Maths", ["1 + 2 = 3"], "Y")
        expected = "Course and course notes have been added."

        self.assertEqual(expected, result)

        self.assertEqual(["1 + 2 = 3"], self.student.courses["Maths"])

    def test_enrolling_no_such_course_yet_third_parameter_n(self):
        result = self.student.enroll("Maths", ["1 + 2 = 3"], "N")
        expected = "Course has been added."

        self.assertEqual(expected, result)

        self.assertEqual([], self.student.courses["Maths"])

    def test_adding_notes_no_such_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Maths", ["1 + 2 = 3"])

        expected = "Cannot add notes. Course not found."

        self.assertEqual(expected, str(ex.exception))

    def test_adding_notes_correctly(self):
        expected = "Notes have been updated"
        result = self.student_enrolled_courses.add_notes("Maths", ["2 + 2 = 4"])

        self.assertEqual(expected, result)

    def test_leaving_course_no_such_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Maths")

        expected = "Cannot remove course. Course not found."

        self.assertEqual(expected, str(ex.exception))

    def test_leaving_course_correctly(self):
        expected = "Course has been removed"
        result = self.student_enrolled_courses.leave_course("Maths")

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()