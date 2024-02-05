import discord
from discord.ext import commands
import os
import random 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def plastik(ctx):
    img_name = random.choice(os.listdir('imagess'))
    with open(f'imagess/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)
bot.run("token")
