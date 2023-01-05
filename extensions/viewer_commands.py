import hikari, lightbulb

plugin = lightbulb.Plugin("viewer_commands")

# Viewer custom commands
@plugin.command
@lightbulb.command("ajaboy", "Ajaboy")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ajaboy(ctx) -> None:
    await ctx.respond("Voici notre nouveau copain, Ajaboy ! Toujours fidèle et adorablement gentil ! Il a le swag aussi :hibiscus: Bienvenue à toi :purple_heart:")
    return

@plugin.command
@lightbulb.command("amandine", "Amandine")
@lightbulb.implements(lightbulb.PrefixCommand)
async def amandine(ctx) -> None:
    await ctx.respond("Voici Amandine, toute gentille et toujours fidèle, elle vient toujours faire un coucou quand elle peut ! C'est un membre swag et oui elle a le SWAG :sunglasses: :white_heart:")
    return

@plugin.command
@lightbulb.command("anahera", "Anahera_Pokiha")
@lightbulb.implements(lightbulb.PrefixCommand)
async def anahera(ctx) -> None:
    await ctx.respond("Voici notre océan de bonheur ! Passioné de tout, il est toujours bienveillant et adorable ! Partout à la fois ! Nous on t'aime déjà Anahera :hibiscus: :heartpulse:\nVoici son profil swag : <https://www.mamanswag.tv/membre-famille-swag_Anahera_pokiha>")
    return

@plugin.command
@lightbulb.command("anymaa", "Anymaa")
@lightbulb.implements(lightbulb.PrefixCommand)
async def anymaa(ctx) -> None:
    await ctx.respond("Voici notre Anymaa toujours au top et sympathique ! Tu es plus que bienvenue ! :wink:")
    return

@plugin.command
@lightbulb.command("arthur", "Arthur")
@lightbulb.implements(lightbulb.PrefixCommand)
async def arthur(ctx) -> None:
    await ctx.respond("Toujours en train de délirer, il est la bonne humeur incarnée, qui pourrait se passer de lui sur ce chat ? Pas moi en tout cas ! Merci à toi pour ta présence :two_hearts:")
    return

@plugin.command
@lightbulb.command("attix", "Attix")
@lightbulb.implements(lightbulb.PrefixCommand)
async def attix(ctx) -> None:
    await ctx.respond("Il fait parti des premiers viewers réguliers et je l'en remercie beaucoup ! Si vous ne le voyez pas, c'est qu'il vient tard me faire des coucous ! On t'adore notre Attiti :orange_heart:")
    return

@plugin.command
@lightbulb.command("azard", "Azard")
@lightbulb.implements(lightbulb.PrefixCommand)
async def azard(ctx) -> None:
    await ctx.respond("Je vous présente Azard ! Malgré son pseudo, il n'est pas là par hasard ! Il a le swag voilà tout ! On t'aime nous! :heartpulse:")
    return

@plugin.command
@lightbulb.command("bebeswag", "BébéSwag")
@lightbulb.implements(lightbulb.PrefixCommand)
async def bebeswag(ctx) -> None:
    await ctx.respond("Parce que je suis le centre du monde au sein de cette famille, je m'exprime !")
    return

@plugin.command
@lightbulb.command("bipbip", "BipBip")
@lightbulb.implements(lightbulb.PrefixCommand)
async def bipbip(ctx) -> None:
    await ctx.respond("Mon premier coach officiel de RL ! C'est un membre essentiel et de bonne humeur dans cette famille ! On t'adore bip bip :white_heart: :purple_heart:")
    return

@plugin.command
@lightbulb.command("black", "BlackCandle")
@lightbulb.implements(lightbulb.PrefixCommand)
async def black(ctx) -> None:
    await ctx.respond("Un voyage en mer et une bonne rigolade autour d'une bouteille ? Appelez capitaine BlackCandle elle hissera le pavillon pour vous ! :wink: :purple_heart:")
    return

