from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        self._check_service_type(service_type)

        new_service = self._create_service(service_type, name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        self._check_robot_type(robot_type)

        new_robot = self._create_robot(robot_type, name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._find_obj_by_name(robot_name, self.robots)
        service = self._find_obj_by_name(service_name, self.services)

        if robot.POSSIBLE_SERVICE != service.__class__.__name__:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._find_obj_by_name(service_name, self.services)
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        r = robot[0]
        service.robots.remove(r)
        self.robots.append(r)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._find_obj_by_name(service_name, self.services)
        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self._find_obj_by_name(service_name, self.services)
        total = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {total:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])

    def _check_service_type(self, service_type):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

    def _check_robot_type(self, robot_type):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

    def _create_service(self, service_type, name):
        return self.SERVICE_TYPES[service_type](name)

    def _create_robot(self, robot_type, name, kind, price):
        return self.ROBOT_TYPES[robot_type](name, kind, price)

    @staticmethod
    def _find_obj_by_name(name, collection):
        return [obj for obj in collection if obj.name == name][0]