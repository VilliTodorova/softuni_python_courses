from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    BUDGET = 500.0
    WIN_INCREMENT = 145
    TEAM_TYPE = "IndoorTeam"

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.advantage += self.WIN_INCREMENT
        self.wins += 1
