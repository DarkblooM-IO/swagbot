#!/usr/bin/python3
import hikari, lightbulb
from dotenv import load_dotenv
from os import getenv
from datetime import datetime
from re import match
from pyfiglet import Figlet

def getUserIdFromArg(arg):
    if not match(r"^<@\d+>$", arg):
        return None
    return int(arg[2:len(arg) - 1])

plugin = lightbulb.Plugin("single_commands")

load_dotenv()
botversion = getenv("VERSION")
embedColor = f"#{getenv('EMBEDCOLOR')}"

# Avatar command
@plugin.command
@lightbulb.option("membre", "Le membre dont tu veux récupếrer l'avatar")
@lightbulb.command("avatar", "Récupère l'avatar d'un membre du serveur")
@lightbulb.implements(lightbulb.SlashCommand)
async def avatar(ctx):
    id = getUserIdFromArg(ctx.options.membre)
    if id == None:
        await ctx.respond("L'argument reçu n'est pas un membre")
        return
    user = ctx.app.cache.get_user(id)
    if user == None:
        user = await ctx.app.rest.get_user(id)
    await ctx.respond(attachment=user.avatar_url)
    return

# Figlet command
@plugin.command
@lightbulb.option("texte", "Le texte que tu veux transformer")
@lightbulb.command("figlet", "Transforme du texte en lettres géantes")
@lightbulb.implements(lightbulb.SlashCommand)
async def figlet(ctx):
    await ctx.respond(f""":warning: Rend moins bien sur mobile
```
{Figlet().renderText(ctx.options.texte)}
```""")
    return

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)