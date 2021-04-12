from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CgACAgUAAxkDAAKTW2BzoCtRbAIxilmvOXta2hs7dyIOAAJQAwACgYs5V4BBr0TfyanDHgQ")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI'm Rythm Music Bot i can help you play music in your group's voice chat.
\nTo add in your group contact us at @godzilla_bot_support.
\nUse the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/VCPlayBot?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/Hi01212"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/sum897/VCPlayBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌍 Music World", url="https://t.me/godzilla_bot_support"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
