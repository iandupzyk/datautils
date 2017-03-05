import time
import calendar

DATEINTFORMAT = "%Y%m%d"
HOURINTFORMAT = "%Y%m%d%H"

class datetime(object) :
    def __init__(self, dt) :
        pass

def epoch(ms=False) :
    """
    Return the current number of seconds from the epoch (1970-01-01 00:00:00)
    If ms is specified to be True, then the epoch returned is in milliseconds
    """
    if ms :
        return int(time.time()*1000)
    else :
        return int(time.time())

def dateint() :
    """
    Returns the current dateint in the format YYYYMMDD
    """
    e = epoch()
    return epochToDateint(e)

def hourint() :
    """
    Returns the current hourint in the format YYYYMMDDHH
    """
    e = epoch()
    return epochToHourint(e)

def epochToDateint(ts, ms=False) :
    """
    Convert an epoch to dateint format.
    If ms is specified to be True, then the epoch is assumed to be in milliseconds
    """

    if ms :
        dt = dt / 1000

    dt = time.gmtime(ts)
    return int(time.strftime(DATEINTFORMAT, dt))

def epochToHourint(ts, ms=False) :
    """
    Convert an epoch to hourint format.
    If ms is specified to be True, then the epoch is assumed to be in milliseconds
    """

    if ms :
        dt = dt / 1000

    dt = time.gmtime(ts)
    return int(time.strftime(HOURINTFORMAT, dt))
