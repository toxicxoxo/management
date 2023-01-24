import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "18701068")
    API_HASH = getenv("API_HASH", "10f119750c7feed4716d1fda45824b8b")
    TOKEN = getenv("TOKEN", "5587629345:AAElIc-a3f3qqkrcm6D67HuDPDMEsorXkuQ")
    OWNER_ID = getenv("OWNER_ID", "5001113788")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "5001113788")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOK4Bu337M6pCef0iRg9JpYfPYreLAmxINz-8JhYXPH_AuN51fpv_19CkxaPSbQ5WzfYIp0Rrz1xyqo03kaOP7bysqFTQ5aZb_aMy0X1d5GSvpU4-9Em8LjwllnGbULgAyTluu8gxDd5tHIqzOo1vkEF5KwwNVcxsV78-uUrRycar-uA4ShVMsXSoC667IhD0LWh7b6UwdEl3YDaaDNS33zbusuxCkqbPHi7oa4bI8-xF5f_e71lcjzkj79L_jGfIcVZ74fCMZEmEFcwxibyrnnBsMyOGpuLx6VRkgPosHFYmJa5f0VDGCv0Ur6GE8A5GmLzG5LN_d1Jq1yjCn_vR0kJf2Z8=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "@HOMIESASSITANT")
    DB_URI = getenv("DATABASE_URL", "postgres://iemqmhee:fCgaio3Y47y1pxzKvPiVXc5xKhpHCqUw@kashin.db.elephantsql.com/iemqmhee
")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001658805766")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001658805766")
    SYS_ADMIN = getenv("SYS_ADMIN", "5001113788")
    DEV_USERS = getenv("DEV_USERS", "5001113788")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "real_homie")
    SUPPORT = getenv("SUPPORT", "real_homies")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/1dfada489528335e50d1c.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    CASH_API_KEY = getenv("CASH_API_KEY", "1KR9XZG9FFY32G1Y")
    TIME_API_KEY = getenv("TIME_API_KEY", "E0TMC1W407Y9")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "tZQXWW~atAVRKRxEsXKIvSDDK48zDPVetytIkgfk9KH6quNH~whEKhbU9MYUDmGo")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "2ba276e5c3a8515a66d4e9d106f7cb57")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5001113788").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "5001113788").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
