# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "27318489"))
API_HASH = os.environ.get("API_HASH", "6e87be2c71039c0c6f2077266f9827c2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6638166308:AAEauhWVObw1mCglDLAFF1PzKC51v2eJdLA")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "5979184565").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://kajitest:kajitest@cluster0.l308bgi.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5979184565")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5979184565)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001528714984")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Kajilinks_official") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
