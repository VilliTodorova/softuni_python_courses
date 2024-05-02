from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BUDGET = 1000.0
    WIN_INCREMENT = 115
    TEAM_TYPE = "OutdoorTeam"

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.advantage += self.WIN_INCREMENT
        self.wins += 1