@plugin.command
@lightbulb.command("carpediem", "Carpediem")
@lightbulb.implements(lightbulb.PrefixCommand)
async def carpediem(ctx) -> None:
    await ctx.respond("Travailleur au grand coeur, il me soutient par sa présence et sa bonne humeur et à l'occase il se peut qu'on invoque Guney mais ça c'est pas gagné ! Quoiqu'il en soit merci a toi :sparkling_heart:\nCarpe fait partie de cette famille si tu veux en savoir plus sur lui c'est ici : <https://www.mamanswag.tv/membre-famille-swag_Carpediem090500>")
    return

@plugin.command
@lightbulb.command("comprimette", "Comprimette")
@lightbulb.implements(lightbulb.PrefixCommand)
async def comprimette(ctx) -> None:
    await ctx.respond("Voici notre Lapin mais pas n'importe lequel, c'est notre Lapin au grand coeur de ouf ! Un amour de femme travailleuse et dévouée et d'une gentillesse extraordinaire ! On t'aime déjà Lapin :heartpulse:\nVoici son profil swag : <https://www.mamanswag.tv/membre-famille-swag_Comprimette>")
    return

@plugin.command
@lightbulb.command("corentin", "Corentin")
@lightbulb.implements(lightbulb.PrefixCommand)
async def corentin(ctx) -> None:
    await ctx.respond("Voici notre nouveau membre adorable de la family swag, d'une âme charitable, il faut prendre soin de lui :heartpulse: :sparkling_heart:")
    return

@plugin.command
@lightbulb.command("cranberry", "Cranberry")
@lightbulb.implements(lightbulb.PrefixCommand)
async def cranberry(ctx) -> None:
    await ctx.respond("Cranberry fait partie de la famille Swag !\nSi tu veux en savoir plus sur lui c'est ici : <https://www.mamanswag.tv/membre-famille-swag_Cranberry29Aquarius>\nVous savez ce qu'il vous reste à faire maintenant... Entrez dans la danse ! Merci à toi Cranberry :white_heart: :ribbon:")
    return

@plugin.command
@lightbulb.command("darkbloom", "DarkblooM")
@lightbulb.implements(lightbulb.PrefixCommand)
async def darkbloom(ctx) -> None:
    await ctx.respond("La bourrinerie n'est jamais finie...\nVoici son profil swag : <https://www.mamanswag.tv/membre-famille-swag_DarkblooM>")
    return

@plugin.command
@lightbulb.command("dark", "Dark")
@lightbulb.implements(lightbulb.PrefixCommand)
async def dark(ctx) -> None:
    await ctx.respond("Il est arrivé et il a tout cassé avec ses blagues et son délire, trolleur remasterisé adorable, il essaye d'invoquer KAARIS sur chaque live mais apparemment ça ne marche pas ! Pas grave on t'aime quand même ! :smiling_face_with_3_hearts:")
    return

@plugin.command
@lightbulb.command("darkwhite", "DarkWhite")
@lightbulb.implements(lightbulb.PrefixCommand)
async def darkwhite(ctx) -> None:
    await ctx.respond("Voici the DarkWhite toujours présent et un amour !!! Ça fait déjà un moment que nous nous connaissons et c'est un membre au top de cette famille ! On t'aime DarkWhite :ribbon: :white_heart:")
    return

@plugin.command
@lightbulb.command("dealer", "Dealer")
@lightbulb.implements(lightbulb.PrefixCommand)
async def dealer(ctx) -> None:
    await ctx.respond("Voici dealer au top de la sympathie ! Soit le bienvenu swaggeur :two_hearts: :hibiscus: :white_heart:")
    return

@plugin.command
@lightbulb.command("deltoura", "Deltoura")
@lightbulb.implements(lightbulb.PrefixCommand)
async def deltoura(ctx) -> None:
    await ctx.respond("Voici notre super Deltoura notre nouveau swaggeur adorable et super sympas ! On t'adore déjà :heart_eyes:")
    return

