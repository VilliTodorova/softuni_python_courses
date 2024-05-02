from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    MUSICIAN_NAMES = []
    BAND_NAMES = []

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if name in self.MUSICIAN_NAMES:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        self.MUSICIAN_NAMES.append(name)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in self.BAND_NAMES:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        self.BAND_NAMES.append(name)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_musician_by_name(musician_name)
        band = self._find_band_by_name(band_name)
        band.add_member(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._find_band_by_name(band_name)
        musician = self.__find_added_to_band_musician_by_name(band, musician_name)

        band.remove_member(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._find_band_by_name(band_name)
        concert = self._find_concert_by_place(concert_place)

        for musician_type in self.VALID_MUSICIAN_TYPES:
            if not any(
                filter(
                    lambda x: x.__class__.__name__ == musician_type,
                    band.members
                )
            ):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            result = self._validate_rock_concert(band, concert)
        elif concert.genre == "Metal":
            result = self._validate_metal_concert(band, concert)
        elif concert.genre == "Jazz":
            result = self._validate_jazz_concert(band, concert)

        return result

    #   helper methods

    def _find_musician_by_name(self, name):
        for musician in self.musicians:
            if name == musician.name:
                return musician
        else:
            raise Exception(f"{name} isn't a musician!")

    def _find_band_by_name(self, name):
        for band in self.bands:
            if name == band.name:
                return band
        else:
            raise Exception(f"{name} isn't a band!")

    def _find_concert_by_place(self, place):
        for concert in self.concerts:
            if place == concert.place:
                return concert

    @staticmethod
    def __find_added_to_band_musician_by_name(band, name: str):
        for musician in band.members:
            if musician.name == name:
                return musician
        else:
            raise Exception(f"{name} isn't a member of {band.name}!")

    @staticmethod
    def _validate_rock_concert(band, concert):
        for band_member in band.members:
            if band_member.__class__.__name__ == 'Drummer' and \
                    "play the drums with drumsticks" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

    @staticmethod
    def _validate_metal_concert(band, concert):
        for band_member in band.members:
            if band_member.__class__.__name__ == 'Drummer' and \
                    "play the drums with drumsticks" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

    @staticmethod
    def _validate_jazz_concert(band, concert):
        for band_member in band.members:
            if band_member.__class__.__name__ == 'Drummer' and \
                    "play the drums with brushes" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills \
                    and "sing high pitch notes" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
