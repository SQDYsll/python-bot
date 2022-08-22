import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from asyncio import sleep
import time

# remove all "#" characters and insert the necessary data which is described in 'description'
bot_token = 'token'                               # copy token https://discord.com/developers/applications/
bot_id = 'bot id'                                 # copy token https://discord.com/developers/applications/
bot_name = 'name your bot'                        # pick a name for your bot
bot_prefix = 'prefix for bot commands'            # select the desired prefix for the bot that will be placed before the message to call commands (!for_example)

bot = commands.Bot(command_prefix=bot_prefix, description='random description')

# game activity timer if you want activate, just delete """ at the beginning and at the end
"""
@bot.event
async def on_ready():

    minute = 0

    while True:
        await asyncio.sleep(60)
        minute += 1
        console = str(minute) + " min"
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(console))
"""
# to change the call command in line with code "async def pick_a_command(context):" write what you want, for example info. Now, in order to call this command
# you need to write in the discord chat !info. Where "!" this is the prefix you chose earlier
@bot.command()
async def pick_a_command(context):
    await context.send('```write the result a command```')

print("Bot is online!")
bot.run(bot_token)
input()