import discord
from discord.ext import commands
import main

'''Module for the >info command.'''

class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def info(self, ctx, member):
        """Get user info. Ex: >info @user"""
        if ctx.invoked_subcommand is None:
            name = ctx.message.content[5:].strip()
            if name:
                try:
                    name = ctx.message.mentions[0]
                except:
                    name = ctx.message.server.get_member_named(name)
                if not name:
                    await self.bot.send_message(ctx.message.channel, commands.Bot + 'Could not find user.')
                    return
            else:
                name = ctx.message.author

            if ctx.message:
                em = discord.Embed(colour=0x708DD0)
                em.add_field(name='User ID', value=name.id, inline=True)
                em.add_field(name='Nick', value=name.name, inline=True)
                em.add_field(name='Status', value=name.status, inline=True)
                em.add_field(name='Account Created', value=name.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.add_field(name='Join Date', value=name.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.set_footer(text='RAW-Bot made by RAW-Team')
                await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Userinfo(bot))
