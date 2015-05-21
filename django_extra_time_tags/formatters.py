# -*- coding: utf-8 -*-


def humanize_minutes(minutes):
    """
    Format a number of minutes into a human-readable string
    """
    if not isinstance(minutes, int):
        minutes = int(minutes)

    if minutes == 0:
        return '0 minutes'

    (hours, minutes) = divmod(minutes, 60)

    duration_string = ''

    if hours:
        duration_string += '{h} hour{s}'.format(
            h=hours,
            s='s' if hours != 1 else '',
        )

    if hours and minutes:
        duration_string += ', '

    if minutes:
        duration_string += '{m} minute{s}'.format(
            m=minutes,
            s='s' if minutes != 1 else '',
        )

    return duration_string
