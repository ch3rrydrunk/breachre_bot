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

# Init discord bot-client
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
	bot.status = "Protecting security"
	print('We have logged in as {0.user}'.format(bot))

# API response : r_keys = ['email', 'records', 'isAssigned', 'breaches']
@bot.command(pass_context=True)
async def check(ctx, email):
    r = requests.get(API_address.format(email), params={}, headers = headers)
    if (r.status_code == requests.codes.ok):
        r_dict = r.json()
        if (r_dict['records'] == 0):
            await ctx.send('🙌You are safe!🙌\nBig ups on keeping your password secure!')
        else:
            message = 'Whoopsie! Some of your data may have been compromised!\n'\
                        'Here is a list of resources and types of data leaked\n'
            for breach_d in r_dict['breaches']:
                message += '    Resource: {0}.\n'.format(breach_d['title'])
                message += '    Data type: {0}'.format(breach_d['dataCompromised'])
            await ctx.send(message)
    else:
        await ctx.send('Service seems to be offline.\nPlease, try again in 5 minutes.')

# Set tokens from env variables and config requests headers
if __name__ == "__main__":
    API_address = "https://breachreport.com/portal/api/v1/email/{0}/check"
    TOKEN = os.getenv('TOKEN')
    B_TOKEN = os.getenv('BREACH_TOKEN')
    headers = {'Authorization': B_TOKEN}
    bot.run(TOKEN)