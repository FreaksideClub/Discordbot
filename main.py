import os
import config.settings
from discord.ext import commands

#Bot Prefix
bot = commands.Bot(command_prefix="!")

#Commands Loading
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename !="__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

#Bot Token
bot.run(config.settings.BOT_TOKEN)