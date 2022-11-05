#!/usr/bin/python3

# --------- Libraries --------- #

import hikari, lightbulb
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

# ---------- Globals ---------- #

load_dotenv()
bot = lightbulb.BotApp(token=getenv('TOKEN'), intents=hikari.Intents.ALL, prefix="!")

# --------- Listeners --------- #

# Error handler
@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent):
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"""Une erreur est survenue lors de l'invocation de la commande `{event.context.command.name}`.
Je le fais savoir à DarkblooM pour qu'il se penche sur ce cas.""")
        with open(f"./error_logs/{datetime.today().strftime('%Y-%m-%d')}.txt", "a+") as file:
            file.write(f"""{datetime.today().strftime('%H:%M:%S')}
Member: {event.context.member.username}{event.context.member.discriminator}
Command: {event.context.invoked.name}
Channel: {event.context.get_channel().name}
Cause: {event.exception.original}

""")
    elif isinstance(event.exception, lightbulb.MissingRequiredPermission):
        await event.context.respond("Désolé, je ne crois pas que tu ai le droit de faire ça")
    raise event.exception

# New member listener
@bot.listen(hikari.MemberCreateEvent)
async def new_member(event: hikari.MemberCreateEvent):
    channel = await event.app.rest.fetch_channel(int(getenv("WELCOME_CHANNEL")))
    content = f"Hey {event.user.mention} ! Bienvenue chez la Swag Family !"
    await event.app.rest.create_message(channel=channel, content=content, attachment=event.member.avatar_url)
    return

# ------- Load Commands ------- #

bot.load_extensions_from("extensions")

# - Extensions reload command - #

@bot.command
@lightbulb.add_checks(lightbulb.checks.has_role_permissions(hikari.Permissions().ADMINISTRATOR))
@lightbulb.command("reload", "reload")
@lightbulb.implements(lightbulb.PrefixCommand)
async def reload(ctx):
    bot.reload_extensions(*bot.extensions)
    await ctx.respond("Reloaded successfully")
    return

# ---------- Run bot ---------- #

bot.run()