@plugin.command
@lightbulb.command("dunmcleod", "DunMcLeod")
@lightbulb.implements(lightbulb.PrefixCommand)
async def dunmcleod(ctx) -> None:
    await ctx.respond("Voici notre cher ami au top du top, discret mais d'une fiélité imparable, toujours sympathique et bienveillant on te kiff Dun :purple_heart: :two_hearts:")
    return

@plugin.command
@lightbulb.command("dydouks", "Dydouks")
@lightbulb.implements(lightbulb.PrefixCommand)
async def dydouks(ctx) -> None:
    await ctx.respond("Une belle rencontre qu'est Dydouks, j'ai toujours un immense plaisir de lire ton \"ça va PIS toi ?\" ! Merci de m'aider comme tu le fais pour ouvrir les portes et tant d'autres choses :sparkling_heart: ! Merci pour ta fidélité depuis le début :ribbon:")
    return

@plugin.command
@lightbulb.command("effie", "Effie")
@lightbulb.implements(lightbulb.PrefixCommand)
async def effie(ctx) -> None:
    await ctx.respond("Voilà l'arrivée de notre adorable elfe !! Je suis très très contente d'avoir fait ta connaissance ! Une nouvelle partenaire des escape games ! On t'adore déjà :hibiscus: :white_heart:")
    return

@plugin.command
@lightbulb.command("elidyr", "Elidyr")
@lightbulb.implements(lightbulb.PrefixCommand)
async def elidyr(ctx) -> None:
    await ctx.respond("Voici Elidyr calme et posé, discret mais très bon joueur, on apprécie jouer avec toi copain ! On te kiff :purple_heart:")
    return

@plugin.command
@lightbulb.command("elyas", "Elyas")
@lightbulb.implements(lightbulb.PrefixCommand)
async def elyas(ctx) -> None:
    await ctx.respond("Certaines personnes cherchent la gloire, la puissance et la fortune alors que le véritable trésor se trouve au côté de Maman, Papa Swag et leur communauté. :ribbon:")
    return

@plugin.command
@lightbulb.command("ezequiel", "Ezequiel")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ezequiel(ctx) -> None:
    await ctx.respond("Il est le calme incarné, il sait calmer le jeu quand Peter Pan tape sur Pocahontas ! Et oui c'est un héro d'une certaine façon ! MERCI de ta présence Ezequiel ! AU TOP :purple_heart:")
    return

@plugin.command
@lightbulb.command("fan2toi", "fan2toi")
@lightbulb.implements(lightbulb.PrefixCommand)
async def fan2toi(ctx) -> None:
    await ctx.respond("Voici notre swaggeur de folie ! Un super fidèle parmi les fidèles ! Un énorme merci pour ton soutien tous les jours ! On veut te garder avec nous notre sasageyo swag ! :ribbon: :kiss:\nSi tu veux mieux le connaitre, c'est ici : <https://www.mamanswag.tv/membre-famille-swag_1fan2tol>")
    return

@plugin.command
@lightbulb.command("fatha", "Fathala")
@lightbulb.implements(lightbulb.PrefixCommand)
async def fatha(ctx) -> None:
    await ctx.respond("Voici notre pote adorable et fidèle ! On se frappe toujours des délires avec toi ! Et il a le don de faire rire PapaSwag donc que demander de mieux ? On t'adore Fatha :purple_heart:")
    return

@plugin.command
@lightbulb.command("fauchaire", "Fauchaire")
@lightbulb.implements(lightbulb.PrefixCommand)
async def fauchaire(ctx) -> None:
    await ctx.respond("Voici notre membre clippeur professionnel ! Oui monsieur avec Fauchaire tout est clair, même les clips ! :sunglasses:\nFauchaire fait parti de la famille Swag, si tu veux en savoir plus sur lui, c'est ici : <https://www.mamanswag.tv/membre-famille-swag_Fauchaire>")
    return

@plugin.command
@lightbulb.command("fl0rien", "Fl0rien")
@lightbulb.implements(lightbulb.PrefixCommand)
async def fl0rien(ctx) -> None:
    await ctx.respond("Voici Flo ! adorabe et fidèle ! Un pote au top quoi !! Nous on t'adore Fl0rien :heartpulse:")
    return

