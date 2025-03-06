# Don't Remove Credit Tg - https://t.me/Prime_Botz
# Subscribe Telegram Channel For Amazing Bot https://t.me/Prime_Botz
# Support Group Tg ➠ https://t.me/Prime_Botz_Support
# Ask Doubt on HTTPS://T.ME/MR_PRIME_SUPREME

import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    API_ID = int(os.environ.get("API_ID", 19234664))
    API_HASH = os.environ.get("API_HASH", "29c2f3b3d115cf1b0231d816deb271f5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8070686038:AAGaXuAB1MZYGXuLUtZ5EeTh76nlA3DRoQc")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "Link-Search-Prime-Botz")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQElf2gAJK2K9nJAQK3b5sBgJU-rFFyd_nWwJJ87fnPF985QjyzquoO5zTS6_eA2CgnudhyccFcQ33KMoWIPNlGeCX81EajhENbJnP_EUeZ-1vCcFcxrUbHZs-u-dZ2uW1lMFN-xndaOgce0xKhQFDsOilnshUSXQudojkW9anrlXLwthn1-FhgvYfWRfw7ji-Dn42Eh-yYKW7IpgI6SOcAPxptoxgQLJYuO4zUhTz37lOJRWYpRng9I3-Z46vXU8NH5K5DYEdy-cZc4c0BJvNpO3VtdQExd-Eft73WDANDX0dcnyJWsAQ0bQzdJINrY-E5TAK8nx6VFYwsOgrWs4YwP7yJ4KQAAAAHgT530AA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1002312573856))
    BOT_USERNAME = os.environ.get("Auto_Link_Search_Bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER","8058281460"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://manogog673:manogog673@cluster0.ot1qt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", False)
    AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002309821556').split()] 
    BROADCAST_AS_COPY = True  
    ABOUT_BOT_TEXT = """<b><blockquote>⍟───[  <a href='https://t.me/Prime_Botz'>📌 ᴍʏ ᴅᴇᴛᴀɪʟꜱ ʙʏ ᴘʀɪᴍᴇ ʙᴏᴛᴢ 🤖</a ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/Prime_Link_Search_FastBot'>🔍 ᴘʀɪᴍᴇ ʟɪɴᴋ sᴇᴀʀᴄʜ ғᴀsᴛʙᴏᴛ 🚀</a>
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Prime_Nayem'>ᴍʀ.ᴘʀɪᴍᴇ</a> 
‣ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Prime_Botz'>ᴘʀɪᴍᴇ ʙᴏᴛᴢ</a> 
‣ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Prime_Movies4U'>ᴘʀɪᴍᴇ ᴍᴏᴠɪᴇs</a> 
‣ ѕᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href='https://t.me/Prime_Botz_Support'>ᴘʀɪᴍᴇ ʙᴏᴛᴢ ѕᴜᴘᴘᴏʀᴛ</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]></b>"""

    ABOUT_HELP_TEXT = """<b>✅ ɪᴛ'ꜱ ɴᴏᴛ ᴀ ᴅɪꜰꜰɪᴄᴜʟᴛ ᴘʀᴏᴄᴇꜱꜱ, ᴊᴜꜱᴛ ᴛʏᴘᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ʜᴇʀᴇ ᴀɴᴅ ᴛʜᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ʟɪɴᴋ ᴡɪʟʟ ᴄᴏᴍᴇ.  

🔍 ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ꜱᴘᴇʟʟɪɴɢ, ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ɪᴛ ꜰʀᴏᴍ ɢᴏᴏɢʟᴇ.  

➕ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴛʜɪꜱ ᴛᴏ ᴀɴʏ ᴏꜰ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ, ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ɪᴛ, ᴀɴᴅ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ʟɪɴᴋꜱ ᴛᴏ ᴀʟʟ ᴛʜᴏꜱᴇ ɢʀᴏᴜᴘꜱ.  

❗ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍꜱ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴏᴘᴛɪᴏɴꜱ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ꜱᴜᴘᴘᴏʀᴛ ꜰʀᴏᴍ ᴜꜱ. ❗
    

🤖 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ʟɪᴋᴇ ᴛʜɪꜱ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ \nᴄᴏɴᴛᴀᴄᴛ ᴏᴜʀ ᴅᴇᴠᴇʟᴏᴘᴇʀ 👉 <a href='https://t.me/prime_Nayem'>ᴍʀ.ᴘʀɪᴍᴇ</a></b>
"""

    HOME_TEXT = """
<b>👋 ʜᴇʟʟᴏ ʙᴜᴅᴅʏ! {}🥰,

🤖 ɪ ᴀᴍ ᴀ ꜱɪᴍᴘʟᴇ ʙᴜᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀɴᴅ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋ ꜱᴇᴀʀᴄʜ ʙᴏᴛ.  
ʏᴏᴜ ᴄᴀɴ ᴄᴀʟʟ ᴍᴇ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ, ʟɪɴᴋ ꜱᴇᴀʀᴄʜ, ᴏʀ ᴜʀʟ ꜱᴇᴀʀᴄʜ ʙᴏᴛ—ᴡʜɪᴄʜᴇᴠᴇʀ ʏᴏᴜ ᴘʀᴇꜰᴇʀ!  

📌 ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ!!  

⚡ ɪᴛ ɪꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴍᴇ, ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ.

<blockquote> 🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ  <a href='https://t.me/Prime_Botz'>ᴘʀɪᴍᴇ ʙᴏᴛz</a></blockquote>
"""

# Don't Remove Credit Tg - https://t.me/Prime_Botz
# Subscribe Telegram Channel For Amazing Bot https://t.me/Prime_Botz
# Support Group Tg ➠ https://t.me/Prime_Botz_Support
# Ask Doubt on HTTPS://T.ME/MR_PRIME_SUPREME
    

    START_MSG = """
<b>👋 ʜᴇʟʟᴏ ʙᴜᴅᴅʏ! {}🥰,

🤖 ɪ ᴀᴍ ᴀ ꜱɪᴍᴘʟᴇ ʙᴜᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀɴᴅ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋ ꜱᴇᴀʀᴄʜ ʙᴏᴛ.  
ʏᴏᴜ ᴄᴀɴ ᴄᴀʟʟ ᴍᴇ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ, ʟɪɴᴋ ꜱᴇᴀʀᴄʜ, ᴏʀ ᴜʀʟ ꜱᴇᴀʀᴄʜ ʙᴏᴛ—ᴡʜɪᴄʜᴇᴠᴇʀ ʏᴏᴜ ᴘʀᴇꜰᴇʀ!  

📌 ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ!!  

⚡ ɪᴛ ɪꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴍᴇ, ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ.

<blockquote> 🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ  <a href='https://t.me/Prime_Botz'>ᴘʀɪᴍᴇ ʙᴏᴛz</a></blockquote>
"""

# Don't Remove Credit Tg - https://t.me/Prime_Botz
# Subscribe Telegram Channel For Amazing Bot https://t.me/Prime_Botz
# Support Group Tg ➠ https://t.me/Prime_Botz_Support
# Ask Doubt on HTTPS://T.ME/MR_PRIME_SUPREME
