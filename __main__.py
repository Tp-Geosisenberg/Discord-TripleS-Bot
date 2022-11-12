import discord
from discord.utils import get
from discord.ext import commands
from datetime import datetime, timedelta
from __song__ import songAPI 
from os import name
import discord
from discord import channel
from discord import message
from discord import voice_client
from discord.ext import commands
from discord.ext.commands.core import Command
from discord.utils import get 
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import youtube_dl
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from discord.ext import commands
token='' #Change for your token at here
bot = commands.Bot(command_prefix='?')

songsInstance = songAPI()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send("You typed {0}".format(par))

@bot.command(aliases=['p']) 
async def play(ctx,* ,search: str):
    await songsInstance.play(ctx, search)

@bot.command()
async def stop(ctx):
    await songsInstance.stop(ctx)

@bot.command()
async def pause(ctx):
    await songsInstance.pause(ctx)

@bot.command()
async def resume(ctx):
    await songsInstance.resume(ctx)

@bot.command()
async def leave(ctx):
    await songsInstance.leave(ctx)

@bot.command()
async def queueList(ctx):
    await songsInstance.queueList(ctx)

@bot.command(aliases=['s'])
async def skip(ctx):
    await songsInstance.skip(ctx)

bot.run(token)
