import asyncio
from discord.ext import commands
import discord


def is_not_pinned(mess):
    return not mess.pinned


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Stats about server
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def server(self, ctx):
        """Various info about the server."""
        guild = ctx.guild

        online = 0
        for i in guild.members:
            if str(i.status) == 'online':
                online += 1

        channel_count = len([x for x in guild.channels if type(x) == discord.channel.TextChannel])

        role_count = len(guild.roles)
        emoji_count = len(guild.emojis)

        em = discord.Embed(color=0xea7938)
        em.add_field(name='Name', value=guild.name)
        em.add_field(name='Owner', value=guild.owner, inline=False)
        em.add_field(name='Members', value=ctx.guild.member_count)
        em.add_field(name='Currently Online', value=online)
        em.add_field(name='Text Channels', value=str(channel_count))
        em.add_field(name='Region', value=guild.region)
        em.add_field(name='Number of roles', value=str(role_count))
        em.add_field(name='Number of emotes', value=str(emoji_count))
        em.add_field(name='Created At', value=guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.set_thumbnail(url=guild.icon_url)
        em.set_author(name='Server Info',
                      icon_url='https://cdn.discordapp.com/icons/558732591679668233/ef633304894c85044bfa9c1ea6e44adf.png')
        em.set_footer(text='Server ID: %s' % guild.id)
        em.set_footer(text='FSC-Bot made by ExiWexi')
        await ctx.send(embed=em)

        await asyncio.slepp(2)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(manage_messages=True)
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

            if ctx.message.author.permissions_in(ctx.message.channel).attach_files:
                em = discord.Embed(colour=0x708DD0)
                em.add_field(name='User ID', value=name.id, inline=True)
                em.add_field(name='Nick', value=name.name, inline=True)
                em.add_field(name='Status', value=name.status, inline=True)
                em.add_field(name='Account Created', value=name.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.add_field(name='Join Date', value=name.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.set_thumbnail(url=name.avatar_url)
                em.set_author(name=name,
                              icon_url='https://cdn.discordapp.com/icons/558732591679668233/ef633304894c85044bfa9c1ea6e44adf.png')
                em.set_footer(text='FSC-Bot made by ExiWexi')
                await ctx.send(embed=em)

            await asyncio.sleep(2)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, *limit):
        '''Deletes multiple messages at once (ADMIN ONLY)
        Example:
        -----------
        :purge 100
        '''

        def not_pinned(msg):
            return not msg.pinned
        try:
            limit = int(limit[0])
        except IndexError:
            limit = 1
        deleted = 0
        while limit >= 1:
            cap = min(limit, 100)
            deleted += len(await ctx.channel.purge(limit=cap, before=ctx.message, check=not_pinned))
            limit -= cap
        tmp = await ctx.send(f'**:put_litter_in_its_place:** {deleted} Messages deleted')
        await asyncio.sleep(15)
        await tmp.delete()
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Admin(bot))
