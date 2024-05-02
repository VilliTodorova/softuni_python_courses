class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f"{'' if self.hours > 9 else '0'}{self.hours}:" \
               f"{'' if self.minutes > 9 else '0'}{self.minutes}:" \
               f"{'' if self.seconds > 9 else '0'}{self.seconds}"

    def next_second(self) -> str:
        if self.seconds + 1 > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_seconds:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        else:
            self.seconds += 1

        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
