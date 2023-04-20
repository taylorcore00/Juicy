import discord
from discord.ext import commands
from discord.ui import Button, View
from discord import Embed, Message
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi
import asyncio
import datetime
import pytz
import requests
arg_tz = pytz.timezone('America/Argentina/Buenos_Aires')
bot = discord.ext.commands.Bot(command_prefix='.', intents = discord.Intents.all())
start_time = datetime.datetime.now()

# message_id = 123456789012345678
# channel_id = 1095505616459546644
# channel = bot.get_channel(channel_id)
# message = channel.fetch_message(message_id)

# ID del canal permitido
allowed_channel = 1095505616459546644
    

@bot.event
async def on_ready():
    embed = discord.Embed(title="",description="",color=0x00FF00)
    embed.add_field(name="Estado",value="```\n🟢 En linea\n```",inline=True)
    embed.add_field(name="🌐  | Total servidores",value=f"```\n{len(bot.guilds)}\n```",inline=True)
    embed.add_field(name="| Bot Invite",value="```\nhttps://discord.gg/GAjSbah6\n```",inline=False)
    channel = bot.get_channel(1098595724742099055)
    mensaje = await channel.fetch_message(1098617921997115503)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".Help"))
    status = await mensaje.edit(embed = embed)
    print(f"Conectado como: {bot.user}")
    bot.add_view(Roles())
    @bot.command(aliases=["quit"])
    @commands.has_permissions(administrator=True)
    async def close(ctx):
        embed = discord.Embed(title="",description="",color=0xFF0000)
        embed.add_field(name="Estado",value="```\n🔴 Offline\n```",inline=True)
        embed.add_field(name="🌐  | Total servidores",value=f"```\n{len(bot.guilds)}\n```",inline=True)
        embed.add_field(name="Bot Invite",value="```\nhttps://discord.gg/GAjSbah6\n```",inline=False)
        await status.edit(embed = embed)
        await bot.close()

class Roles(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="👤 Usuario",custom_id="Usuario",style=discord.ButtonStyle.grey )
    async def usuario(self, interaction, button):
        anunciosid = 1001611392694112447
        user = interaction.user
        if anunciosid in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(anunciosid))
            await interaction.response.send_message("Tu rol fue eliminado con exito",ephemeral = True)
        else:
            await user.add_roles(user.guild.get_role(anunciosid))
            await interaction.response.send_message("Tu rol fue agregado con exito",ephemeral = True)
    @discord.ui.button(label="📣 Anuncios",custom_id="Anuncios",style=discord.ButtonStyle.primary )
    async def annonce(self, interaction, button):
        anunciosid = 1097530287036039269
        user = interaction.user
        if anunciosid in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(anunciosid))
            await interaction.response.send_message("Tu rol fue eliminado con exito",ephemeral = True)
        else:
            await user.add_roles(user.guild.get_role(anunciosid))
            await interaction.response.send_message("Tu rol fue agregado con exito",ephemeral = True)
    @discord.ui.button(label="🎉 Sorteos",custom_id="Sorteos",style=discord.ButtonStyle.danger )        
    async def sorteos(self, interaction, button):
        sorteosid = 1097530311178473603
        user = interaction.user
        if sorteosid in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(sorteosid))
            await interaction.response.send_message("Tu rol fue eliminado con exito",ephemeral = True)
        else:
            await user.add_roles(user.guild.get_role(sorteosid))
            await interaction.response.send_message("Tu rol fue agregado con exito",ephemeral = True)

@bot.command()
async def roles(ctx):
    embed = discord.Embed(title="SISTEMA DE AUTO-ROLES",description="```\nHaz click en alguna reacción para adquirir o eliminar un role deseado.\n```",color=0x2596be)
    embed.set_footer(text="TayAssist",icon_url="https://media.discordapp.net/attachments/1001644299949183079/1097524781252882452/soporte-tecnico.png")
    await ctx.send(embed = embed,view = Roles())

