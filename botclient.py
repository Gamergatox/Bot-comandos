import discord
from bot_logic import gen_pass
from discord.ext import commands
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$", intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send("hola, para que soy bueno?")
@bot.command()  
async def bye(ctx):
    await ctx.send("ya vete xd") }
@bot.command()  
async def dfkjdfkjdfjkdfjk(ctx):
    await ctx.send("No se lo que dijo pero miente")
@bot.command()   
async def password(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def joined_server(ctx, member: discord.Member):
    await ctx.send (f' {member.name} joined this server on {discord.utils.format_dt(member. joined at)}')
@bot.command()
async def joined_discord(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined Discord on {discord.utils.format_dt(member created at)}')      
bot.run("Token")
