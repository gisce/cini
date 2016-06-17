# coding=utf-8
try:
    VERSION = __import__('pkg_resources') \
        .get_distribution(__name__).version
except Exception, e:
    VERSION = 'unknown'


def nearest(value, *values):
    """
    Get the nearest value from values
    :param value: value to find
    :param values: list of values to return
    :return: the nearest value from values
    """
    ant_diff = None
    values = sorted(values)
    for idx, v in enumerate(values):
        diff = abs(value - v)
        if diff == 0:
            return v
        elif ant_diff is not None and diff > ant_diff:
                return values[idx - 1]
        ant_diff = diff
    return v
