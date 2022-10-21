#!/usr/bin/python3

# --------- Libraries --------- #

import hikari, lightbulb
from lightbulb.ext import tungsten
from dotenv import load_dotenv
from os import getenv
from datetime import datetime
from re import match

# --------- Functions---------- #

# Wow, such empty

# ---------- Globals ---------- #

load_dotenv()
bot = lightbulb.BotApp(token=getenv('TOKEN'), intents=hikari.Intents.ALL)
botuser = bot.get_me()
botversion = "1.0.0"

# --------- Listeners --------- #

# Error handler
@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent):
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"""Une erreur est survenue lors de l'invocation de la commande `{event.context.command.name}`.
Je le fais savoir à DarkblooM pour qu'il se penche sur ce cas.""")
#         file = open(f"./error_logs/{datetime.today().strftime('%Y-%m-%d')}.txt", "a+")
#         file.write(f"""{datetime.today().strftime('%H:%M:%S')}
# Member: {event.context.member.username}{event.context.member.discriminator}
# Command: {event.context.invoked.name}
# Channel: {event.context.get_channel().name}
# Cause: {event.exception.original}

# """)
#         file.close()
    raise event.exception

# New member listener
@bot.listen(hikari.MemberCreateEvent)
async def new_member(event: hikari.MemberCreateEvent):
    channel = await event.app.rest.fetch_channel(1031689089382109226)
    content = f"Hey <@{event.user_id}> ! Bienvenue chez la Swag Family !"
    await event.app.rest.create_message(channel=channel, content=content, attachment=event.user.avatar_url)
    return

# ------ Single commands ------ #

# About command
@bot.command
@lightbulb.command('apropos', 'À propos de Swagbot')
@lightbulb.implements(lightbulb.SlashCommand)
async def apropos(ctx):
    embed = (
        hikari.Embed(title=f"Swagbot (v{botversion})", description="Bot multifonction développé pour la communauté de MamanSwag", color="#FF33BC")
        .add_field("Auteur", "DarkblooM#8472")
        .add_field("Langage", "Python")
    )
    await ctx.respond(embed)
    return

# Social command
@bot.command
@lightbulb.command('social', 'Les liens utiles')
@lightbulb.implements(lightbulb.SlashCommand)
async def social(ctx):
    await ctx.respond("""Suis MamanSwag partout !
**__Twitch__ :** <https://twitch.tv/mamanswag>
**__YouTube__ :** <https://youtube.com/c/MamanSwag>
**__Twitter__ :** <https://twitter.com/SwagMaman>
**__TikTokk__ :** <https://www.tiktok.com/@mamanswag>

Visite aussi le site web !
<https://mamanswag.tv/>""")
    return

# ----- Argument commands ----- #

# Avatar command
@bot.command
@lightbulb.option("membre", "Le membre dont tu veux récupếrer l'avatar")
@lightbulb.command("avatar", "Récupère l'avatar d'un membre du serveur")
@lightbulb.implements(lightbulb.SlashCommand)
async def avatar(ctx):
    if not match(r"^<@\d+>$", ctx.options.membre):
        await ctx.respond("L'argument reçu n'est pas un membre du serveur")
        return
    id = int(ctx.options.membre[2:len(ctx.options.membre) - 1])
    user = ctx.app.cache.get_user(id)
    if user == None:
        user = await ctx.app.rest.get_user(id)
    await ctx.respond(attachment=user.avatar_url)
    return

# ------ Command groups ------ #

# Wow, such empty

# ---------- Run bot ---------- #

bot.run()