import numpy as np


def parse_cap(s):
    """Convert the capped scored string into a number,
    e.g. 'CAP+ 123' to 123.0
    """
    try: 
        s2 = s.replace(" ", "").lower()
        return float(s2.split("cap+")[-1])
    except:
        return None


def parse_time(timestr):
    """Convert time string to seconds"""
    try:
        micro = 0.0
        if '.' in timestr:
            timestr, m = timestr.split('.')
            micro = int(m) / 10**len(m)
        tc = timestr.split(':')
        ftr = [3600, 60, 1]
        ftr = ftr[(3 - len(tc)):]
        return float(sum([a*b for a,b in zip(ftr, map(int, tc))]) + micro)
    except:
        return None


def extrap_cap2sec(s, timecap, maxrep):
    """Extrapolate capped score to seconds"""
    reps = parse_cap(s)
    assert maxrep >= reps
    factor = (maxrep / reps)
    # convert TC to seconds
    if isinstance(timecap, (int, float)):
        tcsec = 60 * timecap
    elif isinstance(timecap, str):
        tcsec = parse_time(timecap)
    else:
        raise Exception(f"cannot parse {type(timecap)} format for time cap.")
    # done
    return tcsec * factor
