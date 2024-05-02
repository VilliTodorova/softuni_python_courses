from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_PEAK_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}
    VALID_CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        climber = self._get_climber_by_name(climber_name)
        if climber is not None:
            return f"{climber_name} has been already registered."

        climber_obj = self.VALID_CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(climber_obj)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        peak_obj = self.VALID_PEAK_TYPES[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak_obj)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        peak = self._get_peak_by_name(peak_name)
        climber = self._get_climber_by_name(climber_name)

        required_gear = set(peak.get_recommended_gear())
        missing_gear = required_gear - set(gear)

        if missing_gear:
            climber.is_prepared = False
            sorted_missing_gear = sorted(missing_gear)
            return f"{climber_name} is not prepared to climb {peak_name}. " \
                   f"Missing gear: {', '.join(sorted_missing_gear)}."
        else:
            return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._get_climber_by_name(climber_name)
        peak = self._get_peak_by_name(peak_name)

        if climber is None:
            return f"Climber {climber_name} is not registered yet."

        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda climber: (-len(climber.conquered_peaks), climber.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        result.append(climber_statistics)

        return '\n'.join(result)

    #   helper methods

    def _get_climber_by_name(self, climber_name):
        climber = [c for c in self.climbers if c.name == climber_name]

        return climber[0] if climber else None

    def _get_peak_by_name(self, peak_name):
        peak = [p for p in self.peaks if p.name == peak_name]

        return peak[0] if peak else None
