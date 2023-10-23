import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "14281524"))
API_HASH = getenv("API_HASH", "1a2e3f00651f595c53c36140abc5d0c9")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5963562690:AAGwIoleDCYsC3EtamtsMBLcY0Jvo63U68Y")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001603822916"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6079943111))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/YumiXBot/AloneXMusicVps",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneXBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AlonesHeaven")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQCzTb8ADkBQrhF5L4gIukHk8gNml3THaG3rIa4x1Z6N6IB4PcwDurUPGOf3DiHQ3pJ8crbVZanmxmPXZFoFNtkhvPz6nfa793epjfcsRtZyrNvTIr4dAru9cBZbw271hbyLONgeKPwOFJN-qwGu5XtAzm8a94DHjLAEjP2U8EsW_nL4Jv2gZe3d52spMyvi1HRYT1cwu4K6_r6h4ajMNXTY1YxFFvvIIghoIgj6vmdGoTaE3GTep-18OVIo62_sT5-7BnKbEJtBWY-EyGc6XqUb4KmStREjfdyZ0Q3WmGKYgYlKoi5-tOuqSHQeS0Je0pgH1FNB4ClStPDZOPMj3BtXoeyQ1AAAAABqwr10AA")
STRING2 = getenv("STRING_SESSION2", "BQG7300APGWKT69WHV13G-VqcnX81GTBg-6HrHM7DXRp1mwCUblF5avEHq8FgfTd2N-ESklKbilrpINeq8QeK7q0nmzpvnHj1ODymUydwq-sIIKC9ZBE8mo6Kji3NYg-0CoimBqUJiycbYKiW-Q0H3JFpx3_27ERVWtZh4_y_to8BRJUgo3XQX1ISI0CcdQStWkYTjMR0WbOBQ_EuxBUgPi-2eC4OldCfNZAF_bBfY1061jW8Vfnu9lNApl_JgsmZ4h4VUaM2q9YJ0wmGKdIhUjS5QbtUSECGcLv41q2RttFGNkaKREEba4u_LMekNceUo_X7f8bAsbzcuiPBOQRvKkszr7KRAAAAAFvHw8EAA")
STRING3 = getenv("STRING_SESSION3", "BQDZ6zQABmjisBCXKlF-OPUJ5KU_ZrEr5nDuLdmKoIydYOcDeG62SOPmTyaBB5hISaKiPxvhdSCsQKlTrozdgP1lv81_RjpIwEAcTYJS-WFBxSfKdnS-cBp9rFqi4qf_GJBQtrfl_9ycis45ZNT0CKloPTzGY26yEj4fhB5G0JWaDMydW8MsdnonBxOeOtxWv6SGwAIksZEt9vGC559ILZdYZ9zcfVzrGjGFgmJcKlv1I-LxI8ojO1cJ_xAY1IzkFvoBi63a-lNI8Z4hHY0JFKsDbbsg06OUjNkY4CKzuQxKFj0bX4bpXCdQ549VQHJnU88eVdYCtQbWDMCNSYOKDMk1zr4w7AAAAAFbFbFxAA")
STRING4 = getenv("STRING_SESSION4", "BQFnEL8AcXyiMbtbbhNxlgXCrPky0UMDaEfyKwVFe5Cpu_baLEq6hoOuvhGCA_6HvsA4nc5EFvOtY2sJ-HYfKoPRi1cS5qjCu4iXfnD8S-QaR-SQ7EiOl8iOrP4jCbfaxkwLSqTF9vUaogcxaO0-eaht7q_O25EG3SsxAZrfIh5wPCIq5UyoauW4b_EfJawLg2E8EvlgoabsBuR1NRuWM1CmxImbmJ8t9U5b64kgUF46A1TMdal1Jv5OJr2OMjBg449M-SiqqU0CvN2K5q3D6Ua-rDdYTVL4b0bRFOJKg0hTfjHLapE3v9o4IQV30zHcpGYL9vnYjvK49e7FUDhpLZDWn-fgAAAAFTXiDAAA")
STRING5 = getenv("STRING_SESSION5", "BQG_fLUAg7Ccll2FsEjofbKqdtfTReaBWJ6trnKld5rBTqwhPEe1aEqRzlSlqE6Q6MUZHxqHCFsHAdOD-WnpfqbsPY9W22zhFr2hTNkFJfPexJT-POpm_ErycbaOZX_GP3NM-G7mptgaC4v69Em2OkqozKMXtrQDEWNdmXxk47ZT5hFVDtYh5XYNkW32IdhGg1_QsRjqkqIHBER3776R3hyy3VIIdzeWTOoMs6RaPGaRJ4qkJAPbiW9dU6ADi_nwNblgdwyEKtkU26QiFt6qT9VSCGEy-zhqK5ZgpzyPaZ8ICoxE73_IOzxmnBih-BTB1d_VOOP2LnLkggIhz8Ba9ue41Yv-nAAAAAFxrqGiAA")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/d5a15d51e5b21c19f1ff3.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
