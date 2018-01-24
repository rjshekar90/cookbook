from datetime import datetime

def parse_ymd(s):
    year_s, mon_s, day_s, hour_s, min_s, sec_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s), int(), int(hour_s), int(min_s), int(sec_s))

print(parse_ymd('2017-1-12-12-00-00'))