#/env/bin/Python3
# https://discord.gg/79Zn3n

### Libraries 
import os, discord, requests, logging
from discord.ext import commands

### Logging ON
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Init discord client and bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	bot.status = "Protecting security"
	print('We have logged in as {0.user}'.format(bot))

@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send('Hi!')

@bot.command(pass_context=True)
async def check(ctx, mail):
    await ctx.send('This is your mail {0}'.format(mail))

if __name__ == "__main__":
    TOKEN = os.getenv('TOKEN')
    bot.run(TOKEN)