@plugin.command
@lightbulb.command("flaykon", "Flaykon")
@lightbulb.implements(lightbulb.PrefixCommand)
async def flaykon(ctx) -> None:
    await ctx.respond("Hey voici Flaykon ! Un joueur hors pair de Marbles :slight_smile: Il est au top alors prenez soin de lui les amis :hibiscus:")
    return

@plugin.command
@lightbulb.command("folded", "Folded")
@lightbulb.implements(lightbulb.PrefixCommand)
async def folded(ctx) -> None:
    await ctx.respond("Nouvelle recrue hyper sympa ! Je suis contente d'avoir fait ta connaissance ! Trop cool ! On t'adore déjà :white_heart:")
    return

@plugin.command
@lightbulb.command("foxtrot", "FoxTroT")
@lightbulb.implements(lightbulb.PrefixCommand)
async def foxtrot(ctx) -> None:
    await ctx.respond("Rusé comme un renard, il est adorable et généreux ! Toujours très pro, il maîtrise plein de choses ! Tu es notre modo discord préféré ! Merci de ta présence Fox :smiling_face_with_3_hearts: On t'aime :heartpulse:\nVoici son portrait swag si tu veux plus le connaitre c'est ici : <https://www.mamanswag.tv/membre-famille-swag_mFoxTrot>")
    return

@plugin.command
@lightbulb.command("gandalf", "Gandalf")
@lightbulb.implements(lightbulb.PrefixCommand)
async def gandalf(ctx) -> None:
    await ctx.respond("Voici notre super Gandalf !!! Adorable et généreux d'amitié ! Un homme au top ! On t'adore notre gandalf :white_heart:")
    return

@plugin.command
@lightbulb.command("geekforever", "GeekForever")
@lightbulb.implements(lightbulb.PrefixCommand)
async def geekforever(ctx) -> None:
    await ctx.respond("Partageons de l'amour et du soutien au copain :cherry_blossom:\n-> <https://www.twitch.tv/geekforever31>")
    return

@plugin.command
@lightbulb.command("geektor", "Geektor")
@lightbulb.implements(lightbulb.PrefixCommand)
async def geektor(ctx) -> None:
    await ctx.respond("Je suis le premier follower de MamanSwag sauf qu'à force de me defollow/refollow je n'en ai plus la preuve ! :joy: MamanSwag te remercie de ton soutien depuis le début tu es au top !\nGeektor fait partie de la famille Swag, si tu veux en savoir plus sur lui c'est ici : <https://www.mamanswag.tv/membre-famille-swag_le_geektor>")
    return

@plugin.command
@lightbulb.command("gudiginga", "Gudiginga")
@lightbulb.implements(lightbulb.PrefixCommand)
async def gudiginga(ctx) -> None:
    await ctx.respond("Voici notre Gudiginga ! Fidèle et adorable on s'y est attaché !! On t'adore Gudi !!!!! :hibiscus:")
    return

@plugin.command
@lightbulb.command("jody", "Jody")
@lightbulb.implements(lightbulb.PrefixCommand)
async def jody(ctx) -> None:
    await ctx.respond("Voici TonDieuGrec allias Jody ! Adorable il veut donner une infinité d'amour et d'affection alors donnons lui en retour car il le mérite :heartpulse: On t'adore mon petit spartiate :hibiscus:")
    return

@plugin.command
@lightbulb.command("jojo", "Jojo")
@lightbulb.implements(lightbulb.PrefixCommand)
async def jojo(ctx) -> None:
    await ctx.respond("Un joueur avec une persévérance extrême surtout sur Marbles ! :joy: Bienvenue a toi ! On te kiff déjà nous :hibiscus:")
    return

