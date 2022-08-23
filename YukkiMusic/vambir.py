import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["المطور","مطور","فيرس","المبرمج"])
    & ~filters.edited
)
async def vambir(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/music_rio_bot",
        caption=f"""◍ الزرار الاول: قناه السورس \n◍ الزرار الثاني: هو مبرمج السورس\n√""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "𓆩 ˹𝚂𝙾𝚞𝚁𝙲𝙴 𝙺𝙰𝚁𝙼𝙰𝙽˼ 𓆪", url=f"https://t.me/YDDCJ"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "#،𝙑𝒗 𝙄𝒊 𝙍𝒓 𝙐𝒖 𝙎𝒔 💎⛓", url=f"https://t.me/VR_LA"),
                ],
            ]
        ),
    )
