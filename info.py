import re, os
from os import environ, getenv
from Script import script
import asyncio
from logging import WARNING, getLogger
from pyrogram import Client
from time import time
import logging 
from dotenv import load_dotenv
load_dotenv()

LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)
getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '24817837'))
API_HASH = environ.get('API_HASH', 'acd9f0cc6beb08ce59383cf250052686')
OWNER_ID = environ.get('OWNER_ID', '7428552084')
BOT_TOKEN = environ.get('BOT_TOKEN', "7783135016:AAEeWHYiBri1oURTw2WFjD24xz_YB_UD4AU")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/2518d4eb8c88f8f669f4c.jpg https://graph.org/file/d6d9d9b8d2dc779c49572.jpg https://graph.org/file/4b04eaad1e75e13e6dc08.jpg https://graph.org/file/05066f124a4ac500f8d91.jpg https://graph.org/file/2c64ed483c8fcf2bab7dd.jpg https://envs.sh/hwc.jpg https://envs.sh/hwZ.jpg https://envs.sh/fCc.jpg https://envs.sh/fhw.jpg https://envs.sh/Hzh.jpg https://envs.sh/HzQ.jpg https://envs.sh/Nya.jpg https://envs.sh/JNK.jpg https://envs.sh/Ea4.jpg https://envs.sh/EaU.jpg https://envs.sh/Eal.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/549fd9f3272214acade82.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/6988f560cf6d67339f628.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/549fd9f3272214acade82.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/347c1f79f36d3cf14e0f5.jpg'))
CODE = (environ.get('CODE', 'https://graph.org/file/02e7ecc3e2693b481b914.jpg'))
REFER_PICS = (environ.get("REFER_PICS", "https://graph.org/file/1c1a3cb814cd719ae3bd3.jpg https://graph.org/file/1a2e64aee3d4d10edd930.jpg")).split()

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'shareus.io'))
STREAM_API = (environ.get('STREAM_API', ''))
STREAMHTO = (environ.get('STREAMHTO', 'https://t.me/How_to_Download_7x/32'))

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
PREFIX = environ.get("PREFIX", "/")

CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002165407793"))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7428552084 5814104129').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '5814104129 7428552084').split()]
auth_channel = environ.get('AUTH_CHANNEL', '') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001566837125') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1001905367057') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True)) # True if you want no results messages in Log Channel

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Ethan:Ethan123@telegrambots.lva9j.mongodb.net/?retryWrites=true&w=majority&appName=TELEGRAMBOTS")
DATABASE_NAME = environ.get('DATABASE_NAME', "Hokage")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#chatgptAI
AI = is_enabled((environ.get("AI","True")), True)
OPENAI_API = environ.get("OPENAI_API", " ")
DEEP_API = environ.get("DEEP_API", "3ac9b077-654f-45c6-a1f0-a04a5ef6b69e")
GOOGLE_API_KEY = environ.get("GOOGLE_API_KEY", "AIzaSyD214hhYJ-xf8rfaWX044_g1VEBQ0ua55Q")
AI_LOGS = int(environ.get("AI_LOGS", "-1002376378205")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of Bot ]

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nTa requêtepour rejoindre {title} a été approuvé.\n\‣ Propulser @BotZFlix</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Referal Settings
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1 week')
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'kingcey') # owner username without @

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002376378205')) #Log channel id ( make sure bot is admin )
DUMP_CHNL = int(environ.get('DUMP_CHNL', '-1002067012611'))

# Verify
VERIFY = bool(environ.get('VERIFY', False)) # Verification On ( True ) / Off ( False )
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/How_to_Download_7x/26') # How to open tutorial link for verification

# Others
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', '1Jh0re6olVUHnr3eEyFG7NZX7RF3')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
BOT_USERNAME = environ.get("BOT_USERNAME", "Marsh_Mello_bot")
BOT_NAME = environ.get("BOT_NAME", "Marsh Crow")
BOT_ID = environ.get("BOT_ID", "7783135016")
S_GROUP = environ.get('S_GROUP', "kingcey1")
S_CHANNEL = environ.get('S_CHANNEL', "BotZFlix")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/kingcey1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/AntiFlix_A')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/How_to_Download_7x/32') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
MSG_ALRT = environ.get('MSG_ALRT', 'Maintenu Par : BotZFlix')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/AntiFlix_d') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002463797892')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["francais", "", "vf", "", "english", "", "vostfr", ""]

SEASONS = ["S01" , "S02" , "S03" , "S04", "S05" , "S06" , "S07" , "S08" , "S09" , "S010"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", "", "UHD", "", "HD", "", "SD", "", "FHD", "", "4K", "", "8K", ""]


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'hokage'))
MULTI_CLIENT = False
name = str(environ.get('name', 'hokage'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002376378205'))

REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]  # Ne pas ajouter d'emoji non supporté par Telegram


LOG_STR = "Les configurations personnalisées actuelles sont :\n"
LOG_STR += ("Les résultats IMDB sont activés, le bot affichera les détails d'IMDB pour vos requêtes.\n" if IMDB else "Les résultats IMDB sont désactivés.\n")
LOG_STR += ("P_TTI_SHOW_OFF est activé, les utilisateurs seront redirigés pour envoyer /start au bot en MP au lieu d'envoyer le fichier directement.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF est désactivé, les fichiers seront envoyés en MP, au lieu de rediriger vers /start.\n")
LOG_STR += ("SINGLE_BUTTON est activé, le nom du fichier et la taille du fichier seront affichés dans un seul bouton au lieu de deux boutons séparés.\n" if SINGLE_BUTTON else "SINGLE_BUTTON est désactivé, le nom du fichier et la taille du fichier seront affichés sous forme de boutons distincts.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION est activé avec la valeur {CUSTOM_FILE_CAPTION}, vos fichiers seront envoyés avec cette légende personnalisée.\n" if CUSTOM_FILE_CAPTION else "Aucun CUSTOM_FILE_CAPTION trouvé, la légende par défaut du fichier sera utilisée.\n")
LOG_STR += ("La description longue d'IMDB est activée.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION est désactivée, l'intrigue sera plus courte.\n")
LOG_STR += ("Le mode de vérification orthographique est activé, le bot suggérera des films similaires si le film n'est pas trouvé.\n" if SPELL_CHECK_REPLY else "Le mode SPELL_CHECK_REPLY est désactivé.\n")
LOG_STR += (f"MAX_LIST_ELM est activé, les longues listes seront raccourcies aux premiers {MAX_LIST_ELM} éléments.\n" if MAX_LIST_ELM else "La liste complète des acteurs et de l'équipe sera affichée dans le modèle IMDB, limitez-la en ajoutant une valeur à MAX_LIST_ELM.\n")
LOG_STR += f"Votre modèle IMDB actuel est {IMDB_TEMPLATE}"