@plugin.command
@lightbulb.command("kevn", "Kevn")
@lightbulb.implements(lightbulb.PrefixCommand)
async def kevn(ctx) -> None:
    await ctx.respond("Hey !! Allez voir la chaîne de <https://www.twitch.tv/kevnfrench> ! Notre star americaine à nous ! We love you Kevin :two_hearts:")
    return

@plugin.command
@lightbulb.command("kratoss", "Kratoss")
@lightbulb.implements(lightbulb.PrefixCommand)
async def kratoss(ctx) -> None:
    await ctx.respond("Voici notre Kratoss en or toujours présent et de bonne humeur ! Gentil reporter swag, on le kiff déjà comme il se doit :purple_heart:")
    return

@plugin.command
@lightbulb.command("kuto", "Kuto")
@lightbulb.implements(lightbulb.PrefixCommand)
async def kuto(ctx) -> None:
    await ctx.respond("Ce Kuto est un génie et d'un amour incommensurable ! Nous on t'aime Kuto !!! :hibiscus: :kiss:")
    return

@plugin.command
@lightbulb.command("lejp", "leJP")
@lightbulb.implements(lightbulb.PrefixCommand)
async def lejp(ctx) -> None:
    await ctx.respond("Maître incontesté de Skribbl, challenger sur tous les jeux, joueur talentueux, respecté et respectable, il vous fait des bisous non covided.\nJP fait partie de la famille Swag si tu veux en savoir plus sur lui c'est ici : <https://www.mamanswag.tv/membre-famille-swag_LeJeanPascal>\nOn t'adore JP :two_hearts:")
    return

@plugin.command
@lightbulb.command("lico", "Lico")
@lightbulb.implements(lightbulb.PrefixCommand)
async def lico(ctx) -> None:
    await ctx.respond("Un Potit Chat de l'ombre, du lurk pour une Maman merveilleuse !")
    return

@plugin.command
@lightbulb.command("lizea", "Lizea")
@lightbulb.implements(lightbulb.PrefixCommand)
async def lizea(ctx) -> None:
    await ctx.respond("Voici Lizea notre Marry Poppins de la médecine ! Et la pro de Beyond: Two Souls ! Merci à toi Lizea :white_heart: :ribbon:")
    return

@plugin.command
@lightbulb.command("lunatik", "LuNatiK")
@lightbulb.implements(lightbulb.PrefixCommand)
async def lunatik(ctx) -> None:
    await ctx.respond("Voici LuNatiK, une rencontre qui l'a fait devenir un membre et copain swag ! Il est au top et bon joueur ! On te kiff LuNatiK :heartpulse:\nVoici son portrait swag : <https://www.mamanswag.tv/membre-famille-swag_LuNatiK>")
    return

@plugin.command
@lightbulb.command("major", "Major")
@lightbulb.implements(lightbulb.PrefixCommand)
async def major(ctx) -> None:
    await ctx.respond("Voici notre MajorTomsec discret mais adorable ! Un pro multigaming ! On te kiff Major de l'armée :wink:")
    return

@plugin.command
@lightbulb.command("mamanswag", "MamanSwag")
@lightbulb.implements(lightbulb.PrefixCommand)
async def mamanswag(ctx) -> None:
    await ctx.respond("Tu n'as pas le SWAG ? Moi non plus :joy: !!! Mais faisons comme si... On finira par l'avoir ensemble :heartpulse:")
    return

@plugin.command
@lightbulb.command("max", "Max")
@lightbulb.implements(lightbulb.PrefixCommand)
async def max(ctx) -> None:
    await ctx.respond("Rencontré grâce à notre fils spirituel, il est plein de vannes et de délires ! On t'apprécie déjà beaucoup, sauf Yta, mais ça c'est entre vous ! :wink:")
    return

@plugin.command
@lightbulb.command("mayeu", "Mayeu")
@lightbulb.implements(lightbulb.PrefixCommand)
async def mayeu(ctx) -> None:
    await ctx.respond("Merci à la formidable équipe de modérateurs Twitch et Discord :heart: Voici notre mayeu qui fait partie des plus belles rencontres que j'ai pu faire sur Twitch ! :white_heart:\nN'hésitez pas à en savoir un peu plus sur cette superbe personne -> <https://www.mamanswag.tv/membre-famille-swag_Mayeu>")
    return

