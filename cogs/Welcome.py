import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name="👋willkommen")
        em = discord.Embed(colour=0x708DD0)
        em.add_field(name='Herzlich Willkommen', value=member.name, inline=True)
        em.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name="👋willkommen")
        embed = discord.Embed(color=0x708DD0)
        embed.add_field(name='Auf Wiedersehen', value=member.name, inline=True)
        await channel.send(embed=embed)

    @commands.command()
    async def akzeptiere(self, ctx):
        def not_pinned(msg):
            return not msg.pinned
        user = ctx.message.author
        role = 'Freak'  # change the role here
        try:
            await user.add_roles(discord.utils.get(user.guild.roles, name=role))
            await ctx.channel.purge(limit=100, check=not_pinned)

        except Exception as e:
            await ctx.send('Cannot assign role. Error: ' + str(e))


def setup(client):
    client.add_cog(Welcome(client))