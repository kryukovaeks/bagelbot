import os
from datetime import timedelta

EMAIL_DOMAIN = "ekaterina.kryukova@epfl.ch"
SLACK_TOKEN = "xoxb-2046293016928-2007760046679-sDmnN4i3VMUt1BDfI5ydJRJ0"
SLACK_CHANNEL = "#general"
SHELVE_FILE = "meetings.shelve"
ATTENDANCE_TIME_LIMIT = 60 * 15
PAIRING_SIZE = 2
GOOGLE_HANGOUT_URL = "https://hangouts.google.com/hangouts/_/"
S3_BUCKET = None
S3_PREFIX = None
FREQUENCY = timedelta(days=14)
TIMEZONE = "Europe/Moscow"
ATTENDANCE_TIME = {"hour": 11, "minute": 28, "weekday": 0}
MEETING_TIME = {"hour": 14, "minute": 29, "weekday": 0}

if os.path.exists("config_private.py"):
    # Use config_private for your own personal settings - default to be git ignored.
    # Yup, intentionally using wildcard import to shadow the default values
    from config_private import *
# hi