@plugin.command
@lightbulb.command("melcki", "Melcki")
@lightbulb.implements(lightbulb.PrefixCommand)
async def melcki(ctx) -> None:
    await ctx.respond("Voici notre Melcki de folie ! Toujours là pour la culture G, les énigmes et tout le reste ! Merci de ta présence ! :cherry_blossom: :two_hearts:")
    return

@plugin.command
@lightbulb.command("melicendre", "Melicendre")
@lightbulb.implements(lightbulb.PrefixCommand)
async def melicendre(ctx) -> None:
    await ctx.respond("Voici Melicendre ! Une superbe rencontre IRL elle est pro gameuse et hyper drôle ! Tu peux pas t'ennuyer avec elle ! Crois-moi ! Bienvenue à toi, on t'adore déjà :two_hearts:")
    return

@plugin.command
@lightbulb.command("niddo", "Niddo")
@lightbulb.implements(lightbulb.PrefixCommand)
async def niddo(ctx) -> None:
    await ctx.respond("Voici notre Niddo ! Plus qu'un viewer depuis le temps !! Hyper sympathique et très gentil, on aime t'avoir à nos côtés dans la famille Swag :two_hearts:")
    return

@plugin.command
@lightbulb.command("nounours", "Nounours")
@lightbulb.implements(lightbulb.PrefixCommand)
async def nounours(ctx) -> None:
    await ctx.respond("Voilà notre Nounours au top du top depuis un long moment maintenant ! Que veux tu qu'on te dise à part qu'on t'adore depuis le début :cherry_blossom:")
    return

@plugin.command
@lightbulb.command("nukinaos", "Nukinaos")
@lightbulb.implements(lightbulb.PrefixCommand)
async def nukinaos(ctx) -> None:
    await ctx.respond("Bienvenue à toi jeune pingouin ! Ici il fait chaud tu risques de fondre :joy: Bienvenue swaggeuse :ribbon:")
    return

@plugin.command
@lightbulb.command("nymphaquali", "Nymphaquali")
@lightbulb.implements(lightbulb.PrefixCommand)
async def nymphaquali(ctx) -> None:
    await ctx.respond("Voici Nymphaquali, il est très drôle et il donne beaucoup d'amour :purple_heart:\nSi tu veux faire plus sa connaissance, c'est ici : <https://www.mamanswag.tv/membre-famille-swag_Nymphaquali>")
    return

@plugin.command
@lightbulb.command("panda", "Panda")
@lightbulb.implements(lightbulb.PrefixCommand)
async def panda(ctx) -> None:
    await ctx.respond("Voici notre Panda ! Un amour insomniaque, mais d'une gentillesse incroyable ! Je crois qu'il est attiré par la SNCF mais chuuuut :rofl: On t'adore déjà Pandalol :white_heart:")
    return

@plugin.command
@lightbulb.command("papaswag", "PapaSwag")
@lightbulb.implements(lightbulb.PrefixCommand)
async def papaswag(ctx) -> None:
    await ctx.respond("Comme vous le savez, sans lui je ne vous aurais jamais rencontré ! Alors pour cette raison et pour infiniment d'autres... PAPASWAG JE T'AIME :heartpulse:\nEt si tu veux en savoir plus sur lui rdv ici : <https://www.mamanswag.tv/membre-famille-swag_LePapaSwag>")
    return

@plugin.command
@lightbulb.command("pirataflama", "Pirataflama")
@lightbulb.implements(lightbulb.PrefixCommand)
async def pirataflama(ctx) -> None:
    await ctx.respond("Voici notre Pirata au top du top ! Cela fait un moment qu'on s'est rencontré et on te kiff copain ! Changes pas :two_hearts:")
    return

