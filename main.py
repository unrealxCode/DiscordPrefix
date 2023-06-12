from discord.ext import commands
import asyncio



client = commands.Bot(command_prefix='##Nothing##')

    
@client.event
async def on_ready():
    print('Bot is ready.')

         
@client.listen("on_message")
async def me_floor(message):
    if message.content.startswith('?fp'):
            print('Bot is ready.')
client.run('KEY')

# KEY = YOUR DISCORD KEY
