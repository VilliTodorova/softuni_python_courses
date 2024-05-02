from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {"ElbowPad": ElbowPad, "KneePad": KneePad}
    TEAM_TYPES = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        equipment_obj = self.EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment_obj)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        team_obj = self.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team_obj)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team_obj = self._find_team_by_name(team_name)
        equipment_obj = self._find_last_equipment_by_type(equipment_type)

        if team_obj.budget < equipment_obj.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment_obj)
        team_obj.equipment.append(equipment_obj)
        team_obj.budget -= equipment_obj.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_obj = self._find_team_by_name(team_name)

        if team_obj is None:
            raise Exception("No such team!")

        if team_obj.wins > 0:
            raise Exception(f"The team has {team_obj.wins} wins! Removal is impossible!")

        self.teams.remove(team_obj)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        collection = [eq for eq in self.equipment if eq.EQUIPMENT_TYPE == equipment_type]

        for eq in collection:
            eq.increase_price()

        return f"Successfully changed {len(collection)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = self._find_team_by_name(team_name1)
        team_2 = self._find_team_by_name(team_name2)

        if team_1.TEAM_TYPE != team_2.TEAM_TYPE:
            raise Exception("Game cannot start! Team types mismatch!")

        t1_points = self._calculate_points(team_1)
        t2_points = self._calculate_points(team_2)

        if t1_points > t2_points:
            team_1.win()
            return f"The winner is {team_1.name}."
        elif t1_points < t2_points:
            team_2.win()
            return f"The winner is {team_2.name}."

        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"Tournament: {self.name}\nNumber of Teams: {len(sorted_teams)}\nTeams:"]

        [result.append(t.get_statistics()) for t in sorted_teams]

        return "\n".join(result)

    # helper methods

    def _find_last_equipment_by_type(self, equipment_type):
        collection = [eq for eq in self.equipment if eq.EQUIPMENT_TYPE == equipment_type]
        return collection[-1] if collection else None

    def _find_team_by_name(self, team_name):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None

    @staticmethod
    def _calculate_points(team_obj):
        protection_points = sum([eq.protection for eq in team_obj.equipment])
        total_points = protection_points + team_obj.advantage
        return total_points
