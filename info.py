import re
from os import environ
from Script import script 

# ============== REGEX PATTERN ==============

id_pattern = re.compile(r'^.\d+$')

# ============== BOT INFORMATION ==============

SESSION = environ.get('SESSION', 'MyselfNeon')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# ============== START MESSAGE PICTURES ==============

# (Add Multiple By Giving One Space Between Each)
PICS = (environ.get('PICS', 'https://files.catbox.moe/ybg6gw.jpg https://files.catbox.moe/b5a3dz.jpg https://files.catbox.moe/n0xw7h.jpg https://files.catbox.moe/fhexii.jpg https://files.catbox.moe/v7w8co.jpg https://files.catbox.moe/r946bu.jpg')).split()

# ============== ADMINS & USERS ==============

ADMINS = [int(admin) if id_pattern.search(admin) else admin
          for admin in environ.get('ADMINS', '841851780').split()]  # Multiple IDs separated by space

auth_users = [int(user) if id_pattern.search(user) else user
              for user in environ.get('AUTH_USERS', '').split()]  # Multiple IDs separated by space

AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# ============== CHANNELS & GROUPS ==============

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001889915480'))

CHANNELS = [int(ch) if id_pattern.search(ch) else ch
            for ch in environ.get('CHANNELS', '-1002627138181 -1002487845241').split()]

REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False))  # True → request to join FSUB
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False))                # Retry button for FSUB

# Force Subscribe Channel
auth_channel = environ.get('AUTH_CHANNEL', '-1002384933640')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# File request channel
reqst_channel = environ.get('REQST_CHANNEL', '-1002158258466')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None

# Index request channel
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

# Bot support group
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# File store channel (/batch command)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002487845241')).split()]

# Delete channel(s)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch
                   for dch in environ.get('DELETE_CHANNELS', '-1002231967338').split()]

# ============== DATABASE ==============

DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "MyselfNeon")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'neoncollection')

MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', False))

# Separate DBs if MULTIPLE_DATABASE = True
O_DB_URI = environ.get('O_DB_URI', "")
F_DB_URI = environ.get('F_DB_URI', "")
S_DB_URI = environ.get('S_DB_URI', "")

if not MULTIPLE_DATABASE:
    USER_DB_URI = OTHER_DB_URI = FILE_DB_URI = SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = O_DB_URI
    FILE_DB_URI = F_DB_URI
    SEC_FILE_DB_URI = S_DB_URI

# ============== Premium and REFERAL  ==============

# Premium And Referal Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If Flase Then No Need To Fill.
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True))

REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '5'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://files.catbox.moe/tc8drk.jpg')
PAYMENT_TEXT = environ.get(
    'PAYMENT_TEXT',
    '<b><blockquote>‣ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐏𝐋𝐀𝐍𝐒 📝</blockquote>\n'
    '<i>• 30Rs - 01 Week\n• 50Rs - 01 Month\n• 120Rs - 03 Months\n• 220Rs - 06 Months</i>\n\n'
    '<blockquote>‣ 𝐏𝐋𝐀𝐍 𝐁𝐄𝐍𝐄𝐅𝐈𝐓𝐒 ✨</blockquote>\n'
    '<i>• No Need To Verify\n• No Need To Open Links\n• Direct Files\n• Ad-Free Experience\n'
    '• High Speed Download\n• Multiplayer Streaming Links\n• Unlimited Movies, Animes & Series\n'
    '• 24×7 Admin Support\n• Requests Will Be Completed Within 01 Hour Of Submission If Available</i>\n\n'
    '<blockquote>‣ 𝐔𝐏𝐈 𝐈𝐃 🆔</blockquote> - <code>neonan23@ibl</code>\n\n'
    '<i>• Click /myplan To Check Your Plan\n• Send Screenshots After Payment\n'
    '• After Sending Screenshot Give Us Some Time To Add You In Premium</i></b>'
)

# ============== CLONE SETTINGS ==============

# Clone Information : If Clone Mode Is True Then Bot Clone Other Bots.
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "") # Necessary If clone mode is true
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '') # Public Channel Username Without @ or without https://t.me/ and Bot Is Admin With Full Right.


# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+o1s-8MppL2syYTI9')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/neonfiles')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Talk2NeonBot') # Support Chat Link Without https:// or @
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/MyselfNeon')

# True Or False
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
BUTTON_MODE = bool(environ.get('BUTTON_MODE', True))
MAX_BTN = bool(environ.get('MAX_BTN', True))
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
IMDB = bool(environ.get('IMDB', False))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))
SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))
MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', True))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))


# Token Verification Info :
VERIFY = bool(environ.get('VERIFY', False))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')

# If You Fill Second Shortner Then Bot Attach Both First And Second Shortner And Use It For Verify.
VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', False))
# if verify second shortner is True then fill below url and api
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')


# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
TUTORIAL = environ.get('TUTORIAL', '') # How Open Shortner Link Video Link , Channel Link Where You Upload Your Video.


# Others
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Powered by @NeonFiles ❤️✨')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)


# Choose Option Settings 
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = ["1900", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]




# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")


# Rename Info : If True Then Bot Rename File Else Not
RENAME_MODE = bool(environ.get('RENAME_MODE', True)) # Set True or False


# Auto Approve Info : If True Then Bot Approve New Upcoming Join Request Else Not
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False)) # Set True or False


# Start Command Reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] #don't add any emoji because tg not support all emoji reactions


