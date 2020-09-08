from discord.ext import commands


class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def setup_voice(self, ctx):
        try:
            await ctx.send("Please wait!")
            await ctx.send("Create category 🎤 VOICE ZONE 🎤")
            category = await ctx.guild.create_category("🎤 VOICE ZONE 🎤", overwrites=None, reason=None)
            await ctx.send("Create channel 📢Get a Voice")
            await ctx.guild.create_voice_channel(f"📢Get a Voice", overwrites=None, category=category, reason=None)
            await ctx.send("Setup finished!")
        except Exception as errors:
            print(f"Bot Error: {errors}")


def setup(bot):
    bot.add_cog(Setup(bot))
