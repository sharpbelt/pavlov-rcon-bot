import discord
from discord.ext import commands
import traceback
from pavlov import PavlovRCON
import asyncio
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True
bot_token = "token"
serverIP = "ip"
serverPORT = "9100"
RCONPassword = "password"
bot_prefix = "!"
allowed_channel_id = channel-id
bot = commands.Bot(command_prefix=bot_prefix, intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    try:
        if message.content.startswith("!run ") and message.channel.id == allowed_channel_id:
            command_to_run = message.content[5:]
            pavlov = PavlovRCON(serverIP, int(serverPORT), RCONPassword)
            data = await pavlov.send(command_to_run)
            await message.channel.send(f"Command '{command_to_run}' sent successfully: {data}")
    except Exception as err:
        print(f'Server crashed: {err}')
        traceback.print_exc()
        await message.channel.send(f"An error occurred: {err}")
bot.run(bot_token)
