import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name='general')
        embed = discord.Embed(color=0x4a3d9a)
        embed.add_field(name="Welcome", value=f"{member.name} has joined {member.guild.name}", inline=False)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name='general')
        embed = discord.Embed(color=0x4a3d9a)
        embed.add_field(name="Bye Bye", value=f"{member.name} has left {member.guild.name}", inline=False)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Welcome(client))