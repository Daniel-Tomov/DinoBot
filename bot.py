######  Copyright 2022 Daniel Tomov  #######

import discord
import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

import random
import chatbot
import asyncio

name = 'DinoBot'
alias = "dino"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #print(f'Message from {message.author}: {message.content}')

        author = str(message.author)
        if author == "DinoBot#0260":
            return


        m_Lower = str(message.content).lower()
        m = str(message.content)

        # The famous "Im" command most bots have
        if (('i\'m ' in m_Lower) or ('im ' in m_Lower) or (' i\'m ' in m_Lower) or (' im ' in m_Lower) or ('i am ' in m_Lower) or (' i am ' in m_Lower)):

            if 'im dinobot' in m_Lower:
                await message.channel.send("Your not DinoBot, I'm DinoBot!")
                return

            #print(m.find('im'))
            if m_Lower.find('i\'m') != -1:
                loc = m_Lower.find('i\'m') + 3
                #print(loc)
                #print(m[loc:len(m)])
                text = m[loc:len(m)]
            
            elif m_Lower.find('im') != -1:
                loc = m_Lower.find('im') + 3
                #print(loc)
                #print(m[loc:len(m)])
                text = m[loc:len(m)]

            rand = random.randint(0,1)

            if rand == 0:
                await message.channel.send("Hello \"" + text + "\", I'm " + name + "!")
            elif rand == 1:
                await message.channel.send("Hello \"" + text + "\", I'm " + name + "!")
            return


        # Silly message to "im" only
        elif m_Lower == "im" or m_Lower == 'i am':
            await message.channel.send("Who are you really?")
            return

        # Test Message
        elif message.content.startswith('$hello'):
            await message.channel.send('Hello!')
            return

        # go on to chat model
        elif m_Lower.startswith(name.lower()) or m_Lower.startswith(alias):
            #print(m[8:len(m)])
            
            returnText = await chatbot.async_chat(m_Lower[8:len(m)])
            #print(returnText)
            await message.channel.send(returnText.replace("cleverbot", 'DinoBot').replace("CleverBot", "DinoBot").replace("Cleverbot", "DinoBot"))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)