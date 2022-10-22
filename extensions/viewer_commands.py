#!/usr/bin/python3
import hikari, lightbulb

plugin = lightbulb.Plugin("viewer_commands")

# Viewer custom commands
@plugin.command
@lightbulb.command("ajaboy", "Ajaboy")
@lightbulb.implements(lightbulb.SlashCommand)
async def ajaboy(ctx):
    await ctx.respond("Voici notre nouveau copain, Ajaboy ! Toujours fidèle et adorablement gentil ! Il a le swag aussi :hibiscus: Bienvenue à toi :purple_heart:")
    return

@plugin.command
@lightbulb.command("amandine", "Amandine")
@lightbulb.implements(lightbulb.SlashCommand)
async def amandine(ctx):
    await ctx.respond("Voici Amandine, toute gentille et toujours fidèle, elle vient toujours faire un coucou quand elle peut ! C'est un membre swag et oui elle a le SWAG :sunglasses: :white_heart:")
    return

@plugin.command
@lightbulb.command("anahera", "Anahera_Pokiha")
@lightbulb.implements(lightbulb.SlashCommand)
async def anahera(ctx):
    await ctx.respond("Voici notre océan de bonheur ! Passioné de tout, il est toujours bienveillant et adorable ! Partout à la fois ! Nous on t'aime déjà Anahera :hibiscus: :heartpulse:\nVoici son profil swag : <https://www.mamanswag.tv/membre-famille-swag_Anahera_pokiha>")
    return

@plugin.command
@lightbulb.command("anymaa", "Anymaa")
@lightbulb.implements(lightbulb.SlashCommand)
async def anymaa(ctx):
    await ctx.respond("Voici notre Anymaa toujours au top et sympathique ! Tu es plus que bienvenue ! :wink:")
    return

@plugin.command
@lightbulb.command("arthur", "Arthur")
@lightbulb.implements(lightbulb.SlashCommand)
async def arthur(ctx):
    await ctx.respond("Toujours en train de délirer, il est la bonne humeur incarnée, qui pourrait se passer de lui sur ce chat ? Pas moi en tout cas ! Merci à toi pour ta présence :two_hearts:")
    return

@plugin.command
@lightbulb.command("attix", "Attix")
@lightbulb.implements(lightbulb.SlashCommand)
async def attix(ctx):
    await ctx.respond("Il fait parti des premiers viewers réguliers et je l'en remercie beaucoup ! Si vous ne le voyez pas, c'est qu'il vient tard me faire des coucous ! On t'adore notre Attiti :orange_heart:")
    return

@plugin.command
@lightbulb.command("azard", "Azard")
@lightbulb.implements(lightbulb.SlashCommand)
async def azard(ctx):
    await ctx.respond("Je vous présente Azard ! Malgré son pseudo, il n'est pas là par hasard ! Il a le swag voilà tout ! On t'aime nous! :heartpulse:")
    return

@plugin.command
@lightbulb.command("bebeswag", "BébéSwag")
@lightbulb.implements(lightbulb.SlashCommand)
async def bebeswag(ctx):
    await ctx.respond("Parce que je suis le centre du monde au sein de cette famille, je m'exprime !")
    return

@plugin.command
@lightbulb.command("bipbip", "BipBip")
@lightbulb.implements(lightbulb.SlashCommand)
async def bipbip(ctx):
    await ctx.respond("Mon premier coach officiel de RL ! C'est un membre essentiel et de bonne humeur dans cette famille ! On t'adore bip bip :white_heart: :purple_heart:")
    return

@plugin.command
@lightbulb.command("black", "BlackCandle")
@lightbulb.implements(lightbulb.SlashCommand)
async def black(ctx):
    await ctx.respond("Un voyage en mer et une bonne rigolade autour d'une bouteille ? Appelez capitaine BlackCandle elle hissera le pavillon pour vous ! :wink: :purple_heart:")
    return

@plugin.command
@lightbulb.command("carpediem", "Carpediem")
@lightbulb.implements(lightbulb.SlashCommand)
async def carpediem(ctx):
    await ctx.respond("Travailleur au grand coeur, il me soutient par sa présence et sa bonne humeur et à l'occase il se peut qu'on invoque Guney mais ça c'est pas gagné ! Quoiqu'il en soit merci a toi :sparkling_heart:\nCarpe fait partie de cette famille si tu veux en savoir plus sur lui c'est ici : <https://www.mamanswag.tv/membre-famille-swag_Carpediem090500>")
    return

