from settings import *
import discord
from discord.ext import commands

#Bot Prefix
bot = commands.Bot(command_prefix="!")
client = discord.Client()


#Commands Loading
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename !="__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

#Bot Token
bot.run(DISCORD_BOT_TOKEN)