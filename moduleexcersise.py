import pytz
import datetime

timezones = {
    "India"    : "Asia/Kolkata",
    "USA"      : "America/New_York",
    "UK"       : "Europe/London",
    "Dubai"    : "Asia/Dubai",
    "Singapore": "Asia/Singapore",
    "Sweden"   : "Europe/Stockholm"
}

for country, tz in timezones.items():
    zone = pytz.timezone(tz)
    time = datetime.datetime.now(zone)
    print(country, ":", time.strftime("%d-%m-%Y %H:%M:%S"))