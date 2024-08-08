# »»————-　IMPORT DISCORD IMPORTANT　————-««

import discord
from discord.ext import commands
from discord.ui import Button, View
from discord import Embed, Message
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext.commands import command, cooldown, MissingRequiredArgument, CommandNotFound, BadArgument, CommandOnCooldown
# »»————-　FIN IMPORT DISCORD 　————-««


# »»————-　IMPORT GENERAL　————-««

import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi
import asyncio
import datetime
import pytz
import requests
# »»————-　FIN IMPORT GENERAL 　————-««


# »»————-　PROPIEDADES DEL BOT 　————-««
bot = discord.ext.commands.Bot(command_prefix='.', intents = discord.Intents.all())
bot.remove_command("help")
# »»————-    FIN PROPIEDADES 　————-««

# »»————-  VAR GENERALES 　————-««

arg_tz = pytz.timezone('America/Argentina/Buenos_Aires')
start_time = datetime.datetime.now()
# message_id = 
# channel_id = 
# channel = bot.get_channel(channel_id)
# message = channel.fetch_message(message_id)
# ID del canal permitido
allowed_channel =   
# »»————-  FIN VAR GENERALES 　————-««


# »»————-———————————————————  EVENTOS DEL BOT 　———————————————————————-««

# »»————-  ON READY + STATUS 　————-««
@bot.event
async def on_ready():
    ***

# »»————-  FIN ON READY + STATUS 　————-««
@bot.event
async def on_command_error(ctx, error):
   ***



# »»————-  SISTEMA DE AUTO-ROLES CON BOTONES　————-««
class Roles(discord.ui.View):
    ***

@bot.command()
@commands.has_permissions(administrator=True)
async def roles(ctx):
   **
# »»————-  FIN SISTEMA DE AUTO-ROLES 　————-««


# »»————-  MOSTRADOR DE IMAGENES GOOGLE (NO FIXED)　————-««
# @bot.command
# async def imagenes(ctx):
#    ***

# »»————-  FIN MOSTRADOR DE IMAGENES GOOGLE (NO FIXED)　————-««



# »»————-  SCANNER URL WITH VIRUSTOTAL　————-««
@bot.command()
***
# »»————-————  FIN SCANNER URL 　————————-««


# »»————-————  FORMULARIO DE MECANICO COMANDO PRIVADO 　————————-««
@bot.command()
async def form(ctx): 
   ***
# »»————-————  FIN FORMULARIO DE MECANICO 　————————-««



# »»————-————  MENU HELP (ACTUALIZAR)　————————-««
@bot.command()
async def Help(ctx):
  **
# »»————-————  FIN MENU HELP　————————-««



# »»————-————  ENTRAR Y SALIR EN SERVICIO - COMANDO PRIVADO　————————-««
@bot.command()
async def entrar(ctx):
    **
@bot.command()
async def salir(ctx):
    **
# »»————-————  FIN ENTRAR Y SALIR EN SERVICIO　————————-««


# »»————-————  INFORMACION DEL USUARIO　————————-««
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    **
# »»————-————  FIN INFORMACION DEL USUARIO　————————-««


# »»————-————  MOSTRAR AVATAR DE UN X USUARIO　————————-««
@bot.command()
async def av(ctx, member: discord.Member = None): #comando para obtener la imagen del perfil de un user determinado
   **
# »»————-————  FIN MOSTRAR AVATAR　————————-««



@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
@commands.has_permissions(administrator=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
   **
    # < ======================== LOG ==================================================>



bot.run('t o k e n')
