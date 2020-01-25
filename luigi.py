import discord
from discord.ext import commands
import random

description = "luigi luigi luigi"
bot = commands.Bot(command_prefix='L! ', description=description, case_insensitive=True)

# start up
@bot.event
async def on_ready():
    print("We have logged in as {}".format(bot.user.name))

# load quotes
quotes = []
with open ('quotes.txt', 'rt') as quotefile:
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

bot.run('NjcwNDczNjIwNjAxOTYyNDk5.Xiu5tw.kI8svdiI6rmj012HQfOKsXHvuiw')        