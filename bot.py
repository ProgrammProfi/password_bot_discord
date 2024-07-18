import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())

passwords = {
}


def password_gen(length):
    symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    passw = ""
    for i in range(length):
        passw = passw + symbols[random.randint(0, len(symbols) - 1)]
    return passw


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def gen_psw(ctx, length=10):
    await ctx.send(password(length))


@bot.command()
async def my_psw(ctx, site):
    await ctx.send(passwords[site])


@bot.command()
async def edit_psw(ctx, site, passw):
    passwords[site] = passw
    await ctx.send(f"OK {site} - {passw}")


@bot.command()
async def del_psw(ctx, site):
    del passwords[site]
    await ctx.send(f"OK {site} deleted")
    
bot.run("token")