@plugin.command
@lightbulb.command("poke", "Poke")
@lightbulb.implements(lightbulb.PrefixCommand)
async def poke(ctx) -> None:
    await ctx.respond("Il n'est plus le même homme depuis qu'il joue à Phasmo, en tout cas tout ce que je peux dire c'est que c'est un DJINN !! Poki Poka on t'aime :kissing_smiling_eyes:\nPoke fait partie de cette famille, tu peux en savoir plus sur lui ici : <https://www.mamanswag.tv/membre-famille-swag_PokefluteBleuCanard>")
    return

@plugin.command
@lightbulb.command("poussin", "Poussin")
@lightbulb.implements(lightbulb.PrefixCommand)
async def poussin(ctx) -> None:
    await ctx.respond("Voici notre Poussin de competition ! Adorable, bienveillant et ultra sympas, des poussins comme lui on adore ! On te kiff poussin :purple_heart: :two_hearts: :cherry_blossom:\nVoici son profil swag : <https://www.mamanswag.tv/membre-famille-swag_Poussinenslip2bain>")
    return

@plugin.command
@lightbulb.command("quentin", "Quentin")
@lightbulb.implements(lightbulb.PrefixCommand)
async def quentin(ctx) -> None:
    await ctx.respond("Voilà mon coéquipier enquêteur hors-pair sur les jeux d'énigmes et casse tête, tu me suis de A à Z sur les jeux ! Un grand merci pour ton aide !\nQuentin fait parti de la fmaille swag, si tu veux en savoir plus sur lui, c'ets ici : <https://www.mamanswag.tv/membre-famille-swag_QuentinM91_35>")
    return

@plugin.command
@lightbulb.command("ratonio", "Ratonio")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ratonio(ctx) -> None:
    await ctx.respond("Je vous présente Ratonio ! Un pote super sympa qui passe toujours nous faire des coucous dès qu'il peut ! Si besoin il peut vous faire votre piscine =) ! On te kiffe Ratonio :white_heart:")
    return

@plugin.command
@lightbulb.command("rubn", "Rubn")
@lightbulb.implements(lightbulb.PrefixCommand)
async def rubn(ctx) -> None:
    await ctx.respond("J'aide MamanSwag sur ses lives, même si j'aime pas les jeux auxquels elle joue !\nUn grand merci pour ta fidèle présence et merci de m'accompagner comme tu le fais :pray:")
    return

@plugin.command
@lightbulb.command("sam", "Sam")
@lightbulb.implements(lightbulb.PrefixCommand)
async def sam(ctx) -> None:
    await ctx.respond("Bienvenue à toi swaggeur ! Nous sommes ravis de t'avoir parmi nous dans notre Family Swag ! Prends place et éclates-toi, on t'adore déjà :wink: :heartpulse:")
    return

@plugin.command
@lightbulb.command("serendipidy", "Serendipidy")
@lightbulb.implements(lightbulb.PrefixCommand)
async def serendipidy(ctx) -> None:
    await ctx.respond("Avec sa gentillesse et sa sympathie il a su se démarquer ! Je te remercie de ta présence et d'être revenu me voir après un certains moment, ça me fait super plaisir de t'avoir retrouvé :pray: :kissing_closed_eyes:")
    return

@plugin.command
@lightbulb.command("snooky", "Snooky")
@lightbulb.implements(lightbulb.PrefixCommand)
async def snooky(ctx) -> None:
    await ctx.respond("Un des meilleurs partenaires que j'ai pu rencontrer pous les casse-têtes et énigmes il est présent et je peux compter sur lui ! Un grand merci pour ton soutien et ta présence :purple_heart: :ribbon:")
    return

@plugin.command
@lightbulb.command("sophie", "Sophie")
@lightbulb.implements(lightbulb.PrefixCommand)
async def sophie(ctx) -> None:
    await ctx.respond("Je suis la NounouSwag de cette communauté et même si je suis loin, j'apporte beaucoup d'amour et d'affection à BébéSwag :sparkling_heart:")
    return

