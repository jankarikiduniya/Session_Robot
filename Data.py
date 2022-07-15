from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "✨ ᴏᴜʀ ᴏᴛʜᴇʀ ʙᴏᴛs ᴀɴᴅ sᴛᴀᴛᴜs ✨", url="https://t.me/AsadSupport/77"
            )
        ],
        [
            InlineKeyboardButton("🤔 ʜᴏᴡ ᴛᴏ ᴜsᴇ 🤔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("💌 ᴏᴛʜᴇʀ ʙᴏᴛs 💌", url="https://t.me/Alexa_Help")],
    ]

    START = """
Hey {}
Welcome to {}
If you don't trust this bot, 
1) stop reading this message
2) delete this chat
Still reading?
You can use me to generate Pyrogram and Telethon string session. Use below buttons to learn more !
By @Shayri_Music_Lovers And @AsadSupport
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/repo - Get Repo
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @AsadSupport

Source Code : [Click Here](https://t.me/Alexa_Help)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @Dr_Assad_Ali
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ᴏғ ♻️ ᴅʀ ᴀsᴀᴅ ᴀʟɪ 🔥
━━━━━━━━━━━━━━━━━
GENERATE SESSION FOR TG...
┏━━━━━━━━━━━━━━━━━┓
┣★ [𝐂𝐫𝐞𝐚𝐭𝐨𝐫] [Asad Ali](https://t.me/Dr_Asad_Ali)
┣★ [𝐇𝐞𝐚𝐫𝐭]   [Heart ❤️](https://t.me/Give_Me_Heart)
┣★ [𝐁𝐨𝐭 𝐔𝐩𝐝𝐚𝐭𝐞𝐬] [Our Other Bots](https://t.me/AsadSupport)
┣★ [𝐎𝐮𝐫 𝐅𝐞𝐝] [Fed Logs](https://t.me/Part_Of_Rocks)
┣★ [𝐍𝐞𝐭𝐰𝐨𝐫𝐤] [Rocks](https://t.me/Shayri_Music_Lovers)
┗━━━━━━━━━━━━━━━━━┛
💞 
IF HAVE ANY QUESTION OR WANT REPO THEN CONTACT » TO » MY » [OWNER] @Dr_Asad_Ali
   """
