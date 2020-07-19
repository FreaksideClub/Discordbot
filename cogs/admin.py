import PythonGists as PythonGists
from discord import Embed
from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Stats about server
    @commands.group(pass_context=True)
    async def server(self, ctx):
        """Various info about the server."""
        guild = ctx.guild

        online = 0
        for i in guild.members:
            if str(i.status) == 'online':
                online += 1

        em: Embed = discord.Embed(color=0xea7938)
        em.add_field(name='Name', value=guild.name)
        em.add_field(name='Owner', value=guild.owner, inline=False)
        em.add_field(name='Members', value=ctx.guild.member_count)
        em.add_field(name='Currently Online', value=online)
        em.add_field(name='Region', value=guild.region)
        em.add_field(name='Created At', value=guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.set_thumbnail(url=guild.icon_url)
        em.set_footer(text='RAW-Bot made by RAW-Team')
        await ctx.send(embed=em)



    @commands.group(pass_context=True)
    async def userinfo(self, ctx, member):
        """Get user info. Ex: !userinfo @user"""
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
    bot.add_cog(Admin(bot))