import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())


def password(length):
    symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    passw = ""
    for i in range(length):
        passw = passw + symbols[random.randint(0, len(symbols) - 1)]
    return passw


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def psw(ctx, length=10):
    await ctx.send(password(length))

bot.run("token")
