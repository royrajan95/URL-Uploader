import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5657653415:AAGZ4-b5s1WJH4peHcZFrZlzi25AVHoTZl0")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 5503927))
    API_HASH = os.environ.get("API_HASH", "6f3a051b5da7f5b499cde019d273fca1")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "773325066").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/1efd13f55ef33d64aa2c8.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # LOGGER INFO CHANNEL ID
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001872036502))
    # Give Admin id in this field 
    LAZY_DEVELOPER = set(int(x) for x in os.environ.get("LAZY_ADMIN", "773325066").split())
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 40960
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""


    
