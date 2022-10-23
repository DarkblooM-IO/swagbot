#!/usr/bin/python3
import hikari, lightbulb
from dotenv import load_dotenv
from os import getenv

plugin = lightbulb.Plugin("single_commands")

load_dotenv()
botversion = getenv("VERSION")
embedColor = f"#{getenv('EMBEDCOLOR')}"

# About command
@plugin.command
@lightbulb.command('apropos', 'À propos de Swagbot')
@lightbulb.implements(lightbulb.SlashCommand)
async def apropos(ctx):
    embed = (
        hikari.Embed(title=f"Swagbot (v{botversion})", description="Bot multifonction développé pour la communauté de MamanSwag", color=embedColor)
        .add_field("Auteur", "DarkblooM#8472")
        .add_field("Code source", "https://github.com/DarkblooM-SR/swagbot")
    )
    await ctx.respond(embed)
    return

# Patch note command
@plugin.command
@lightbulb.command('patchnote', 'Informations sur le dernier patch')
@lightbulb.implements(lightbulb.SlashCommand)
async def patchnote(ctx):
    embed = hikari.Embed(title="Patch note", color=embedColor)
    embed.add_field("Version", botversion)
    if "beta" in botversion:
        embed.add_field("Disclaimer", "Je suis encore en beta ! Il se peut que je ne fonctionne pas toujours corrèctement, alors soyez patients avec moi.")
    embed.add_field("Contenu", "Lancement du bot")
    await ctx.respond(embed)
    return

# Social command
@plugin.command
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

# Dixper command
@plugin.command
@lightbulb.command("dixper", "Inscris-toi sur Dixper !")
@lightbulb.implements(lightbulb.SlashCommand)
async def dixper(ctx):
    await ctx.respond("""INSCRIS-TOI maintenant sur <https://dixper.gg/MamanSwag>
Pourquoi ? Car tu vas donner un tout autre sens à mes lives !! :wink:""")
    return

# Epic code command
@plugin.command
@lightbulb.command("epic", "Code créateur Epic Games")
@lightbulb.implements(lightbulb.SlashCommand)
async def epic(ctx):
    await ctx.respond("""CODE CRÉATEUR : mamanswag
Merci pour ton soutien :heartpulse: :hugging:""")
    return

def load(bot):
    bot.add_plugin(plugin)