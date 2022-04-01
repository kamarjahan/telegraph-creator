import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram import filters, Client

force_channel = "septemberfilms"


@Client.on_message(filters.text & filters.photo & filters.video & filters.command & filters.incoming)
async def start(bot, msg):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, msg.from_user.id)
            if user.status == "you removed":
                await msg.reply_text("you are banned")
                return
        except UserNotParticipant:
            await msg.reply_text(
                text="PLEASE JOIN OUR UPDATE CHANNEL/GROUP TO USE THIS COMMAND",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("JOIN UPDATE GRP", url=f"t.me/{force_channel}"),
                 ],[
                 InlineKeyboardButton("TRY AGAIN", url=f"http://t.me/ddtelegraphbot?start=start_")  
                 ]]
                )
            )
            return
    await msg.reply_text("your subscription added to db now you can use the bot")






FORCE_CODE = """if force_channel:
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
            return"""




BUTTONS1 = [[

        InlineKeyboardButton('ADD ME TO GROUP', url='t.me/ddtelegraphbot?startgroup=true'),
    ],
    [

        InlineKeyboardButton('🤔Help', callback_data='help'),
        InlineKeyboardButton('Close🔐', callback_data='close')
    ],
    [

    ]]








