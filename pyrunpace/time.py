def seconds_to_hms(time_s) -> tuple:
    hours = int(time_s / 3600)
    seconds = int(time_s) - 3600 * hours
    minutes = int(seconds / 60)
    seconds -= 60 * minutes

    return (hours, minutes, seconds)
