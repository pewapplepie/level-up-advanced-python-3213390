# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open("10k_racetimes.txt", "rt") as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    races = races.splitlines()
    athelete = "Jennifer Rhines"
    jr_races = [race_info for race_info in races if athelete in race_info]
    jr_times = [info.split()[0] for info in jr_races]
    return jr_times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
    mm:ss:M where :
    m corresponds to a minutes digit
    s corresponds to a seconds digit
    M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    
    def converttime(t):
        t = t.split(':')
        ttl_ms = float(t[0])* 60 * 100 
        ttl_ms += float(t[1])* 100 
        if len(t) > 2:
            ttl_ms += float(t[2])
        return ttl_ms

    ttlms = sum([converttime(tstr) for tstr in racetimes])
    ttlms /= len(racetimes)
    ms_str = str(ttlms%100)[0]
    ttls = ttlms // 100
    min_str = str(int(ttls//60))
    ss_str = str(int(ttls%60))
    return min_str + ":" + ss_str + '.' + ms_str