@plugin.command
@lightbulb.command("comprimette", "Comprimette")
@lightbulb.implements(lightbulb.SlashCommand)
async def comprimette(ctx):
    await ctx.respond("Voici notre Lapin mais pas n'importe lequel, c'est notre Lapin au grand coeur de ouf ! Un amour de femme travailleuse et dévouée et d'une gentillesse extraordinaire ! On t'aime déjà Lapin :heartpulse:\nVoici son profil swag : <https://www.mamanswag.tv/membre-famille-swag_Comprimette>")
    return

@plugin.command
@lightbulb.command("corentin", "Corentin")
@lightbulb.implements(lightbulb.SlashCommand)
async def corentin(ctx):
    await ctx.respond("Voici notre nouveau membre adorable de la family swag, d'une âme charitable, il faut prendre soin de lui :heartpulse: :sparkling_heart:")
    return

@plugin.command
@lightbulb.command("cranberry", "Cranberry")
@lightbulb.implements(lightbulb.SlashCommand)
async def cranberry(ctx):
    await ctx.respond("Cranberry fait partie de la famille Swag !\nSi tu veux en savoir plus sur lui c'est ici : <https://www.mamanswag.tv/membre-famille-swag_Cranberry29Aquarius>\nVous savez ce qu'il vous reste à faire maintenant... Entrez dans la danse ! Merci à toi Cranberry :white_heart: :ribbon:")
    return

@plugin.command
@lightbulb.command("darkbloom", "DarkblooM")
@lightbulb.implements(lightbulb.SlashCommand)
async def darkbloom(ctx):
    await ctx.respond("La bourrinerie n'est jamais finie...\nVoici son profil swag : <https://www.mamanswag.tv/membre-famille-swag_DarkblooM>")
    return

@plugin.command
@lightbulb.command("dark", "Dark")
@lightbulb.implements(lightbulb.SlashCommand)
async def dark(ctx):
    await ctx.respond("Il est arrivé et il a tout cassé avec ses blagues et son délire, trolleur remasterisé adorable, il essaye d'invoquer KAARIS sur chaque live mais apparemment ça ne marche pas ! Pas grave on t'aime quand même ! :smiling_face_with_3_hearts:")
    return

@plugin.command
@lightbulb.command("darkwhite", "DarkWhite")
@lightbulb.implements(lightbulb.SlashCommand)
async def darkwhite(ctx):
    await ctx.respond("Voici the DarkWhite toujours présent et un amour !!! Ça fait déjà un moment que nous nous connaissons et c'est un membre au top de cette famille ! On t'aime DarkWhite :ribbon: :white_heart:")
    return

@plugin.command
@lightbulb.command("dealer", "Dealer")
@lightbulb.implements(lightbulb.SlashCommand)
async def dealer(ctx):
    await ctx.respond("Voici dealer au top de la sympathie ! Soit le bienvenu swaggeur :two_hearts: :hibiscus: :white_heart:")
    return

@plugin.command
@lightbulb.command("deltoura", "Deltoura")
@lightbulb.implements(lightbulb.SlashCommand)
async def deltoura(ctx):
    await ctx.respond("Voici notre super Deltoura notre nouveau swaggeur adorable et super sympas ! On t'adore déjà :heart_eyes:")
    return

@plugin.command
@lightbulb.command("dunmcleod", "DunMcLeod")
@lightbulb.implements(lightbulb.SlashCommand)
async def dunmcleod(ctx):
    await ctx.respond("Voici notre cher ami au top du top, discret mais d'une fiélité imparable, toujours sympathique et bienveillant on te kiff Dun :purple_heart: :two_hearts:")
    return

@plugin.command
@lightbulb.command("dydouks", "Dydouks")
@lightbulb.implements(lightbulb.SlashCommand)
async def dydouks(ctx):
    await ctx.respond("Une belle rencontre qu'est Dydouks, j'ai toujours un immense plaisir de lire ton \"ça va PIS toi ?\" ! Merci de m'aider comme tu le fais pour ouvrir les portes et tant d'autres choses :sparkling_heart: ! Merci pour ta fidélité depuis le début :ribbon:")
    return

@plugin.command
@lightbulb.command("effie", "Effie")
@lightbulb.implements(lightbulb.SlashCommand)
async def effie(ctx):
    await ctx.respond("Voilà l'arrivée de notre adorable elfe !! Je suis très très contente d'avoir fait ta connaissance ! Une nouvelle partenaire des escape games ! On t'adore déjà :hibiscus: :white_heart:")
    return

