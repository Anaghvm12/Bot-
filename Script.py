class script(object):
    START_TXT = """ʜᴇʟʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪꜱ <a href=https://t.me/{}>{}</a>, ɪ ᴄᴀɴ ᴩʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ, ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ 😇"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """○ 𝖬𝗒 𝖭𝖺𝗆𝖾 : <a href=https://t.me/{}>{}</a>
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href="https://t.me/DARKWEBLOAD">𝑡ℎ𝑖𝑠 𝑝𝑒𝑟𝑠𝑜𝑛</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥 
○ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆
○ 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖧𝖾𝗋𝗈𝗄𝗎
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : 𝖬𝗈𝗇𝗀𝗈𝖣𝖡 
○ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : 𝖵9.8 [BeTa]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project."""
    ALIVE_TXT ="""<b>ALIVE MODULE</b>
• /alive - check me alive or dead🤧
Just for a rasam😂"""
    OWNER_TXT ="""<b>മുതലാളി 🔥</b>
• /owner - To See My Owner"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
  /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>"""
    STICKER_TXT ="""<b>COMMAND /stickerid\n𝖨𝖿 𝖸𝗈𝗎 𝖭𝖾𝖾𝖽 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖽 𝖢𝗅𝗂𝖼𝗄 /stickerid 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖽 (𝖱𝖾𝗉𝗅𝗒 𝖶𝗂𝗍𝗁 𝖲𝗍𝗂𝖼𝗄𝖾𝗋)</b>"""  
    PASTE_TXT = """Help: <b>Paste</b>
Paste some texts or documents on a website!
<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty
<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""    
    PURGE_TXT = """Help: <b>Purge</b>
Need to delete lots of messages? That's what purges are for!
<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.
<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""   
    JSON_TXT ="""<b>JSON MODULE</b>
JSON:
Bot returns json for all replied messages with /json
Features:
Message Editting JSON
Pm Support
Group Support
Note:
Everyone can use this command , if spaming happens bot will automatically ban you from the group"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>🎲 NOTHING MUCH JUST SOME FUN THINGS</b>
t𝗋𝗒 𝗍𝗁𝗂𝗌 𝖮𝗎𝗍: 
𝟣. /dice - Roll The Dice 
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin :</b>
<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>
<b>📚 Commands & Usage:</b>
◉ /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
◉ /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    
    RESTRIC_TXT = """Help: <b>Restrictions</b>
Some people need to be publicly banned; spammers, annoyances, or just trolls.
This module allows you to do that easily, by exposing some common actions, so everyone will see!
<b>Commands and Usage:</b>
• /ban - ban a user.
• /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - unmute a user & unban a user.
<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>
<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    URLSHORT_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖲𝗁𝗈𝗋𝗍 𝖠 𝖴𝗋𝗅 
➤ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:
➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/IF_qoYnCLjs</code>"""
        ABOOK_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝖸𝗈𝗎 𝖢𝖺𝗇 𝖢𝗈𝗇𝗏𝖾𝗋𝗍 𝖠 𝖯𝖽𝖿 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖠 𝖵𝗂𝖽𝖾𝗈 𝖥𝗂𝗅𝖾 𝖶𝗂𝗍𝗁 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽.
➤𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:
➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    
    YTTHUMB_TXT = """𝖧𝖾𝗅𝗉𝗌 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖠𝗇𝗒 𝖸𝗈𝗎𝗍𝗎𝖻𝖾 𝖵𝗂𝖽𝖾𝗈 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅
    
🛃 𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾
𝖳𝗒𝗉𝖾 /ytthumb 𝖠𝗇𝖽 𝖵𝗂𝖽𝖾𝗈 𝖫𝗂𝗇𝗄
• 𝖤𝗑𝖺𝗆𝗉𝗅𝖾
<code>/ytthumb https://youtu.be/OWqbMNrVt5s</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>🗃️ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code></b>
<b>👤 𝖳𝗈𝗍𝖺𝗅 𝖴𝗌𝖾𝗋𝗌 : <code>{}</code></b>
<b>👥 𝖳𝗈𝗍𝖺𝗅 𝖢𝗁𝖺𝗍𝗌 : <code>{}</code></b>
<b>💾 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 : <code>{}</code> 𝖬𝖻</b>
<b>🖥️ 𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 : <code>{}</code> 𝖬𝖻</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    ENGLISH_TXT = """Look in Google or any internet browser's and find the right movie name and send it here for the movie / series ....\n\nIf you still do not get it. Send a message to group in this way Movie Name & year after @admin. Example: @admin Kurup.\n\nWe will try to upload if requested one is theatre print. Ott and Dvd released movies, will upload within 24 hours."""

    MALAYALAM_TXT = """Google അല്ലെങ്കിൽ ഏതേലും internet browser's ഇൽ നോക്കി ശരിയായ സിനിമയുടെ പേര് കണ്ടെത്തി ഇവിടെ നൽകുക എന്നാലേ സിനിമ / സീരിയസ് കിട്ടുകയുള്ളു....\n\nഎന്നിട്ടും കിട്ടുന്നില്ല എങ്കിൽ. @admin ശേഷം മൂവി Name & year. Example : @admin Kurup 2021 ഈ രീതിയിൽ  ഗ്രൂപ്പിൽ സെന്റ് ചെയുക. 24 മണിക്കൂറിനുള്ളിൽ അഡ്മിൻ കിട്ടിയാൽ upload ചെയ്യാം..\n\nതിയേറ്ററിൽ റിലീസ് ആയ മൂവിയാണ് ചോദിച്ചതെങ്കിൽ upload ചെയ്യാൻ ശ്രമിക്കാം. ott Dvd റിലീസ് ആയത് ആണെങ്കിൽ തന്നിരിക്കും."""
