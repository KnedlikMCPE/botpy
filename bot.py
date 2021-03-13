import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(message):
    await message.send('pong')

client.run('ODIwMzI0MDc5NTE2MjU0MjIw.YEzgVQ.H5fRyiMktiYAlAqckZ6JTTA5UZ0')
