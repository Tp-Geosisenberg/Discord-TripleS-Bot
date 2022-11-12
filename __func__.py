import __import__ 
import discord
from discord import channel
from discord import message
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



bot = commands.Bot(command_prefix='?')

"""
setting prefix
"""

def __bot_online__():
    
    @bot.event
    async def on_ready():
        print('Bot {0.user} Online now !'.format(bot))

    TOKEN = ''  # Your token
    bot.run(TOKEN)


def __autodeletemsg__(*arg , **kwarg):
    # delete msg of bot music@client.event
    @bot.event
    async def on_message(message):

        #* Word split
        word = str(message.content)
        split_word = word.split()

        __word_list__ = ['_p','_P','_play','_Play','PLAY',
                        '_s','_S','_Skip','_SKIP']


        for word in __word_list__:
            if word == split_word[0]:
                await message.channel.purge(limit=1)

        print(message.author.id)


__autodeletemsg__()

def __playmusic__():


    @bot.command(name='play',  aliases=['p'])
    async def play(ctx, url):
        channel = ctx.author.voice.channel
        voice_client = get(bot.voice_clients, guild=ctx.guild)

        if voice_client == None:
            await ctx.channel.send("Joined!")
            await channel.connect()
            voice_client = get(bot.voice_clients, guild=ctx.guild)
        YDL_OPTIONS = {'format' : 'bestaudio' , 'noplaylist' : 'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        if not voice_client.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
            voice_client.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice_client.is_playing()
        else:
            await ctx.channel.send("Already playing song")

__playmusic__()


def __help__(*arg , **kwarg):
    
    @bot.command
    async def help(ctx):
        await ctx.channel.send("help")

__help__()
