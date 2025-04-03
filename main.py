# Don't Remove Credit Tg - https://t.me/Prime_Botz 
# Subscribe Telegram Channel For Amazing Bot https://t.me/Prime_Botz
# Support Group Tg ➠ https://t.me/Prime_Botz_Support
# Ask Doubt on HTTPS://T.ME/MR_PRIME_SUPREME

from configs import Config  
from pyrogram import Client, filters, idle  
from pyrogram.enums import ParseMode  
from pyrogram.errors import UserNotParticipant  
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio  
import urllib.parse  

AUTH_CHANNEL = Config.AUTH_CHANNEL

# Bot Client
Bot = Client("PrimeBotz", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)  

# User Client
User = Client("UserSession", api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=Config.USER_SESSION_STRING)  

async def is_subscribed(bot, user_id):
    """Check if the user is subscribed to the required channel(s)."""
    btn = []
    for channel in AUTH_CHANNEL:
        try:
            await bot.get_chat_member(int(channel), user_id)
        except UserNotParticipant:
            chat = await bot.get_chat(int(channel))
            btn.append([InlineKeyboardButton("✇ Join Updates Channel ✇", url=chat.invite_link)])
        except Exception as e:
            pass
    return btn

async def force_sub(bot, message):
    """Middleware function to check subscription before allowing any command or search."""
    btn = await is_subscribed(bot, message.from_user.id)
    if btn:
        await message.reply_photo(
            photo="https://i.ibb.co/xt7fzdK3/photo-2025-03-07-15-29-59-7479090267811741696.jpg",  # Change this if needed
            caption="👋 Hello Buddy 👋,\n\n"
                    "You must join our updates channel before using the bot. "
                    "Click the 'Join Updates Channel' button below and then press 'Try Again'.",
            reply_markup=InlineKeyboardMarkup(btn + [[InlineKeyboardButton("♻️ Try Again ♻️", url=f"https://t.me/{(await bot.get_me()).username}?start=true")]])
        )
        return False
    return True

# Start Command
@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(bot, message: Message):
    if not await force_sub(bot, message):
        return

    await message.reply_photo(
        "https://i.ibb.co/fYmcFQvQ/photo-2025-04-03-10-45-24-7489036226658304024.jpg",
        caption=Config.START_MSG.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("☆ Add Me to Group ☆", url="https://t.me/Auto_Link_Search_Bot?startgroup=true")],
            [InlineKeyboardButton("✪ Support Group ✪", url="https://t.me/Movie_Request_Group_23"),
             InlineKeyboardButton("🎬 Movies Channel 🎬", url="https://t.me/TeraboxMovies_world")],
            [InlineKeyboardButton("〄 Updates Channel 〄", url="https://t.me/+3S41nEK-z3YxYjI1")],
            [InlineKeyboardButton("〆 About 〆", callback_data="About_msg"),
             InlineKeyboardButton("〆 Help 〆", callback_data="Help_msg")],
            [InlineKeyboardButton("✧ Creator ✧", url="https://t.me/ctgmovies23")]
        ]),
        parse_mode=ParseMode.HTML    
    )  


# Don't Remove Credit Tg - https://t.me/Prime_Botz
# Subscribe Telegram Channel For Amazing Bot https://t.me/Prime_Botz
# Support Group Tg ➠ https://t.me/Prime_Botz_Support
# Ask Doubt on HTTPS://T.ME/MR_PRIME_SUPREME

# Help Command
@Bot.on_message(filters.private & filters.command("help"))
async def help_handler(bot, message: Message):
    if not await force_sub(bot, message):
        return

    await message.reply_text(
        Config.ABOUT_HELP_TEXT.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("〄 Updates Channel 〄", url="https://t.me/+3S41nEK-z3YxYjI1"),
             InlineKeyboardButton("✪ Support Group ✪", url="https://t.me/Movie_Request_Group_23")],
            [InlineKeyboardButton("〆 About 〆", callback_data="About_msg")]
        ]),
        parse_mode=ParseMode.HTML
    )  

