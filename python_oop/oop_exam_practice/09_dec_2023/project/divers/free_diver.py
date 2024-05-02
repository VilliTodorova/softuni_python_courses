from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN = 120

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        reduce_value = int(time_to_catch * 0.6)

        if self.oxygen_level - reduce_value <= 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduce_value

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN
