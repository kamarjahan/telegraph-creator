import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram import filters, Client

force_channel = "septemberfilms"


@Client.on_message(filters.command(["force"]))
async def force(bot, msg):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, msg.from_user.id)
            if user.status == "you removed":
                await msg.reply_text("you are banned")
                return
        except UserNotParticipant:
            await msg.reply_text(
                text="your not sub my grp",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("join update", url=f"t.me/{force_channel}")
                 ]]
                )
            )
            return
    await msg.reply_text("hi")