@plugin.command
@lightbulb.command("soulzeph", "Soulzeph")
@lightbulb.implements(lightbulb.PrefixCommand)
async def soulzeph(ctx) -> None:
    await ctx.respond("Soulzeph, il arrive avec toute sa sympathie et son empathie, des amis comme ça, on en voudrait à nos côtés tous les jours ! Merci d'être à mes cotés :two_hearts: :ribbon:")
    return

@plugin.command
@lightbulb.command("squally", "Squally")
@lightbulb.implements(lightbulb.PrefixCommand)
async def squally(ctx) -> None:
    await ctx.respond("Squally est un membre unique de la famille Swag. Si tu veux en savoir plus sur lui rdv ici : <https://www.mamanswag.tv/membre-famille-swag_Squally146>\n:heartpulse: On t'aime Squally :heartpulse:")
    return

@plugin.command
@lightbulb.command("stps", "Stps")
@lightbulb.implements(lightbulb.PrefixCommand)
async def stps(ctx) -> None:
    await ctx.respond("Voilà l'incontestable SSAMPION DES ZISTOUARES de tous les temps dans ce monde ! Son imagination est sans limite et nous (les swaggeurs) on adore trop lire les zistouares de Stp ! Alors un énorme merci pour ta présence et ta bonne humeur et pour la personne que tu es ! On t'adore trop copain de le tsat :kiss: :two_hearts:")
    return

@plugin.command
@lightbulb.command("treaker", "Treaker")
@lightbulb.implements(lightbulb.PrefixCommand)
async def treaker(ctx) -> None:
    await ctx.respond("Treaker est un homme généreux, adorable et passionné, le calme incarné, avec une voix digne des plus grands acteurs d'Hollywood ! On t'adore Treaker ! :heartpulse:\nTreaker fait partie de la famille Swag tu peux en savoir plus sur lui ici : <https://www.mamanswag.tv/membre-famille-swag_Treaker59>")
    return

@plugin.command
@lightbulb.command("vanetro", "Vanetro")
@lightbulb.implements(lightbulb.PrefixCommand)
async def vanetro(ctx) -> None:
    await ctx.respond("Il aime aider MamanSwag sur ses lives surtout pour les jeux d'armes et de puzzles ! Même si ses jeux sont embêtants parfois c'est quand même agréable de l'aider ! Merci à toi pour ces heures de live partagées et ça n'est pas fini !! :wink: :two_hearts:")
    return

@plugin.command
@lightbulb.command("wolf", "Wolf")
@lightbulb.implements(lightbulb.PrefixCommand)
async def wolf(ctx) -> None:
    await ctx.respond("Dans la lignée des superbes rencontres, je vous présente Wolf ! :two_hearts: Pour ceux qui ont de la chance vous l'aurez peut être à vos côtés sur Phasmo ! Et oui il gère grave !! En attendant bienvenue dans la familly Swag avec grand plaisir :smiling_face_with_3_hearts:")
    return

@plugin.command
@lightbulb.command("yta", "Yta")
@lightbulb.implements(lightbulb.PrefixCommand)
async def yta(ctx) -> None:
    await ctx.respond("Il est le fils spirituel de cette famille, Ytatoutmis on sait pas ce qu'il met, mais une chose est sûre il y met toujours tout son coeur :heartpulse:")
    return

@plugin.command
@lightbulb.command("zatome", "Zatome")
@lightbulb.implements(lightbulb.PrefixCommand)
async def zatome(ctx) -> None:
    await ctx.respond("Et voici notre Zatome ! Faites attention il risque de tous vous zatomiser !! :joy: Bienvenue ami swaggeur :cherry_blossom:")
    return

@plugin.command
@lightbulb.command("zoscran", "Zoscran")
@lightbulb.implements(lightbulb.PrefixCommand)
async def zoscran(ctx) -> None:
    await ctx.respond("Il débarque quand on l'appel a la rescousse (du moins quand il entend l'appel) ou juste pour sortir des jeux de mots pas si drôles ! Mais nous on t'adore :white_heart:")
    return

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)
