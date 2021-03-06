import discord
from discord.ext import commands
import random
import os
import pathlib

description = "luigi luigi luigi"
bot = commands.Bot(command_prefix='L! ', description=description, case_insensitive=True)

# start up
@bot.event
async def on_ready():
    print("Logged in as {}".format(bot.user.name))

# load quotes
quotes = []
with open ('assets/quotes.txt', 'rt') as quotefile:
    for quoteline in quotefile:
        quotes.append(quoteline)

# test command
@bot.command()
async def test(ctx):
    await ctx.send("its a-me, luigi <3")

# quote command
@bot.command()
async def quote(ctx):
    quote = quotes[random.randrange(0, len(quotes))]
    await ctx.send(quote)

# image command
@bot.command()
async def pic(ctx):
    path = str(pathlib.Path(__file__).parent.absolute()) + '/assets/pictures'
    pic = os.path.join(path, random.choice(os.listdir(path)))
    await ctx.send(file=discord.File(pic))

bot.run('TOKEN')