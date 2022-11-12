# Discord-TripleS-Bot

![MAPPING](Image/TripleS.png)

You must install ffmpeg because of important this to make function in called bot to play music on your room at a Discord server 

> git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg


If you don't sure to use this, you can looking on the website : https://ffmpeg.org/download.html and you can read step-by-step from the website 


```

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

```
I will show important method of function my code, when you called bot to play music by command something such ? ,! ,@ ,# ,etc bot must to call `__playmusic__()` to play music input by its url or name  

# :star: Update now
-  ***[12/11/22]*** none
# :hankey: Bug and Problems
-  ***[12/11/22]*** Cannot search for or play using song name
