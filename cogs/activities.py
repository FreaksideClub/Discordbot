from discord.ext import commands
import discord
from random import choice
from utils import create_voice_channel, get_category_by_name
from utils import auto_voice_channel_names as channel_names

class Activities(commands.Cog):

    current_streamers = list ()

    def __init__(self, bot):
        self.created_channels = []
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if after.bot or before.bot:
            return

        before_a_count = len(before.activities)
        after_a_count = len(after.activities)

        if before_a_count > after_a_count:
            print("User stopped playing")
            print(f'{after.name} stopped {before.activities[0].name}')
        elif before_a_count == after_a_count:
            print("Something changed")
        else:
            print("User started activity")
            print(f'{after.name} started {after.activities[0].name}')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after, auto_voice_channel="Get a Voice"):
        if member.bot:
            return

        if not before.channel:
            print(f'{member.name} joined {after.channel.name}')

        if before.channel and not after.channel:
            print("User left channel")

        if before.channel and after.channel:
            if before.channel.id != after.channel.id:
                print("user switched voice channels")
            elif member.voice.self_stream:
                print("User started streaming")
                self.current_streamers.append(member.id)
            elif member.voice.self_mute:
                print("User muted")
            elif member.voice.self_deaf:
                print("User deafened")
            else:
                print("Something else happened!")
                for streamer in self.current_streamers:
                    if not member.voice.self_stream:
                        print("User stopped streaming")
                        self.current_streamers.remove(member.id)
                    break

        if after.channel is not None:
            if after.channel.name == auto_voice_channel:
                name = choice(channel_names)
                channel = await create_voice_channel(after.channel.guild, name)
                self.created_channels.append(channel)
                await member.move_to(channel)

        if before.channel in self.created_channels and len(before.channel.members) == 0:

            print("User left a temp channel")
            if len(before.channel.members) == 0:
                print("channel is now empty")
                await before.channel.delete()

def setup(bot):
    bot.add_cog(Activities(bot))