@plugin.command
@lightbulb.command("elidyr", "Elidyr")
@lightbulb.implements(lightbulb.SlashCommand)
async def elidyr(ctx):
    await ctx.respond("Voici Elidyr calme et posé, discret mais très bon joueur, on apprécie jouer avec toi copain ! On te kiff :purple_heart:")
    return

@plugin.command
@lightbulb.command("elyas", "Elyas")
@lightbulb.implements(lightbulb.SlashCommand)
async def elyas(ctx):
    await ctx.respond("Certaines personnes cherchent la gloire, la puissance et la fortune alors que le véritable trésor se trouve au côté de Maman, Papa Swag et leur communauté. :ribbon:")
    return

@plugin.command
@lightbulb.command("ezequiel", "Ezequiel")
@lightbulb.implements(lightbulb.SlashCommand)
async def ezequiel(ctx):
    await ctx.respond("Il est le calme incarné, il sait calmer le jeu quand Peter Pan tape sur Pocahontas ! Et oui c'est un héro d'une certaine façon ! MERCI de ta présence Ezequiel ! AU TOP :purple_heart:")
    return

@plugin.command
@lightbulb.command("fan2toi", "fan2toi")
@lightbulb.implements(lightbulb.SlashCommand)
async def fan2toi(ctx):
    await ctx.respond("Voici notre swaggeur de folie ! Un super fidèle parmi les fidèles ! Un énorme merci pour ton soutien tous les jours ! On veut te garder avec nous notre sasageyo swag ! :ribbon: :kiss:\nSi tu veux mieux le connaitre, c'est ici : <https://www.mamanswag.tv/membre-famille-swag_1fan2tol>")
    return

@plugin.command
@lightbulb.command("fatha", "Fathala")
@lightbulb.implements(lightbulb.SlashCommand)
async def fatha(ctx):
    await ctx.respond("Voici notre pote adorable et fidèle ! On se frappe toujours des délires avec toi ! Et il a le don de faire rire PapaSwag donc que demander de mieux ? On t'adore Fatha :purple_heart:")
    return

@plugin.command
@lightbulb.command("fauchaire", "Fauchaire")
@lightbulb.implements(lightbulb.SlashCommand)
async def fauchaire(ctx):
    await ctx.respond("Voici notre membre clippeur professionnel ! Oui monsieur avec Fauchaire tout est clair, même les clips ! :sunglasses:\nFauchaire fait parti de la famille Swag, si tu veux en savoir plus sur lui, c'est ici : <https://www.mamanswag.tv/membre-famille-swag_Fauchaire>")
    return

@plugin.command
@lightbulb.command("fl0rien", "Fl0rien")
@lightbulb.implements(lightbulb.SlashCommand)
async def fl0rien(ctx):
    await ctx.respond("Voici Flo ! adorabe et fidèle ! Un pote au top quoi !! Nous on t'adore Fl0rien :heartpulse:")
    return

@plugin.command
@lightbulb.command("flaykon", "Flaykon")
@lightbulb.implements(lightbulb.SlashCommand)
async def flaykon(ctx):
    await ctx.respond("Hey voici Flaykon ! Un joueur hors pair de Marbles :slight_smile: Il est au top alors prenez soin de lui les amis :hibiscus:")
    return

@plugin.command
@lightbulb.command("folded", "Folded")
@lightbulb.implements(lightbulb.SlashCommand)
async def folded(ctx):
    await ctx.respond("Nouvelle recrue hyper sympa ! Je suis contente d'avoir fait ta connaissance ! Trop cool ! On t'adore déjà :white_heart:")
    return

@plugin.command
@lightbulb.command("foxtrot", "FoxTroT")
@lightbulb.implements(lightbulb.SlashCommand)
async def foxtrot(ctx):
    await ctx.respond("Rusé comme un renard, il est adorable et généreux ! Toujours très pro, il maîtrise plein de choses ! Tu es notre modo discord préféré ! Merci de ta présence Fox :smiling_face_with_3_hearts: On t'aime :heartpulse:\nVoici son portrait swag si tu veux plus le connaitre c'est ici : <https://www.mamanswag.tv/membre-famille-swag_mFoxTrot>")
    return

@plugin.command
@lightbulb.command("gandalf", "Gandalf")
@lightbulb.implements(lightbulb.SlashCommand)
async def gandalf(ctx):
    await ctx.respond("Voici notre super Gandalf !!! Adorable et généreux d'amitié ! Un homme au top ! On t'adore notre gandalf :white_heart:")
    return

