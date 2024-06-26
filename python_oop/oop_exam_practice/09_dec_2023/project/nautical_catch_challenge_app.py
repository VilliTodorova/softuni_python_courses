from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        diver = self._find_diver_by_name(diver_name)

        if diver is not None:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self._find_fish_by_name(fish_name)

        if fish is not None:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self._find_diver_by_name(diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self._find_fish_by_name(fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            self._check_oxygen(diver)

            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                self._check_oxygen(diver)

                return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."

            else:
                diver.miss(fish.time_to_catch)
                self._check_oxygen(diver)

                return f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            self._check_oxygen(diver)

            return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."

    def health_recovery(self):
        counter = 0

        for diver in self.divers:
            if diver.has_health_issue:
                counter += 1
                diver.update_health_status()
                diver.renew_oxy()

        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name: str):
        diver = self._find_diver_by_name(diver_name)
        fish_details = [fish.fish_details() for fish in diver.catch]

        catch_report = '\n'.join(fish_details)
        return f"**{diver_name} Catch Report**\n{catch_report}"

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))

        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in sorted_divers)

        return result

    #   helper methods

    def _find_diver_by_name(self, diver_name):
        diver = [d for d in self.divers if d.name == diver_name]

        return diver[0] if diver else None

    def _find_fish_by_name(self, fish_name):
        fish = [f for f in self.fish_list if f.name == fish_name]

        return fish[0] if fish else None

    @staticmethod
    def _check_oxygen(diver):
        if diver.oxygen_level == 0:
            diver.update_health_status()
