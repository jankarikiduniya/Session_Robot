from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("ð¥ sá´á´Êá´ É¢á´É´á´Êá´á´ÉªÉ´É¢ sá´ssÉªá´É´ ð¥", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ð  Êá´á´á´ÊÉ´ Êá´á´á´ ð ", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "â¨ á´á´Ê á´á´Êá´Ê Êá´á´s á´É´á´ sá´á´á´á´s â¨", url="https://t.me/AsadSupport/77"
            )
        ],
        [
            InlineKeyboardButton("ð¤ Êá´á´¡ á´á´ á´sá´ ð¤", callback_data="help"),
            InlineKeyboardButton("ðª á´Êá´á´á´ ðª", callback_data="about"),
        ],
        [InlineKeyboardButton("ð á´á´Êá´Ê Êá´á´s ð", url="https://t.me/Alexa_Help")],
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
â¨ **Available Commands** â¨

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
ââââââââââââââââââââââââ
ð¥ A á´á´á´¡á´ÊÒá´Ê Êá´á´
á´Ò â»ï¸ á´Ê á´sá´á´ á´ÊÉª ð¥
âââââââââââââââââ
GENERATE SESSION FOR TG...
âââââââââââââââââââ
â£â [ðð«ððð­ð¨ð«] [Asad Ali](https://t.me/Dr_Asad_Ali)
â£â [ðððð«ð­]   [Heart â¤ï¸](https://t.me/Give_Me_Heart)
â£â [ðð¨ð­ ðð©ððð­ðð¬] [Our Other Bots](https://t.me/AsadSupport)
â£â [ðð®ð« ððð] [Fed Logs](https://t.me/Part_Of_Rocks)
â£â [ððð­ð°ð¨ð«ð¤] [Rocks](https://t.me/Shayri_Music_Lovers)
âââââââââââââââââââ
ð 
IF HAVE ANY QUESTION OR WANT REPO THEN CONTACT Â» TO Â» MY Â» [OWNER] @Dr_Asad_Ali
   """
