from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def status(self, ctx):
        guild = ctx.guild

        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)
        embed = discord.Embed(color=0x22a7f0)
        embed.add_field(name="Server Name", value=guild.name, inline=False)

        embed.add_field(name="#Voice Channels", value=no_voice_channels)
        embed.add_field(name="# Text Channels", value=no_text_channels)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))