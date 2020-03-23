# Surgical Assistant Event Driven File

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from googletrans import Translator

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(message.author)
    comments = {
            "qwerty":"Come on now, let's not type gibberish!",
            "lettuce":"Lettuce shouldn't go on hamburgers (@bergermaestru himself told me)",
            "mayonnaise":"Mayonnaise?! no. stop. gross.",
            "robot":"beep boop. I will take over the world",
            "surgery":"oh yes, about that. I've decided not to use an anasthetic",
            "pokemon":"gotta catch 'em all!",
            "beep":"boop",
            "ping":"pong",
            "compiler":"maybe you should compile your life together first",
            "emotions":"robots don't have emotions",
            "romeo":"what about Juliet? wow. sexist.",
            "smurf":"fa la la la la la, sing a happy song",
            "spongebob":"who lives in a pinecone under the forest?... *wait thats not how it goes...*",
            "kiss":"robots don't show affection",
            "coronavirus":"robots don't get sick. suck it.",
            "ugly":"no u",
            "weather":"oh come on, don't be lazy. I'm not *that* helpful",
            "can someone":"No one cares."
        }
    if message.author == client.user:
        return
    
    for key in comments:
        if key in message.content.lower():
            await message.channel.send(comments[key])
            return

client.run(TOKEN)
