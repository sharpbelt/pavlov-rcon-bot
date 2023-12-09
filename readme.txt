you will need python 3.8 or above
you will need to setup a discord bot via the discord developer portal
pip install -r requirements.txt
set token to your bot token from the bot you just made
set ip to your servers ip
set port to your servers rcon port (normally 9100 but can differ depending on your host)
set password to your rcon password (plain text not md5 hash)
set the allowed channel id to the channel id (i advise this channel only being acessible to those you wish to have rcon access)
python3 bot.py
its now setup to use this bot you must do !run command
for example 
!run kick 76561199013473847
would return
Command 'kick 76561199013473847' sent successfully: {'Command': 'Kick', 'UniqueID': '76561199013473847', 'Kick': True, 'Successful': True}

if you need help with this im normally in the pavlov discord server my username is sharpbelt