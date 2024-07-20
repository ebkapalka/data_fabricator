from datetime import datetime


def timestamp(dt_obj: datetime = None, fmt="%Y%m%d"):
    """
    Returns a timestamp string in the format specified by fmt.
    :param dt_obj: optional datetime object to use for the timestamp
    :param fmt: optional format string for the timestamp
    :return: current or provided datetime object as a formatted string
    """
    if dt_obj is None:
        dt_obj = datetime.now()
    return dt_obj.strftime(fmt)
