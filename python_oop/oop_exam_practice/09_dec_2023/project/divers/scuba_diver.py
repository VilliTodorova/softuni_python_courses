from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        reduce_value = int(time_to_catch * 0.3)

        if self.oxygen_level - reduce_value <= 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduce_value

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN
