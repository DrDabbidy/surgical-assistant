# code for the bot Surgical Assistant - commands

import os
import subprocess
import discord
import random
#from sympy import preview
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from googletrans import Translator

# get the bot token from the file .env in same directory
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'filipino',
    'he': 'hebrew'
}
LANGCODES = dict(map(reversed, LANGUAGES.items()))

# create translator for $trans command
translator = Translator()
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

# # set up the mongodb client
# myClient = pymongo.MongoClient("mongodb://localhost:27017/")
# # create the db or switch to it
# myDB = myClient["surgical_assistant"]
# # enter the users collection

# COMMANDS
@bot.command(name="trans", help="Translates a message from any language into the specified language")
async def translate(ctx, dest_lang, *, message):
        translation = translator.translate(message, dest = dest_lang)
        await ctx.send(translation.origin + " :arrow_right: " + translation.text + "\n(" + translation.src + " :arrow_right: " + translation.dest + ")")

@bot.command(name="lang", help="Shows the two letter language code for given language")
async def show_lang(ctx, *, lang):
        if lang.lower() in LANGCODES:
            await ctx.send(LANGCODES[lang.lower()])
        elif lang.lower() == "chinese":
            await ctx.send('''Please specify "chinese (traditional)" or "chinese (simplified)".''')
        else:
            await ctx.send("Not a valid language!")
        return

@bot.command(name="troll", help="Takes your message and makes it into troll text: hello -- > h E l L o")
async def make_troll_text(ctx, *, message):
    out = message[:1]
    uppercase = True
    for c in message[1:]:
        if c in '''.,!@#$%^&*()_-<>/?'";:[{\\|`~}]"'+=''':
            if uppercase:
                out += c.upper()
            else:
                out += c.lower()
        else:
            if uppercase:
                out += " " + c.upper()
            else:
                out += " " + c.lower()
        if random.randint(0,1) == 0:
            uppercase = not uppercase
    await ctx.message.delete()
    await ctx.send(out + "\n(" + str(ctx.message.author.display_name) + ")")

@bot.command(name="roles", help="Lists all available roles that you can add to yourself (e.g. school courses, etc.)")
async def list_roles(ctx):
    roles = ctx.message.guild.roles;
    message = ""
    for role in roles:
        message += role.name + "\n"
    embed = discord.Embed(
        title="The Spitalul Roles!",
        color=discord.Color(0x2b3f58),
        description=message
    )
    await ctx.send(embed=embed)

@bot.command(name="myroles", help="Lists all roles that you currently have (e.g. school courses, etc.)")
async def list_roles(ctx):
    roles = ctx.message.author.roles;
    message = ""
    for role in roles:
        message += role.name + "\n"
    embed = discord.Embed(
        title=ctx.message.author.display_name + "'s Roles!",
        color=discord.Color(0x2b3f58),
        description=message
    )
    await ctx.send(embed=embed)

@bot.command(name="createrole", help="Create a default role with no permissions")
async def create_role(ctx, *, name):
    await ctx.message.guild.create_role(name=name, mentionable=True)
    await ctx.send("Created role {}".format(name))

@bot.command(name="getrole", help="Give yourself the role that you specify if you have the permissions")
async def give_role(ctx, *, name):
    for role in ctx.message.guild.roles:
        if role.name == name:
            if role.permissions == discord.Permissions.none():
                await ctx.message.author.add_roles(role)
                await ctx.send("Added {} to you!".format(role))

@bot.command(name="removerole", help="Removes the given role from yourself")
async def remove_role(ctx, *, roleName):
    role = get(ctx.message.guild.roles, name=roleName)
    if role == None:
        await ctx.send("No such role exists...")
    elif role.permissions == discord.Permissions.none():
        await ctx.author.remove_roles(role)
        await ctx.send("Removed {} from you!".format(role))

@bot.command(name="deleterole", help="Deletes the given role (need admin permissions)")
async def delete_role(ctx, *, roleName):
    role = get(ctx.message.guild.roles, name=roleName)
    if get(ctx.message.guild.roles, name="chirurg") in ctx.message.author.roles:
        if role == None:
            await ctx.send("No such role exists...")
        else:
            await role.delete()
            await ctx.send(f"Deleted {role}!")
    else:
        await ctx.send("Go back to med school for a few years to gain the ability to do that!")

async def render_latex(ctx, textColour, bgColour, message):
    preamble = f"\\documentclass[14pt]{{article}}" \
        f"\\usepackage[active,tightpage]{{preview}}" \
        f"\\usepackage[usenames,dvipsnames,svgnames,table]{{xcolor}}" \
        f"\\usepackage{{amsmath}}" \
        f"\\usepackage{{amssymb}}" \
        f"\\usepackage{{mathtools}}" \
        f"\\usepackage{{pgfplots}}" \
        f"\\pgfplotsset{{width=10cm,compat=1.16}}" \
        f"\\usepackage{{color}}" \
        f"\\usepackage[utf8]{{inputenc}}" \
        f"\\definecolor{{dstext}}{{HTML}}{{{textColour}}}" \
        f"\\definecolor{{dsbackground}}{{HTML}}{{{bgColour}}}" \
        f"\\begin{{document}}" \
        f"\\begin{{preview}}" \
        f"\\color{{dstext}}" \
        f"\\pagecolor{{dsbackground}}" \
        f"\\begin{{huge}}"
    if message[:3] == "```" and message[-3:] == "```":
        message = message[3:-3]
    elif message[0] == "`" and message[-1] == "`":
        message = message[1:-1]
    
    formattedMessage = r"{}".format(message)

    texfile = open("file.tex", "w")
    texfile.write(preamble + formattedMessage + "\\end{huge}\\end{preview}\\end{document}")
    texfile.close()

    try:
        # create pdf from tex and convert to png
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "file.tex"])
        # os.system("pdflatex file.tex")
        # os.system("convert -density 1200 -quality 90 -trim file.pdf image.png")
        os.system(f"convert -density 1200 -quality 90 -background \"#{bgColour}\" -flatten file.pdf image.png")
    except:
        await ctx.send(embed=discord.Embed(
            title= "Render Error!",
            color=discord.Color(0x2b3f58),
            description="An error has occured... please try again"
        ).set_thumbnail(url="https://statsify.net/img/assets/error.gif"))
    # preview(formattedMessage + "\n\\end{huge}\\end{document}", viewer="file", filename="image.png", euler=False, preamble=preamble, dvioptions=['-D','1200'])
    await ctx.send("**" + ctx.message.author.display_name + "**:", file=discord.File("image.png"))
    os.remove("image.png")
    os.remove("file.tex")
    os.remove("file.pdf")

def proccessTags(message, possibleTags):
    tags = []
    for i in range(len(possibleTags)):
        index = message.find(" ")
        if index != -1 and message[:index] in possibleTags:
                tags.append(message[:index])
                message = message[index+1:]
        else:
            return tags, message
    return tags, message

@bot.command(name="latex", help="Returns a rendered image of the given latex source, give an optional theme tag -light for light theme")
async def latex(ctx, *, message):
    tags, message = proccessTags(message, ["-d", "-light"])
    
    if "-light" in tags:
        await render_latex(ctx, "000000", "FFFFFF", message)
    else:
        await render_latex(ctx, "FFFFFF", "36393E", message)
    if "-d" in tags:
        await ctx.message.delete()

@bot.command(name="embed", help="Makes a nice embed that the bot will send, deleting the original message")
async def makeEmbed(ctx, *, message):
    messageEmbed = discord.Embed(
        description=message,
        color=ctx.message.author.color
    )
    
    if ctx.message.attachments:
        messageEmbed.set_image(url=ctx.message.attachments[0].url)
    
    messageEmbed.set_footer(text="Spitalul", icon_url=str(ctx.guild.icon_url))
    messageEmbed.set_author(name=str(ctx.message.author.display_name), icon_url=str(ctx.message.author.avatar_url))
        
    await ctx.send(embed=messageEmbed)
    await ctx.message.delete()
        
# run the bot on the discord server
bot.run(TOKEN)
