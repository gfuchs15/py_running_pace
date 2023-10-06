"""time module."""


def seconds_to_hms(time_s: float) -> tuple:
    """seconds_to_hms converts time in second to hours:minutes:seconds format.

    Parameters
    ----------
    time_s : float
        time in seconds

    Returns:
    -------
    tuple
        hours, miniutes, seconds format
    """
    hours = int(time_s / 3600)
    seconds = int(time_s) - 3600 * hours
    minutes = int(seconds / 60)
    seconds -= 60 * minutes

    return (hours, minutes, seconds)
