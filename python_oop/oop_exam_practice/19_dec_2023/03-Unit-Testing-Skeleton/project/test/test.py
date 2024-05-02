from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobotClass(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Head", 100, 100)

    def test_correct_init(self):
        robot = ClimbingRobot("Mountain", "Head", 100, 100)

        self.assertEqual("Mountain", robot.category)
        self.assertEqual("Head", robot.part_type)
        self.assertEqual(100, robot.capacity)
        self.assertEqual(100, robot.memory)
        self.assertEqual([], robot.installed_software)

    def test_category_setter_not_in_allowed_categories(self):
        allowed_categories = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Test category"

        self.assertEqual(f"Category should be one of {allowed_categories}", str(ve.exception))

    def test_category_setter_with_valid_category(self):
        allowed_categories = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        for category in allowed_categories:
            with self.subTest(category=category):
                self.robot.category = category
                self.assertEqual(self.robot.category, category)

    def test_getting_the_correct_used_capacity_empty_software_list(self):
        self.assertEqual(0, self.robot.get_used_memory())

    def test_getting_the_correct_used_capacity_some_software_installed(self):
        software_1 = {"name": "Test_software 1", "capacity_consumption": 20, "memory_consumption": 20}
        software_2 = {"name": "Test_software 2", "capacity_consumption": 30, "memory_consumption": 30}

        self.robot.installed_software = [software_1, software_2]

        self.assertEqual(50, self.robot.get_used_capacity())

    def test_getting_the_correct_available_capacity_some_software_installed(self):
        software_1 = {"name": "Test_software 1", "capacity_consumption": 20, "memory_consumption": 20}
        software_2 = {"name": "Test_software 2", "capacity_consumption": 30, "memory_consumption": 30}

        self.robot.installed_software = [software_1, software_2]

        self.assertEqual(50, self.robot.get_available_capacity())

    def test_getting_the_correct_used_memory_some_software_installed(self):
        software_1 = {"name": "Test_software 1", "capacity_consumption": 20, "memory_consumption": 20}
        software_2 = {"name": "Test_software 2", "capacity_consumption": 30, "memory_consumption": 30}

        self.robot.installed_software = [software_1, software_2]

        self.assertEqual(50, self.robot.get_used_memory())

    def test_getting_the_correct_available_memory_some_software_installed(self):
        software_1 = {"name": "Test_software 1", "capacity_consumption": 20, "memory_consumption": 20}
        software_2 = {"name": "Test_software 2", "capacity_consumption": 30, "memory_consumption": 30}

        self.robot.installed_software = [software_1, software_2]

        self.assertEqual(50, self.robot.get_available_memory())

    def test_installing_software_when_all_requirements_are_met(self):
        software_1 = {"name": "Test_software 1", "capacity_consumption": 20, "memory_consumption": 20}
        result = self.robot.install_software(software_1)

        self.assertEqual("Software 'Test_software 1' successfully installed on Mountain part.", result)

    def test_installing_software_success_when_edge_case_memory_capacity(self):
        software_1 = {"name": "Test_software 1", "capacity_consumption": 100, "memory_consumption": 100}
        result = self.robot.install_software(software_1)

        self.assertEqual("Software 'Test_software 1' successfully installed on Mountain part.", result)

    def test_installing_software_when_capacity_exceeds(self):
        software_1 = {"name": "Test_software 1", "capacity_consumption": 120, "memory_consumption": 20}
        result = self.robot.install_software(software_1)

        self.assertEqual("Software 'Test_software 1' cannot be installed on Mountain part.", result)

    def test_installing_software_when_memory_exceeds(self):
        software_1 = {"name": "Test_software 1", "capacity_consumption": 20, "memory_consumption": 120}
        result = self.robot.install_software(software_1)

        self.assertEqual("Software 'Test_software 1' cannot be installed on Mountain part.", result)


if __name__ == "__main__":
    main()