# Search Function
@Bot.on_message(filters.incoming & ~filters.channel)
async def inline_handlers(bot, message: Message):
    if not await force_sub(bot, message):
        return

    if not message.text:  
        return  # Ensure message has text  

    if message.text == '/start':
        return  

    sticker_msg = await message.reply_sticker("CAACAgUAAxkBAAIokWfElSr3UnEM3F6h-VYVOo9ye53fAAKJGAACAhAgVte0gD_wIF62HgQ")  
    await asyncio.sleep(3)  
    await sticker_msg.delete()  

    answers = f'**📂 🔍 ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ꜱᴇᴀʀᴄʜ 🔍 ➠ {message.text}**\n\n'  
    found = False  

    async for msg in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=message.text):  
        if msg.text and "\n" in msg.text:  
            found = True  
            f_text = msg.text.split("\n", 1)[0]  
            d_link = msg.text.split("\n", 2)[-1]  
            answers += f'''**▰▱▰▱▰▱▰▱▰▱▰▱▰▱  
📜 File Name: {f_text}\n  
🔗 Link: 👇  
{d_link}  
▰▱▰▱▰▱▰▱▰▱▰▱▰▱**\n\n'''  

    if found:
        answers += '''\n\n\n⋆★⋆━━━━━━★━━━━⋆★⋆\n❗️❗️❗️ ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛɪᴄᴇ ❗️❗️❗️\n⚠️ ʟɪɴᴋ ᴡɪʟʟ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ ɪɴ 3 ᴍɪɴᴜᴛᴇs... ⏰\n⋆★⋆━━━━━━★━━━━⋆★⋆'''  
        msg = await message.reply_text(answers, reply_to_message_id=message.id)
    else:
        google_search_url = f"https://www.google.com/search?q={urllib.parse.quote(message.text)}"  
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔍 ᴄʜᴇᴄᴋ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ 🔍", url=google_search_url)],
            [InlineKeyboardButton("📩 ʀᴇǫᴜᴇꜱᴛ ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ 📩", url="https://t.me/+2jX_TgG9neZlYTM1")]
        ])  
        msg = await message.reply_photo(
            photo="https://i.ibb.co/SgwHKxP/photo-2025-04-03-10-42-42-7489035792866607124.jpg",
            caption=f"**❌ ɴᴏ ʀᴇꜱᴜʟᴛꜱ ꜰᴏᴜɴᴅ ꜰᴏʀ ➠ {message.text}\n\n⚡ ᴛʀʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴡɪᴛʜ ᴄᴏʀʀᴇᴄᴛ ꜱᴘᴇʟʟɪɴɢ ᴏʀ ᴀᴅᴅ ᴛʜᴇ ʀᴇʟᴇᴀꜱᴇ ʏᴇᴀʀ ꜰᴏʀ ʙᴇᴛᴛᴇʀ ʀᴇꜱᴜʟᴛꜱ .🔍 ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ. 👇\n\n📩 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴀᴋᴇ ᴀ ʀᴇǫᴜᴇꜱᴛ ᴛᴏ ᴛʜᴇ ᴅɪʀᴇᴄᴛ ᴀᴅᴍɪɴ, ʏᴏᴜ ᴄᴀɴ ᴅᴏ ᴛʜᴀᴛ ꜰʀᴏᴍ ʙᴇʟᴏᴡ 👇 ʙᴜᴛᴛᴏɴ.**",
            reply_markup=keyboard,
            reply_to_message_id=message.id
        )  

    try:
        await asyncio.sleep(180)  
        await msg.delete()  
        await message.delete()  
    except:
        print(f"[{Config.BOT_SESSION_NAME}] - Failed to delete message for {message.from_user.first_name}")

# Callback Query Handler
@Bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data  
    if "About_msg" in cb_data:
        await cmd.message.edit(
            text=Config.ABOUT_BOT_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("〄 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/+3S41nEK-z3YxYjI1")],
                [InlineKeyboardButton("✧ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ ✧", url="https://t.me/Movie_Request_Group_23"),
                 InlineKeyboardButton("🏠 ʜᴏᴍᴇ 🏠", callback_data="gohome")]
            ]),
            parse_mode=ParseMode.HTML
        )  

    elif "Help_msg" in cb_data:
        await cmd.message.edit(
            text=Config.ABOUT_HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✪ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ✪", url="https://t.me/Movie_Request_Group_23"),
                 InlineKeyboardButton("〄 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/+3S41nEK-z3YxYjI1")],
                [InlineKeyboardButton("🏠 ʜᴏᴍᴇ 🏠", callback_data="gohome")]
            ]),
            parse_mode=ParseMode.HTML
        )  

    elif "gohome" in cb_data:  # এখানে ইন্ডেন্ট ঠিক করা হয়েছে
        await cmd.message.edit(
            text=Config.START_MSG.format(cmd.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("☆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ☆", url="https://t.me/Auto_Link_Search_Bot?startgroup=true")],
                [InlineKeyboardButton("✪ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ✪", url="https://t.me/Movie_Request_Group_23"),
                 InlineKeyboardButton("🎬 ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟ 🎬", url="https://t.me/TeraboxMovies_world")],
                [InlineKeyboardButton("〄 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/+3S41nEK-z3YxYjI1")],
                [InlineKeyboardButton("〆 ʜᴇʟᴘ 〆", callback_data="Help_msg"),
                 InlineKeyboardButton("〆 ᴀʙᴏᴜᴛ 〆", callback_data="About_msg")],
                [InlineKeyboardButton("✧ ᴄʀᴇᴀᴛᴏʀ ✧", url="https://t.me/ctgmovies23")]
            ]),
            parse_mode=ParseMode.HTML
        )

# Start Clients
Bot.start()  
User.start()  
idle()  
Bot.stop()  
User.stop()


# Don't Remove Credit Tg - https://t.me/Prime_Botz
# Subscribe Telegram Channel For Amazing Bot https://t.me/Prime_Botz
# Support Group Tg ➠ https://t.me/Prime_Botz_Support
# Ask Doubt on HTTPS://T.ME/MR_PRIME_SUPREME