# @bot.command
# async def imagenes(ctx):
#     if ctx.author == bot.user:
#         return
#     if ctx.content.startswith('.imagenes'):
#         query = ctx.content[10:]
#         response = requests.get('https://www.google.com/search?q=' + query + '&tbm=isch')
#         soup = BeautifulSoup(response.text, 'html.parser')
#         images = soup.find_all('img')
#         image_urls = []
#         for image in images:
#             url = image['src']
#             if not url.endswith('.gif'):
#                 image_urls.append(url)
#         max_index = min(4, len(image_urls) - 1) # máximo índice de la imagen que se puede mostrar
#         index = 0 # índice de la imagen actualmente mostrada
#         msg = await ctx.channel.send(image_urls[index]) # envía la imagen actual
#         if len(image_urls) > 1: # solo si hay más de una imagen
#             await msg.add_reaction('⬅️') # agregar la reacción de la flecha hacia la izquierda
#             await msg.add_reaction('➡️') # agregar la reacción de la flecha hacia la derecha

#             def check(reaction, user):
#                 return user == ctx.author and reaction.ctx.id == msg.id and reaction.emoji in ['⬅️', '➡️']

#             while True:
#                 try:
#                     reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
#                     if reaction.emoji == '⬅️':
#                         index = max(0, index - 1) # decrementa el índice de la imagen actual
#                     elif reaction.emoji == '➡️':
#                         index = min(max_index, index + 1) # incrementa el índice de la imagen actual
#                     await msg.edit(content=image_urls[index]) # muestra la nueva imagen
#                     await reaction.remove(user) # elimina la reacción del usuario
#                 except:
#                     break # el usuario no respondió dentro del tiempo límite



@bot.command()
async def vtlink(ctx,link):
    api = "API TOKEN VT"
    url = link
    vt = VirusTotalPublicApi(api)
    url_report = vt.get_url_report(url)
    total = url_report['results']['total']
    pos = url_report['results']['positives']
    page = url_report['results']['permalink']
    if pos > 0:
        #si entra por el if EL ARCHIVO ES MALICIOSO
        embed = discord.Embed(title= f"🛑 | ¡El link es malicioso! {pos}/{total}",color=0xFf1200,url=page)
        for key in url_report['results']['scans']:
            if url_report['results']['scans'][key]["detected"] == True:
                result = url_report['results']['scans'][key]['result']
                embed.add_field(name=f"{key} `{result}`",value=f"",inline=False)
                embed.set_thumbnail(url="https://cdn3d.iconscout.com/3d/premium/thumb/malware-5161207-4323229.png")
                embed.set_footer(text="scaneo de url | managed by: Taylor.dll#1539")
    else:
        embed = discord.Embed(title= f"🌐 | ¡El link es seguro! {pos}/{total}",description=f"Ningun **Enginee** lo detecto como **Malware**\n```\n{pos} malware\n```",color=0x008cff,url=page)
        # result = url_report['results']['scans'][key]['result']
        embed.set_thumbnail(url="https://murrayofmelbourne.files.wordpress.com/2022/11/6eb7e83d-4b16-4efa-8422-22120e79452e.png")
        embed.set_footer(text="scaneo de url | managed by: Taylor.dll#1539")
    await ctx.send(embed = embed)


@bot.command()
async def form(ctx): #COMANDO PARA EL FORMULARIO DE MECANICO
    role = discord.utils.get(ctx.guild.roles, id=1093897953854357625)
    aca = bot.get_guild(1072874852026961972)
    if role in ctx.author.roles: #es un if para comprobar si el que usa el comando esta en la lista de roles permitidos para acceder a esto
        emoji1 = discord.utils.get(bot.emojis, name='discordstaffgift')
        emoji2 = discord.utils.get(bot.emojis, name='yellowarrow')
        embed = discord.Embed(title=f"{emoji1} Formulario Mecanico A.C.A AlRitmo 2.0", description=f" {emoji2} **Nombre IC**:\n\n {emoji2} **Diferencias entre IC/OOC:**\n\n {emoji2} **Pregunta #1: ¿Qué es VDM? Dar un ejemplo **\n\n {emoji2} **Pregunta #2: ¿Qué es DM? Dar un ejemplo **\n\n {emoji2} **Pregunta #3: Qué es MG? Dar un ejemplo **\n\n {emoji2} **Pregunta #4: ¿Qué es PG? Dar un ejemplo  **\n\n {emoji2} **Pregunta #5: ¿Para que usamos el /me? Da ejemplos sobre mecanico.**\n\n {emoji2} **Pregunta #6: ¿Para que usamos el /do? Da ejemplos sobre mecanico.**\n\n {emoji2} **Pregunta #7: ¿Qué es forzar rol a alguien? Da un ejemplo**\n\n {emoji2} **Pregunta #8: ¿Podemos usar nuestros vehiculos personales como movilidad estando en servicio? ¿Por qué?**",
        color = 0xFF4500)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1960/1960910.png")
        embed.set_footer(text="sistema de formularios propios | managed by: Taylor.dll#1539")
        await ctx.send(embed=embed)
    else:
        embed = Embed(title="", color=0xFF4500)
        embed.set_footer(text=f"No tienes los suficientes permisos para ejecutar este comando o este comando solo se ejetuta en {aca.name}.",icon_url="https://cdn.staticcrate.com/stock-hd/effects/footagecrate-red-error-icon-prev-full.png")
        await ctx.send(embed = embed)

