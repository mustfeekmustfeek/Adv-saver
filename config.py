# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "5618662"))
API_HASH = getenv("API_HASH", "bf2b762357b4b3c79bbb01e7529b81e2")
BOT_TOKEN = getenv("BOT_TOKEN", "7398759794:AAGf2lx9-Z8OFJcZnGcuygY_cMLi_fCCTs0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7962530240").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://King0077637373:945544Mk@#@cluster0.vjydpkn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1004816221926")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002433751531"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
