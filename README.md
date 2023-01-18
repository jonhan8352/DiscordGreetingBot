# DiscordGreetingBot
----------------------

Here we can create a Discord Bot that interact with members with random message in specific channel in the Discord server.

First we must import discord and import at the beginning of our Python code.
```
import discord
from discord.ext import commands
import random
```
Then following code to point to the Channel ID.
```
bot = commands.Bot(command_prefix='!')

@bot.command()
async def random_response(ctx):
    if ctx.channel.id == CHANNEL_ID:
```
You can also check the channel name instead of the Channel ID by replacing the following code.
```
if ctx.channel.name == 'channel-name':
```
Now you can create the list of random message to be send with following code.
```
      responses = ["I'm doing well, thank you!", "I'm feeling great, thank you!", "I'm fine. How about you?", "I'm good. Anything I can do for you?", "I'm doing well. And you?]
        await ctx.send(random.choice(responses))
    else:
        await ctx.send("This command can only be used in a specific channel.")

bot.run('YOUR_BOT_TOKEN')
```
