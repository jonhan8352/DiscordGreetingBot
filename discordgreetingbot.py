import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command()
async def random_response(ctx):
    if ctx.channel.id == CHANNEL_ID:
      responses = ["I'm doing well, thank you!", "I'm feeling great, thank you!", "I'm fine. How about you?", "I'm good. Anything I can do for you?", "I'm doing well. And you?"]
        await ctx.send(random.choice(responses))
    else:
        await ctx.send("This command can only be used in a specific channel.")

bot.run('YOUR_BOT_TOKEN')
