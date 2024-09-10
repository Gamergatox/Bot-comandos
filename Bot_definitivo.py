import discord
from discord.ext import commands
from coin_flip import flip_coin
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "$", intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def help_(ctx):
    await ctx.send("Los comandos son $ con alguno de los siguientes: hello, bye, dfkjdfkjdfkjdfjk, password, joined(username) y cool(username)")
@bot.command()
async def hello(ctx):
    await ctx.send("Hola, para que soy bueno?")
@bot.command()  
async def bye(ctx):
    await ctx.send("Ya vete xd")
@bot.command()  
async def dfkjdfkjdfjkdfjk(ctx):
    await ctx.send("No se lo que dijo pero miente")
@bot.command()   
async def password(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
@bot.command()
async def meme_gato(ctx):
    with open('images/Gatomeme.jpg', 'rb') as f:
        
        picture = discord.File(f)
@bot.command()
async def meme_gato1(ctx):
    with open('images/gatomeme2.jpg', 'rb') as f:
        
        picture = discord.File(f)
@bot.command()
async def meme_gato2(ctx):
    with open('images/gatoque.jpg', 'rb') as f:
        
        picture = discord.File(f)
@bot.command()  
async def coin_flip(ctx):
    await ctx.send(flip_coin())

bot.run("Token")
