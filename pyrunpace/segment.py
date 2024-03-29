#!/usr/bin/env python3
"""Class segment, for a running segment defined by time and distance."""


from pyrunpace import time


class Segment:
    """class segment, defining a running segment at a given pace."""

    def __init__(self, distance=10, hours=1, minutes=0, seconds=0) -> None:
        """__init__ segment class init.

        Parameters
        ----------
        distance : int, optional
            segment distance, by default 10
        hours : int, optional
            number of hours, by default 1
        minutes : int, optional
            number of minutes , by default 0
        seconds : int, optional
            number of seconds, by default 0
        """
        self.distance = float(distance)
        self.time = int(3600.0 * hours + 60.0 * minutes + seconds)
        # compute integer HMS
        self.__hours = int(hours)
        self.__minutes = int((hours - int(hours)) * 60.0) + int(minutes)
        self.__seconds = int(seconds + (minutes - int(minutes)) * 60.0)
        # compute modulo 60 HMS
        tmp = self.__seconds
        self.__seconds = self.__seconds % 60
        self.__minutes += int(tmp / 60)
        tmp = self.__minutes
        self.__minutes = self.__minutes % 60
        self.__hours += int(tmp / 60)
        # pace in seconds per km
        self.__pace = self.time / self.distance
        # compute modulo 60 HMS
        self.__pace_hours = int(self.__pace / 3600)
        self.__pace_seconds = self.__pace - 3600 * self.__pace_hours
        self.__pace_minutes = int(self.__pace_seconds / 60)
        self.__pace_seconds -= 60 * self.__pace_minutes

        self.__speed_kmh = 1.0 / float(self.__pace / 3600.0)

    def __setattr__(self, name, value) -> None:
        """__setattr__ set attributes.

        Parameters
        ----------
        name : _type_
            _description_
        value : _type_
            _description_
        """
        self.__dict__[name] = value

    def __add__(self, other) -> "Segment":
        if isinstance(other, Segment):
            return self.__class__(
                self.distance + other.distance, self.time + other.time
            )

        raise TypeError("Illegal argument type for built-in operation")

    def __str__(self) -> str:
        """__str__ magic method.

        Returns:
        -------
        str
            _description_
        """
        return str(self.distance)

    def print_info(self) -> None:
        """print_info print information about segment."""
        print(f"\tDistance: {self.distance} km")
        print(f"\tTime: {self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}")
        print(
            f"\tPace: {self.__pace_hours:02d}:{self.__pace_minutes:02d}:{self.__pace_seconds:02f}/km"
        )
        print(f"\tSpeed: {self.__speed_kmh:.2f} km/h")

        print("Time for usual distances")
        print("========================")
        hours, minutes, seconds = time.seconds_to_hms(self.__pace * 42.2)
        print(f"\tTime Marathon: {hours:02d}:{minutes:02d}:{seconds:02d}")

        hours, minutes, seconds = time.seconds_to_hms(self.__pace * 21.1)
        print(f"\tTime Half-Marathon: {hours:02d}:{minutes:02d}:{seconds:02d}")

        hours, minutes, seconds = time.seconds_to_hms(self.__pace * 10)
        print(f"\tTime 10K: {hours:02d}:{minutes:02d}:{seconds:02d}")

        hours, minutes, seconds = time.seconds_to_hms(self.__pace * 5)
        print(f"\tTime 5K: {hours:02d}:{minutes:02d}:{seconds:02d}")
