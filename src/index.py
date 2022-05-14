import datetime, random, discord, re, aiohttp
from urllib import parse, request
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='A bot for the Discord server')

punching_gifs = ["https://c.tenor.com/b9aXVS6p7ucAAAAC/edens-zero-shiki-granbell.gif","https://i.imgur.com/g91XPGA.gif","https://i.imgur.com/7jErgl1.gif","https://i.imgur.com/hlqNBXp.gif","https://i.imgur.com/jznCcr2.gif","https://i.imgur.com/f2kkp3L.gif", "https://i.imgur.com/cgMbUYX.gif", "https://i.imgur.com/pX1E9uU.gif", "https://i.imgur.com/hODM1tI.gif", "https://i.imgur.com/e4bi40y.gif"]
punching_names = ['Te pego un tate quieto!!', 'Te pego un combo!!', 'Te rebento el hocico!!!','Callao perkin']

kick_gifs = ['https://c.tenor.com/LEgnGzli8VMAAAAC/anime-fight.gif', 'https://c.tenor.com/7te6q4wtcYoAAAAC/mad-angry.gif', 'https://c.tenor.com/2l13s2uQ6GkAAAAM/kick.gif', 'https://c.tenor.com/QxoBMmf2bRwAAAAC/jormungand-anime.gif', 'https://c.tenor.com/f1mFGp6vujkAAAAd/charlotte-window-kick-anime-kick.gif',
             'https://c.tenor.com/kvxt9X-gXqQAAAAC/anime-clannad.gif', 'https://c.tenor.com/D67kRWw_cEEAAAAC/voz-dap-chym-dap-chym.gif', 'https://c.tenor.com/EcdG5oq7MHYAAAAM/shut-up-hit.gif', 'https://c.tenor.com/Lyqfq7_vJnsAAAAC/kick-funny.gif', 'https://c.tenor.com/4zwRLrLMGm8AAAAM/chifuyu-chifuyu-kick.gif']
kick_names = ['Te pego senda patada!', 'Patada voladoraaaaa!','WAPAAAAAAAAA!!']

#PING PONG
@bot.command()
async def ping(ctx):
    await ctx.send('Pong')

#INFO INUTIL LA VERDAD
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Rene Puente Presidente de Chile", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_purple())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://i.pinimg.com/736x/6a/b6/95/6ab695255eba0320b98cbf41915a3842.jpg")

    await ctx.send(embed=embed)

#COMANDO QUE BUSCA UN VIDEO EN YT
@bot.command()
async def yt(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
    #print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('Toma xuxetumare: https://www.youtube.com/watch?v=' + search_results[0])

#COMANDO BUSCA OP.GG
@bot.command()
async def opgg(ctx, user):
    try:
        result = ('https://pubg.op.gg/user/' + user)
        await ctx.send('Toma xuxetumare: ' + result)
    except:
        await ctx.send('ESCRIBE ALGO PO MI XAN')

#COMANDO QUE PEGA UN COMBO A ALGUIEN EN EL SERVER
@bot.command()
async def combo(ctx):
    embed = discord.Embed(
        colour=discord.Colour(0xCE3011),
        description=f"{ctx.author.mention} {(random.choice(punching_names))}"
    )
    embed.set_image(url=(random.choice(punching_gifs)))

    await ctx.send(embed=embed)

#COMANDO QUE PEGA UN PATADA A ALGUIEN EN EL SERVER
@bot.command()
async def patada(ctx):
    embed = discord.Embed(
        colour=(discord.Colour(0xE42C47)),
        description=f"{ctx.author.mention} {(random.choice(kick_names))}"
    )
    embed.set_image(url=random.choice(kick_gifs))

    await ctx.send(embed=embed)

#ANIME MEME
@bot.command()
async def animememe(ctx):
    async with aiohttp.ClientSession() as cd:
        async with cd.get("https://www.reddit.com/r/animememes.json") as r:
            animememes = await r.json()
            embed = discord.Embed(color=discord.Color.random())
            embed.set_image(url=animememes["data"]["children"][random.randint(0, 30)]["data"]["url"])
            embed.set_footer(text=f"Meme sent by {ctx.author}")

            await ctx.send(embed=embed)

#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print('My bot is ready!')

@bot.listen()
async def on_message(message):
    if "hola rene" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('que pa mi xan')
        await bot.process_commands(message)

bot.run('tu-token')