@plugin.command
@lightbulb.command("geekforever", "GeekForever")
@lightbulb.implements(lightbulb.SlashCommand)
async def geekforever(ctx):
    await ctx.respond("Partageons de l'amour et du soutien au copain :cherry_blossom:\n-> <https://www.twitch.tv/geekforever31>")
    return

@plugin.command
@lightbulb.command("geektor", "Geektor")
@lightbulb.implements(lightbulb.SlashCommand)
async def geektor(ctx):
    await ctx.respond("Je suis le premier follower de MamanSwag sauf qu'à force de me defollow/refollow je n'en ai plus la preuve ! :joy: MamanSwag te remercie de ton soutien depuis le début tu es au top !\nGeektor fait partie de la famille Swag, si tu veux en savoir plus sur lui c'est ici : <https://www.mamanswag.tv/membre-famille-swag_le_geektor>")
    return

@plugin.command
@lightbulb.command("gudiginga", "Gudiginga")
@lightbulb.implements(lightbulb.SlashCommand)
async def gudiginga(ctx):
    await ctx.respond("Voici notre Gudiginga ! Fidèle et adorable on s'y est attaché !! On t'adore Gudi !!!!! :hibiscus:")
    return

@plugin.command
@lightbulb.command("jody", "Jody")
@lightbulb.implements(lightbulb.SlashCommand)
async def jody(ctx):
    await ctx.respond("Voici TonDieuGrec allias Jody ! Adorable il veut donner une infinité d'amour et d'affection alors donnons lui en retour car il le mérite :heartpulse: On t'adore mon petit spartiate :hibiscus:")
    return

@plugin.command
@lightbulb.command("jojo", "Jojo")
@lightbulb.implements(lightbulb.SlashCommand)
async def jojo(ctx):
    await ctx.respond("Un joueur avec une persévérance extrême surtout sur Marbles ! :joy: Bienvenue a toi ! On te kiff déjà nous :hibiscus:")
    return

@plugin.command
@lightbulb.command("kevn", "Kevn")
@lightbulb.implements(lightbulb.SlashCommand)
async def kevn(ctx):
    await ctx.respond("Hey !! Allez voir la chaîne de <https://www.twitch.tv/kevnfrench> ! Notre star americaine à nous ! We love you Kevin :two_hearts:")
    return

@plugin.command
@lightbulb.command("kratoss", "Kratoss")
@lightbulb.implements(lightbulb.SlashCommand)
async def kratoss(ctx):
    await ctx.respond("Voici notre Kratoss en or toujours présent et de bonne humeur ! Gentil reporter swag, on le kiff déjà comme il se doit :purple_heart:")
    return

@plugin.command
@lightbulb.command("kuto", "Kuto")
@lightbulb.implements(lightbulb.SlashCommand)
async def kuto(ctx):
    await ctx.respond("Ce Kuto est un génie et d'un amour incommensurable ! Nous on t'aime Kuto !!! :hibiscus: :kiss:")
    return

@plugin.command
@lightbulb.command("lejp", "leJP")
@lightbulb.implements(lightbulb.SlashCommand)
async def lejp(ctx):
    await ctx.respond("Maître incontesté de Skribbl, challenger sur tous les jeux, joueur talentueux, respecté et respectable, il vous fait des bisous non covided.\nJP fait partie de la famille Swag si tu veux en savoir plus sur lui c'est ici : <https://www.mamanswag.tv/membre-famille-swag_LeJeanPascal>\nOn t'adore JP :two_hearts:")
    return

@plugin.command
@lightbulb.command("lico", "Lico")
@lightbulb.implements(lightbulb.SlashCommand)
async def lico(ctx):
    await ctx.respond("Un Potit Chat de l'ombre, du lurk pour une Maman merveilleuse !")
    return

@plugin.command
@lightbulb.command("lizea", "Lizea")
@lightbulb.implements(lightbulb.SlashCommand)
async def lizea(ctx):
    await ctx.respond("Voici Lizea notre Marry Poppins de la médecine ! Et la pro de Beyond: Two Souls ! Merci à toi Lizea :white_heart: :ribbon:")
    return

@plugin.command
@lightbulb.command("lunatik", "LuNatiK")
@lightbulb.implements(lightbulb.SlashCommand)
async def lunatik(ctx):
    await ctx.respond("Voici LuNatiK, une rencontre qui l'a fait devenir un membre et copain swag ! Il est au top et bon joueur ! On te kiff LuNatiK :heartpulse:\nVoici son portrait swag : <https://www.mamanswag.tv/membre-famille-swag_LuNatiK>")
    return

def load(bot):
    bot.add_plugin(plugin)