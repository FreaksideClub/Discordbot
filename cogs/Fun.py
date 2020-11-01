from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random(self, ctx, *arg):
        '''Returns a random number or member
        Use:
        -----------
        :random
            Returns a random number between 1 and 100
        :random coin
            Flips a coin (head or tails)
        :random 6
            Returns a random number between 1 and 6
        :random 10 20
            Returns a random number between 10 and 20
        :random user
            Returns a random user who is currently online

        :random choice HΞRR-DΞMΞN Alpy ExiWexi
            Random name
        '''
        if ctx.invoked_subcommand is None:
            if not arg:
                start = 1
                end = 100
            elif arg[0] == 'd6':
              start = 1
              end = 6
            elif arg[0] == 'd20':
              start = 1
              end = 20
            elif arg[0] == 'flip' or arg[0] == 'coin':
                coin = ['Head', 'Tails']
                await ctx.send(f':arrows_counterclockwise: {random.choice(coin)}')
                return
            elif arg[0] == 'choice':
                choices = list(arg)
                choices.pop(0)
                await ctx.send(f':congratulations: The winner is {random.choice(choices)}')
                return
            elif arg[0] == 'user':
                online = self.userOnline(ctx.guild.members)
                randomuser = random.choice(online)
                if ctx.channel.permissions_for(ctx.author).mention_everyone:
                    user = randomuser.mention
                else:
                    user = randomuser.display_name
                await ctx.send(f':congratulations: The winner is {user}')
                return
            elif len(arg) == 1:
                start = 1
                end = int(arg[0])
            elif len(arg) == 2:
                start = int(arg[0])
                end = int(arg[1])
            await ctx.send(
                f'**:arrows_counterclockwise:** Random number ({start} - {end}): {random.randint(start, end)}')

def setup(bot):
    bot.add_cog(Fun(bot))