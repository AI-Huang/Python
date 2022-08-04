#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Apr-07-20 20:04
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)

from datetime import datetime
import pytz


def main():
    CONFIG = {
        778783472: {"daytime": (0, 23)},  # all day long
        628351018: {"daytime": (9, 23)}  # day time
    }

    conf = CONFIG[778783472]["daytime"]
    local_now = datetime.now(pytz.timezone("Asia/Shanghai"))
    print(local_now)
    print(conf)
    print(local_now.hour in range(conf[0], conf[1] + 1))
    # for tz in pytz.all_timezones:
    #     if "Asia" in tz:
    #         print(tz)
    TIME_ZONE = {"北京": "Asia/Shanghai",
                 "东京": "Asia/Tokyo",
                 "纽约": "America/New_York"}
    for tz_name, time_zone in TIME_ZONE.items():
        print(tz_name)
        now = datetime.now(pytz.timezone(time_zone))
        print(now)


if __name__ == "__main__":
    main()
