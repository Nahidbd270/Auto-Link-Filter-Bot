import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from .database import data

@Client.on_message(filters.command("broadcast") & filters.private & filters.user(ADMIN))
async def broadcast(client: Client, message: Message):
    try:
        msg = await message.reply_text("Wait a second!")
        if not message.reply_to_message:
            return await msg.edit("Please reply to a message to broadcast.")
        
        await msg.edit("Processing ...")
        completed, failed = 0, 0
        to_copy_msg = message.reply_to_message
        users_list = await data.get_all_users()
        
        for i, userDoc in enumerate(users_list):
            if i % 20 == 0:
                await msg.edit(f"Total: {i}\nCompleted: {completed}\nFailed: {failed}")
            user_id = userDoc.get("user_id")
            if not user_id:
                continue
            try:
                await to_copy_msg.copy(int(user_id))
                completed += 1
                await asyncio.sleep(0.1)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                try:
                    await to_copy_msg.copy(int(user_id))
                    completed += 1
                except Exception:
                    failed += 1
            except Exception as e:
                print(f"Error in broadcasting to {user_id}: {e}")
                failed += 1
                
        await msg.edit(f"Successfully Broadcasted\nTotal: {len(users_list)}\nCompleted: {completed}\nFailed: {failed}")
    except Exception as e:
        print(f"Error in broadcast: {e}")
        await message.reply_text("An error occurred while broadcasting.")

@Client.on_message(filters.command("users") & filters.user(ADMIN))
async def total_users(client: Client, message: Message):
    try:
        total = await data.users.count_documents({})
        await message.reply_text(f"📊 **Total Users:** `{total}`")
    except Exception as e:
        print(f"Error in /users command: {e}")
        await message.reply_text("⚠️ An error occurred while fetching user count.")