@bot.command()
async def Help(ctx):
    aca = bot.get_guild(1072874852026961972)
    emoji4 = discord.utils.get(bot.emojis, name='cog_gear_work_machine18')
    user = ctx.author
    embed = discord.Embed(title=f"📘 Informacion sobre comandos",description="",color=0x0083FF)
    embed.add_field(name="Informacion sobre un usuario",value="➛ `.userinfo`",inline=False)
    embed.add_field(name="Link Scanner",value="➛ `.vtlink` https://chat.openai.com/ ",inline=False)
    embed.add_field(name="Entrar y salir de servicio",value="➛ `.entrar` y/o ➛ `.salir`",inline=False)
    embed.add_field(name="Formulario",value="➛ `.form`",inline=True)
    embed.add_field(name="habilitado unicamente en:",value=f"`{aca.name}`",inline=True)
    embed.add_field(name="",value="📩 Discord and support | `proximamente`",inline=False)
    embed.set_footer(text="menu help | managed by: Taylor.dll#1539")
    await ctx.reply(embed=embed)

@bot.command()
async def entrar(ctx):
    command_time = ctx.message.created_at
    formatted_time = command_time.strftime("%H:%M:%S") 
    user = ctx.author
    await ctx.message.delete()
    emoji1 = discord.utils.get(bot.emojis, name='discordstaffgift')
    embed = Embed(title=f"{emoji1} Información", description=f"{user.mention} ✅ ha **entrado** en servicio!", color=0x00ff00)
    embed.add_field(name="Hora de entrada", value=f"{formatted_time}", inline=False)
    embed.set_footer(text="entrada | managed by: Taylor.dll#1539")
    await ctx.send(embed=embed)

@bot.command()
async def salir(ctx):
    command_time = ctx.message.created_at
    formatted_time = command_time.strftime("%H:%M:%S") 
    role = discord.utils.get(ctx.guild.roles, id=1094752993112498317) #id del role mecanico
    user = ctx.author
    await ctx.message.delete()
    emoji1 = discord.utils.get(bot.emojis, name='discordstaffgift')
    embed = Embed(title=f"{emoji1} Información", description=f"{user.mention} 📛 ha **salido** de servicio!", color=0x00FF0000)
    embed.add_field(name="Hora de salida", value=f"{formatted_time}", inline=False)
    embed.set_footer(text="salida | managed by: Taylor.dll#1539")
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: discord.Member = None): #COMANDO USERINFO
    emoji3 = discord.utils.get(bot.emojis, name='info')
    if member == None:
        member = ctx.author
    roles = [role.name for role in member.roles] 
    embed = discord.Embed(title=f"{emoji3} Información del miembro", description=member.mention, color=0x339CFF)
    embed.add_field(name="Nombre", value=member.name, inline=True)
    embed.add_field(name="Apodo", value=member.nick, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Fecha de ingreso al servidor", value=member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)
    embed.add_field(name="Fecha de creación de la cuenta", value=member.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
    embed.add_field(name=f"Roles de {member.name}", value=', '.join(roles), inline=False)
    embed.set_thumbnail(url=member.avatar)
    embed.set_footer(text="user info | managed by: Taylor.dll#1539")
    await ctx.send(embed=embed)

@bot.command()
async def img(ctx, member: discord.Member = None): #comando para obtener la imagen del perfil de un user determinado
    if member == None:
        member = ctx.author
    embed = discord.Embed(title="",description="",color=0x339CFF)
    embed.set_image(url=member.avatar)
    embed.set_author(name=member.name,icon_url=member.avatar)
    embed.set_footer(text=f"Comando usado por {ctx.author}")
    await ctx.reply(embed=embed)


bot.run('T O K E N')