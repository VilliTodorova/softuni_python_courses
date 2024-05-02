from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [horse.name for horse in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return

        new_horse = None

        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [jockey.name for jockey in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [race.race_type for race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys), None)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = [horse for horse in self.horses if not horse.is_taken][0]

        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        else:
            jockey.horse = horse
            horse.is_taken = True
            return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = [race for race in self.horse_races if race.race_type == race_type][0]

        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys), None)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey.name in [j.name for j in horse_race.jockeys]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = next(filter(lambda x: x.race_type == race_type, self.horse_races), None)

        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winning_jockey = sorted(horse_race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]

        return (f"The winner of the {race_type} race, with a speed of {winning_jockey.horse.speed}km/h is "
                f"{winning_jockey.name}! Winner's horse: {winning_jockey.horse.name}.")
