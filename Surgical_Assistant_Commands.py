# code for the bot Surgical Assistant - commands

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from googletrans import Translator
from googletrans import LANGUAGES

# get the bot token from the file .env in same directory
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# create translator for $trans command
translator = Translator()
bot = commands.Bot(command_prefix="$")

@bot.command(name="trans", help="Translates a message from any language into the specified language")
async def translate(ctx, dest_lang, *, message):
        translation = translator.translate(message, dest = dest_lang)
        await ctx.send(translation.origin + " :arrow_right: " + translation.text + "\n(" + translation.src + " :arrow_right: " + translation.dest + ")")

@bot.command(name="lang", help="Shows the two letter language code for given language")
async def show_lang(ctx, lang):
        for code, language in googletrans.LANGUAGES.items:
                if lang in language.lower():
                        await ctx.send(code)
                        return

# run the bot on the discord server
bot.run(TOKEN)
