import asyncio
from discord import Embed
from discord.ext import commands
import discord

def is_not_pinned(mess):
    return not mess.pinned

def mods_or_owner():
    def predicate(ctx):
        return commands.check_any(commands.is_owner(),
                                  commands.has_role("Moderator"))
    return commands.check(predicate)

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not unload cog")
            return
        await  ctx.send("Cog unloaded")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def uload(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not load cog")
            return
        await  ctx.send("Cog loaded")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not reload cog")
            return
        await  ctx.send("Cog reloaded")

    # Stats about server
    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(manage_messages = True)
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



    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(manage_messages = True)
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
                em.add_field(name='Join Date', value=name.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
                em.set_footer(text='RAW-Bot made by RAW-Team')
                await ctx.send(embed=em)


    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def clear(self, ctx, args):
        args = ctx.message.content.split(' ')
        if len(args) == 2:
            if args[1].isdigit():
                count = int(args[1]) + 1
                deleted = await ctx.message.channel.purge(limit=count, check=is_not_pinned)
                await ctx.message.channel.send('{} Messages purged.'.format(len(deleted) - 1))
                await asyncio.sleep(10)
                await ctx.message.channel.purge(limit=1, check=is_not_pinned)


def setup(bot):
    bot.add_cog(Admin(bot))