import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    print(error)

@bot.event
async def on_message(message):
    print("RECEIVED:", message.content)
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send("Yo. I’m alive.")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def bye(ctx):
    await ctx.send("See you later 👋")

@bot.command()
async def lol(ctx):
    await ctx.send("haha.")

@bot.command()
async def okay(ctx):
    await ctx.send("Okay 👍")

@bot.command()
async def gg(ctx):
    await ctx.send("good game👍")

    
bot.run("put your token here")