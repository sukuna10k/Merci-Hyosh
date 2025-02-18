class script(object):
    
    START_TXT = """<b>Salut {},

Je suis Marsh ƈɾσɯ je suis un puissant bot qui peut te fournir des Films, Séries, Animes, cartoon et plein d'autres encore. Il suffit de rejoindre mon canal et de profitez !

<blockquote> ‣ Maintenu par : [BotZFlix](https://t.me/BotZFlix)</blockquote></b>
"""
    GSTART_TXT = """<b>Salut {},\n\nJe suis le bot de filtrage automatique le plus puissant avec des fonctionnalités premium.\n\nMaintenu par : <a href="https://t.me/BotZFlix">BotZFlix</a></b>"""

    HELP_TXT = """<b>Cliquez sur le bouton ci-dessous pour obtenir une description des commandes spécifiques !</b>"""

    ABOUT_TXT = """
<b>❍ Nom : {}</b>
<b>❍ Créateur : [Hyosh](https://t.me/hyoshassistantbot) et [🇰ιηg¢єу](https://t.me/kingcey)</b>
<b>❍ Bibliothèque : <a href="https://pyrogram.org/">Pyrogram</a></b>
<b>❍ Langage : <a href="https://www.python.org/">Python</a></b>
<b>❍ Base de données : <a href="https://www.mongodb.com/">MongoDB</a></b>
<b>❍ Hébergé sur : <a href="https://t.me/botZFlix">VPS</a></b>
<b>❍ Version : v4.4.1</b>

➲ Je restreins les utilisateurs, filtre automatiquement, et offre une gestion complète des utilisateurs.<br>
➲ Modules : stockage de fichiers, polices, kanging, IA, etc.<br><br>

➻ Cliquez ci-dessous pour plus d'infos.
"""

    SUBSCRIPTION_TXT = """
<b>Partagez votre lien avec vos amis, votre famille, vos chaînes et vos groupes pour obtenir gratuitement un abonnement premium pour {}

Lien de parrainage - https://telegram.me/{}?start=AntiFlix-{}

Si {} utilisateur unique démarre le bot avec votre lien de parrainage, vous serez automatiquement ajouté à la liste premium.

Achetez un plan payant avec - /plan</b>"""

    SOURCE_TXT = """
Hey,  
C'est BotZFlix,  
un bot Telegram open source d'auto-filtrage avec des modules d'intelligence artificielle et de gestion de groupes.  

Écrit en Python avec l'aide de <a href='https://github.com/pyrogram/pyrogram'>Pyrogram</a> et <a href='https://github.com/python-telegram-bot/python-telegram-bot'>Python-Telegram-Bot</a>,  
et utilisant <a href='https://cloud.mongodb.com'>Mongo</a> comme base de données.  

» Voici mon code source : <a href='https://botZFlix'>Click ici</a>  

Hokage est sous licence <a href='https://LICENSE'>MIT</a>.  
© 2023 - 2024 | <a href='https://t.me/Kingcey1'>Support Chat</a>, tous droits réservés.
"""

    MAIN_TXT = """
Voici le menu d'aide
"""

    SPECIAL_TXT = """
Consultez votre module favori
"""

    CHANNELS = """
<b>Cliquez sur les boutons ci-dessous pour rejoindre les chaînes et obtenir plus d'informations sur nous.</b>  

Si vous trouvez un bug dans « Hokage » ou si vous souhaitez donner un retour sur le bot,  
veuillez le signaler ici : <a href='https://t.me/kingcey1'>Support Chat</a>.
"""

    DONATE = """
<b>Souhaitez-vous aider mon créateur dans ses efforts pour maintenir mon développement actif ?  
Si oui, vous êtes au bon endroit.  

Nous soulignons l'importance des fonds nécessaires pour garder Hokage en développement actif.  
Vos dons, quel qu'en soit le montant, permettront de soutenir les serveurs de Hokage et d'autres utilités,  
et d'assurer une longue durée de vie au projet.  

Tous les dons couvriront les futures dépenses et les mises à niveau des serveurs.  
Si vous avez des moyens de nous aider, faites-le généreusement. Vos contributions motivent également l'ajout de nouvelles fonctionnalités.  

Vous pouvez soutenir le développement en faisant un don :  
UPI : Gautam8292@fam  

Envoyez une capture d'écran ici : @Kingcey</b>
"""

    SETTINGS_TXT = """
Aide : <b>Paramètres</b>

◈ Les paramètres sont une fonctionnalité très importante de ce bot.  
◈ Vous pouvez facilement personnaliser ce bot pour votre groupe.

<b>Note :</b>  
1. Seuls les administrateurs du groupe peuvent utiliser cette commande et modifier les paramètres.  
2. Cela fonctionne uniquement si le bot est déjà connecté à votre groupe.

<b>Commandes et Utilisation :</b>  
• /connect - Connecter votre groupe au bot  
• /settings - Modifier les paramètres selon vos besoins  
"""

    TELEGRAPH_TXT = """
Aide : <b>Telegraph</b>

<b>Note :</b> Cette commande est disponible dans les groupes et en messages privés. Elle peut être utilisée par tout le monde.

<b>Commandes et Utilisation :</b>  
• /telegraph - Envoyez-moi une image ou une vidéo de moins de 5 Mo  
"""

    FONT_TXT = """
Aide : <b>Police</b>

<b>Note :</b> Vous pouvez utiliser ce mode pour changer le style de vos polices.  
Envoyez-moi simplement un message au format suivant :  

<code>/font Team Netflix</code>  
"""

    MANUELFILTER_TXT = """
Aide : <b>Filtres</b>

◈ Le filtre est une fonctionnalité où les utilisateurs peuvent configurer des réponses automatiques pour un mot-clé spécifique, et je répondrai à chaque fois qu’un mot-clé sera trouvé dans un message.

<b>Note :</b>  
1. Ce bot doit avoir des privilèges d'administrateur.  
2. Seuls les administrateurs peuvent ajouter des filtres dans un chat.  
3. Les boutons d'alerte ont une limite de 64 caractères.

<b>Commandes et Utilisation :</b>  
• /filter - Ajouter un filtre dans un chat  
• /filters - Lister tous les filtres d’un chat  
• /del - Supprimer un filtre spécifique dans un chat  
• /delall - Supprimer tous les filtres dans un chat (propriétaire uniquement)  
"""

    BUTTON_TXT = """Aide : <b>Boutons</b>
    
◈ Ce bot prend en charge les boutons URL et les boutons d'alerte inline.

<b>Note :</b>
1. Telegram n'autorise pas l'envoi de boutons sans contenu, donc un contenu est obligatoire.
2. Ce bot prend en charge les boutons avec tout type de média Telegram.
3. Les boutons doivent être correctement formatés en markdown.

Boutons URL :
<code>[Texte du bouton](buttonurl:https://t.me/hyoshassistantbot)</code>

Boutons d'alerte :
<code>[Texte du bouton](buttonalert:Ceci est un message d'alerte)</code>"""

    AUTOFILTER_TXT = """Aide : <b>Auto Filtre</b>
    
<b>Note :</b> Indexation des fichiers
1. Faites de moi un administrateur de votre chaîne si elle est privée.
2. Assurez-vous que votre chaîne ne contient ni camrips, ni contenus pour adultes, ni fichiers falsifiés.
3. Transférez le dernier message de votre chaîne avec des citations. Je vais ajouter tous les fichiers de cette chaîne à ma base de données.

<b>Note :</b> Auto Filtre
1. Ajoutez le bot comme administrateur de votre groupe.
2. Utilisez /connect pour connecter votre groupe au bot.
3. Utilisez /settings dans le message privé du bot pour activer l'Auto Filtre dans le menu des paramètres."""

    RULE_TXT = """♦ Règles du Groupe ♦

◈ <b>Recherchez un film avec une orthographe correcte :</b>
• avatar 2009 ✅
• avatar VF ✅
• avatar series ❌
• avatar Film en français..❌

◈ <b>Recherchez une série Web, Animé, cartoon dans ce format :</b>
• vikings S01 ✅
• vikings S01E01 ✅
• vikings ✅
• vikings S01 hindi dubbed... ❌
• vikings saison 1 ❌
• vikings série web ❌

<b>➙ Ne faites pas d'auto-promotion. 
➙ N'envoyez aucun type de photo, vidéo, document, URL, etc...
➙ Ne demandez rien d'autre que des films, séries, animations, dessins animés, anime, k-dramas, et plus encore.</b>

🔰 <b>Note :</b> Tous les messages seront automatiquement supprimés après 10 minutes pour éviter les problèmes de droits d'auteur."""

    CONNECTION_TXT = """Aide : <b>Connexions</b>

◈ Utilisé pour connecter le bot à la messagerie privée (PM) pour gérer les filtres.
◈ Cela permet d'éviter le spam dans les groupes.

<b>Note :</b>
1. Seuls les administrateurs peuvent ajouter une connexion.
2. Envoyez /connect pour me connecter à votre messagerie privée.

<b>Commandes et Utilisation :</b>
• /connect - Connecte un chat particulier à votre messagerie privée.
• /disconnect - Déconnecte un chat.
• /connections - Liste toutes vos connexions.
"""

    EXTRAMOD_TXT = """Aide : <b>Modules Supplémentaires</b>\n<b>Note :</b>
Ces fonctionnalités sont des options supplémentaires offertes par ce bot.

<b>Commandes et Utilisation :</b>
• /id - Obtenez l'ID d'un utilisateur spécifié.
• /info - Obtenez des informations sur un utilisateur.
• /imdb - Obtenez les informations d'un film depuis la source IMDb.
• /search - Recherchez des informations sur un film depuis diverses sources.
"""

    STICKER_TXT = """<b>Vous pouvez utiliser ce module pour trouver l'ID de n'importe quel sticker.

• Utilisation : Obtenez l'ID d'un sticker.

<b>Comment l'utiliser :</b>
◉ Répondez à n'importe quel sticker avec la commande [`/stickerid`].

/stickerid - Obtenez l'ID d'un sticker.
</b>
"""

    ALL_FILTERS = """
<b>Salut {}, voici les trois types de filtres disponibles.</b>"""

    GFILTER_TXT = """Aide : <b>Filtres globaux</b>

◈ Les filtres globaux sont définis par les administrateurs du bot et fonctionnent dans tous les groupes.

<b>Commandes et utilisations :</b>
• /gfilter - Pour créer un filtre global.
• /gfilters - Pour afficher tous les filtres globaux.
• /delg - Pour supprimer un filtre global spécifique.
• /delallg - Pour supprimer tous les filtres globaux."""

    FILE_STORE_TXT = """Aide : <b>Stockage de fichiers</b>

◈ Le stockage de fichiers permet de créer un lien partageable pour un ou plusieurs fichiers.

<b>Commandes et utilisations :</b>
• /batch - Pour créer un lien regroupant plusieurs fichiers.
• /link - Pour créer un lien pour un seul fichier.
• /pbatch - Comme <code>/batch</code>, mais les fichiers sont envoyés avec des restrictions de transfert.
• /plink - Comme <code>/link</code>, mais le fichier est envoyé avec des restrictions de transfert."""

    YTTHUMB = """<b>YT-Thumbnail

Permet de télécharger la miniature d'une vidéo YouTube.

Utilisez ce format 👇</b>

<code>/ytthumb https://youtu.be/BqlMwyABHOE</code>"""

    GITHUB = """<b>Détails GitHub :</b>

Avec cette commande, vous pouvez obtenir les informations complètes du compte GitHub d'un développeur ou utilisateur.

Utilisez ce format 👇

❍ /github phoenix-erotixe
❍ /git : Pour obtenir des informations sur un identifiant GitHub.
"""

    YTTAGS = """<b>Pour les tags des vidéos YouTube -

Vous pouvez découvrir les tags de n'importe quelle vidéo YouTube avec cette commande

➤ Commande :

/yttags - Répondez à une vidéo YouTube</b>"""

    VIDEO_TXT = """<b>Module de téléchargement de vidéos

Vous pouvez télécharger n'importe quelle vidéo depuis YouTube

➤ Commandes

Tapez /video ou /mp4

Exemples :</b>

<code>/mp4 https://youtu.be/BqlMwyABHOE</code>

<code>/video https://youtu.be/BqlMwyABHOE</code>"""

    REPORT = """<b>Rapport 🧑🏻‍✈️  

Cette commande vous aide à signaler un message ou un utilisateur aux admins du groupe respectif

➤ Commande :

/report @admin - Pour signaler un utilisateur aux admins (répondre à un message).</b>"""

    HYOSHCODER = """
<b>C'est le bot Marsh ƈɾσɯ 🦚,
Un puissant bot stable et mignon pour filtrer et gérer Telegram.</b>"""

    GEN_PASS = """<b>Générateur de mot de passe</b>

Il n'y a rien d'autre à savoir. Envoyez-moi la limite de votre mot de passe.

- Je vous fournirai le mot de passe de cette limite.

➤ Commande :

• /genpassword ou /genpw 20

NOTE :
• Seuls les chiffres sont autorisés
• Longueur maximale autorisée jusqu'à 84
  (Je ne peux pas générer de mots de passe au-delà de 84 caractères)
• IMDb doit avoir des privilèges d'administrateur.
• Ces commandes fonctionnent à la fois en privé et en groupe.
• Ces commandes peuvent être utilisées par n'importe quel membre du groupe."""

    OPNAI_TXT = """OpenAI est un système d'IA qui vous aidera à trouver la réponse à votre question et il fonctionnera uniquement en message privé avec le bot.

Comment l'utiliser

/openai qu'est-ce que append method en python
"""

    KANG = """
Créez votre propre sticker et pack de stickers
Envoyez à l'image
Répondez à l'image et envoyez la commande /kang
"""

    GROUP_TXT = """
<b>๏ Cliquez sur les boutons ci-dessous pour rejoindre les canaux et obtenir plus d'informations sur nous.

Si vous trouvez un bug dans ˹𝐋ᴜᴄʏ˼ ou si vous souhaitez donner votre avis sur le bot, veuillez le signaler dans <a href='https://t.me/promo_prenium_groupe'>le chat de support</a>.</b>
"""

    PURGE_TXT = """<b>Purging

Supprimez un grand nombre de messages dans les groupes ! 

Admin

◉ /purge :- Supprimer tous les messages à partir du message auquel on a répondu, jusqu'au message actuel​</b>"""

    JSON_TXT = """<b>
JSON :

Le bot renvoie un JSON pour tous les messages répondus avec /json

Fonctionnalités :

Édition de message en JSON
Support PM
Support de groupe

Note :

Tout le monde peut utiliser cette commande, mais si du spam est détecté, le bot vous bannira automatiquement du groupe.</b>"""

    CARB_TXT = """<b>Aide pour Carbon

Carbon est une fonctionnalité qui vous permet de personnaliser l'image avec votre texte, comme montré en haut.
Pour utiliser le module, envoyez simplement le texte et utilisez la commande /carbon. Le bot prévisualisera l'image avec votre texte.

</b>"""

    SONG_TXT = """<b>Détails du chanson
Recherche de chansons en vidéo et audio

Exemple -
Commandes de chansons sauvegardées
/ssong seul 
/svideo seul

Commande vidéo YouTube
/ysong seul ou lien YouTube
/yvideo seul ou lien YouTube
</b>"""

    ALIVE = """<b>Détails du PING -</b>
/alive du Bot Alive Test Commande

/Test de vitesse du Bot Ping
"""

    REPO = """<b>Détails du REPO -</b>

Vous pouvez trouver le repo GitHub avec l'aide de cette commande.

❍ /repo : rechercher n'importe quel repo
❍ /allrepo : obtenir tous les repos
❍ /downloadrepo : télécharger le repo

Plus de fonctionnalités à venir bientôt."""

    SHORTNER = """<b>Raccourcisseur d'URL</b>

Ce module vous aide à raccourcir une URL et vous pouvez gagner de l'argent avec ce bot tant qu'il est actif.

➤ Commandes :

➪ /short - Utilisez cette commande avec votre lien pour obtenir des liens raccourcis
➪ /shortlinkon - Activez le raccourcisseur de lien pour votre groupe
➪ /shortlinkoff - Désactivez le raccourcisseur de lien pour votre groupe
➪ /shortlink_info - Vérifiez les informations de votre groupe
➪ /set_shortlink - Pour définir un lien raccourci dans votre groupe, utilisez cette commande
➪ /set_tutorial - Pour définir votre propre tutoriel de raccourcisseur, utilisez cette commande"""

    LYRICS = """<b>Paroles</b>

Avec l'aide de cette commande, vous pouvez obtenir les paroles des chansons.

➤ Commande :

➪ /lyrics - Utilisez cette commande pour obtenir les paroles."""

    RESTRIC_TXT = """➤ Aide : Mute 🚫

Voici les commandes qu'un administrateur de groupe peut utiliser pour gérer son groupe plus efficacement.

➪ /ban : Bannir un utilisateur du groupe.
➪ /unban : Débannir un utilisateur du groupe.
➪ /tban : Bannir temporairement un utilisateur.
➪ /mute : Muter un utilisateur dans le groupe.
➪ /unmute : Démuter un utilisateur dans le groupe.
➪ /tmute : Mute temporairement un utilisateur.

Alimenté par les bots Codeflix

➤ Note :
Lorsque vous utilisez /tmute ou /tban, vous devez spécifier la durée du blocage.

Exemple : /tban 2d ou /tmute 2d.
Vous pouvez utiliser les valeurs : m/h/d.
 • m = minutes
 • h = heures
 • d = jours"""

    GAME_TXT = """Jeux

Module Jeux

🏸 Juste quelques jeux amusants

1. /dice - Lance le dé
2. /Throw ou /Dart - Lance un dart
3. /Runs - Quelques dialogues aléatoires
4. /Goal ou /Shoot - Marque un but ou tire
5. /luck ou /cownd - Lance et tente ta chance"""

    CC_TXT = """
AIDE : Outils CC

Tout sur les cartes de crédit avec le module CC !

UTILISATION :
➢ /sk - Vérifie si la clé Stripe est active ou non.
➢ /bin - Vérifie si le BIN donné est valide ou non.
➢ /fake - Génère des informations utilisateur aléatoires.
➢ /gen - Génère des informations de cartes de crédit aléatoires.
➢ /cc - Génère des cartes de crédit aléatoires.

REMARQUE :
• Hokage doit avoir des privilèges d'administrateur.
• Ces commandes fonctionnent à la fois en message privé et en groupe.
• Ces commandes peuvent être utilisées par n'importe quel membre du groupe."""

    ANIME_TXT = """
Obtenez des informations sur les animés, les mangas et les personnages !

UTILISATION :
➢ /neko [-n] - Obtenez une image aléatoire de neko (-n pour nsfw).
➢ /waifu [-n] - Obtenez une image aléatoire de waifu (-n pour nsfw).
➢ /anime [nom] - Obtenez des informations sur l'anime.
➢ /manga [nom] - Obtenez des informations sur le manga.
➢ /hentai [nom] - Obtenez et lisez le manga hentai (nsfw).
➢ /hentai [-r] - Obtenez un manga hentai aléatoire à lire (nsfw).
➢ /aninews - Obtenez les dernières nouvelles sur les animés de myanimelist.net.
➢ /aniquote - Obtenez des citations aléatoires géniales d'animés.
➢ /character [nom] - Obtenez des informations sur le personnage.

REMARQUE :
• Hokage doit avoir des privilèges d'administrateur.
• Ces commandes fonctionnent à la fois en message privé et en groupe.
• Ces commandes peuvent être utilisées par n'importe quel membre du groupe."""

    FSUB_TXT = """
Forcer les membres à rejoindre le canal avant d'écrire sur le chat !

UTILISATION :
➢ /fsub - Obtenir le statut actuel.
➢ /fsub [off] - Désactiver le forcesub dans le chat.
➢ /fsub [ID du canal / nom d'utilisateur] - Configurer le canal forcesub.
➢ /fsub [clear] - Démuter tous les membres qui sont muets.

REMARQUE :
• Hokage doit avoir les privilèges d'administrateur.
• Ces commandes fonctionnent à la fois en message privé et dans les groupes.
• Ces commandes peuvent être utilisées par n'importe quel membre du groupe.</b>"""

    DONATION_TXT = """<b>dons</b> 

<b>Êtes-vous intéressé à aider mon créateur dans ses efforts pour me maintenir en développement actif ? Si oui, vous êtes au bon endroit. 

Nous mettons l'accent sur l'importance de la nécessité de fonds pour maintenir Hokage Bot sous développement actif. Vos dons, quel que soit le montant, pour les serveurs de Hokage Bot et autres utilitaires, nous permettront de soutenir sa longévité à long terme. Nous utiliserons tous les dons pour couvrir les dépenses futures et les mises à jour des coûts des serveurs. Si vous avez de l'argent à nous aider dans cet effort, merci de le faire, et vos dons pourront également nous motiver à continuer d'apporter de nouvelles fonctionnalités.

Vous pouvez aider le développement avec des dons.</b>"""

    ZOMBIES_TXT = """<b>Aidez-vous à expulser les utilisateurs

Expulser les membres inactifs du groupe. Ajoutez-moi en tant qu'administrateur avec la permission d'expulser des utilisateurs dans le groupe.

COMMANDES ET UTILISATION :

• /inkick - Commande avec des arguments requis et j'expulserai les membres du groupe.
• /instatus - Vérifier le statut actuel des membres du chat dans le groupe.
• /inkick within_month long_time_ago - Expulser les utilisateurs inactifs depuis plus de 6-5 jours.
• /inkick long_time_ago - Expulser les membres inactifs depuis plus d'un mois et les comptes supprimés.
• /dkick - Expulser les comptes supprimés.</b>"""

    REPORT_MSG = """Rapport aux administrateurs"""

    REPORT_TXT = """@admins, @admins, /report. Pour rapporter aux administrateurs (fonctionne uniquement dans le groupe)"""

    VSONG = """
» Commandes disponibles pour la musique et la vidéo :

➻ /vsong - Télécharger une chanson YouTube
➻ /vvideo - Télécharger une vidéo YouTube
➻ /song - Téléchargeur de chanson Spotify
"""
    CHATAI = """
» Commandes disponibles pour Chat AI :

L'IA peut répondre à vos questions et vous montrer les résultats.

 ❍ /chatgpt : répondre à un message ou donner un texte
 ❍ /Hokage : répondre à un message ou donner un texte
 ❍ /ask : IA Google
 ❍ /gpt : ChatGPT
 ❍ /chat : répondre à un message ou donner un texte
"""

    ENCRYPT = """
» Commandes disponibles pour Encrypt :

Convertir
 ❍ /encrypt : crypte le texte donné
 ❍ /decrypt : décrypte un texte précédemment crypté
 ❍ /encode : encode le texte donné
 ❍ /decode : décode un texte précédemment crypté
 ❍ /morseencode : encode le texte donné en morse
 ❍ /morsedecode : décrypte un texte précédemment encodé en morse
 ❍ /password : donne la longueur du mot de passe à générer
 ❍ /uselessfact : génère un fait inutile aléatoire
"""

    YTSEARCH = """
Le module de recherche YouTube est une fonctionnalité de la plateforme YouTube qui permet aux utilisateurs de rechercher des vidéos, des chaînes ou des sujets spécifiques. Lorsque vous entrez une requête dans la barre de recherche sur YouTube, le module de recherche affiche les résultats pertinents basés sur votre requête. Vous pouvez filtrer les résultats par vidéos, chaînes, playlists ou émissions en direct pour trouver le contenu que vous recherchez. Le module de recherche propose également des suggestions pendant que vous tapez, facilitant ainsi la découverte de nouveau contenu sur YouTube. De plus, le module de recherche peut afficher des vidéos tendance ou populaires liées à votre requête. Globalement, le module de recherche YouTube est un outil puissant qui aide les utilisateurs à trouver et explorer une large gamme de contenus vidéo sur la plateforme.

Commande
 ❍ /ytsearch : rechercher une vidéo sur YouTube
 ❍ /google : recherche sur Google
"""
    FIGLET_TXT = """
» Commandes disponibles pour Figlet :

❍ /figlet : crée un figlet du texte donné
Exemple :

/figlet HYOSHCODER
"""

    WALL = """
» Commandes disponibles pour les fonds d'écran :

❍ /wall : recherche un fond d'écran du texte donné
❍ /wallpaper : recherche un fond d'écran du texte donné
Exemple :

/wall HYOSHCODER
"""

    GROUPDATA = """
Obtenez des informations sur le groupe

 ❍ /groupdata
 ❍ /groupinfo

Note : fonctionne uniquement dans les groupes
"""

    TAGALL = """
» Commandes disponibles pour Tag All :

Uniquement pour les admins

❍ /tagall ou @all '(répondez au message ou ajoutez un autre message) Mentionner tous les membres de votre groupe, sans exception.'
❍ /tagoff : annuler toutes les mentions
❍ /hitag : mentionner tous les membres
❍ /lifetag : mentionner tous les membres
❍ /histop ou /lifestop : annuler toutes les mentions
"""
    BG_TXT = """
Outil de suppression de fond :

Notre outil de suppression de fond est une solution puissante et facile à utiliser pour supprimer les fonds des images. En quelques clics, vous pouvez rapidement et précisément enlever le fond de n'importe quelle photo, vous laissant ainsi avec une image propre et professionnelle. Que vous soyez photographe cherchant à améliorer vos images ou graphiste travaillant sur un projet, notre outil de suppression de fond est la solution idéale pour tous vos besoins de retouche. Dites adieu à l'édition manuelle fastidieuse et laissez notre outil faire le travail pour vous, vous faisant gagner du temps et des efforts. Essayez-le dès aujourd'hui et voyez la différence qu'il peut apporter à vos images !

Exemple : /rmbg en répondant à une image
"""

    TORRENT = """
Commande de recherche de torrent

Exemple : /torrent braquage d'argent
"""

    RING_TXT = """
Commande de sonnerie

Vous pouvez demander une sonnerie dans le format /ringtune {nom_de_chanson + nom_artiste} ou {nom_de_chanson}
"""

    FUN_TXT = """
Rendez vos discussions amusantes avec de nombreux modules amusants !

UTILISATION :
➢ /punch - Envoie des GIFs de coups aléatoires.
➢ /slap - Envoie des GIFs de gifles aléatoires.
➢ /lick - Envoie des GIFs de léchage aléatoires.
➢ /kill - Envoie des GIFs de meurtres aléatoires.
➢ /kick - Envoie des GIFs de coups de pied aléatoires.
➢ /hug - Envoie des GIFs de câlins aléatoires.
➢ /dare - Joue à la vérité ou défi.
➢ /truth - Joue à la vérité ou défi.
➢ /bite - Envoie des GIFs de morsures aléatoires.
➢ /meme - Des memes géniaux à chaque fois.
➢ /kiss - Envoie des GIFs de baisers aléatoires.
➢ /waifu - Obtient un waifu aléatoire.
➢ /highfive - Envoie des GIFs de highfive aléatoires.
"""

    MONGO_TXT = """
Commande de vérification MongoDB

Entrez votre URL MongoDB après la commande.

Exemple : /mongo votre_url_mongodb
"""
    SPECIAL_MOD1 = """
» Commandes disponibles pour Aï et images AI :

 ➻ /imagine : Générer une image AI à partir d'un texte
 ➻ /mahadev : Générer une image de Mahadev
 ➻ /upscale : Mettre à l'échelle vos images
 ➻ /gpt : ChatGPT
 ➻ /draw : Créer des images

NOTE :
• L'admin doit avoir des privilèges admin.
• Ces commandes fonctionnent aussi bien en PM qu'en groupe.
• Ces commandes peuvent être utilisées par n'importe quel membre de groupe.

Alimenté par Hyosh coder Bots...
"""

    SPECIAL_MOD2 = """Voici l'aide pour le module Fake Info :
UTILISATION :
➢ /fake` : Générer des informations fausses
➢ /picgen` : Générer une fausse image

NOTE :
• L'admin doit avoir des privilèges admin.
• Ces commandes fonctionnent aussi bien en PM qu'en groupe.
• Ces commandes peuvent être utilisées par n'importe quel membre de groupe.

Alimenté par Hyosh coder Bots...
"""

    EXTRA_MOD = """
Fonctionnalités supplémentaires :

➢ /imdb - Infos sur un film (IMDB).
➢ /eval - Évaluer du code.
➢ /info - Obtenir vos infos.
➢ /animememe - Memes d'anime.
➢ /write - Écrire du texte à la main.
➢ /afk - Marquer comme AFK.
➢ /truth - Vérité aléatoire.
➢ /dare - Défi aléatoire.
➢ /song - Télécharger une chanson (YouTube).
➢ /spotify - Détails d'une chanson.
➢ /instagram - Télécharger des Reels/Stories/Posts (public).
➢ /autorequest - Ajoutez-moi à votre groupe/canal.
➢ /t2f - Convertir texte en fichier.
➢ /logo (Texte) - Créer un logo.
➢ /animelogo (Texte) - Logo style anime.

NOTE :
• Admin requis pour certaines commandes.
• Fonctionne en MP et en groupe.
• Accessible à tous les membres.

Alimenté par Hyosh coder Bots...
"""

    ADMINS = """
Mon Proriétaire est @hyoshdesign"""


    SPECIAL_TXT = """
Vérifiez votre module préféré
"""

    EXPERT_TXT = """
Voici quelques commandes IA/expert

 ➻ /mahadev : Générer une image Mahadev
 ➻ /fakegen : Générer de fausses informations
 ➻ /picgen : Générer une fausse image
 ➻ /eval : Évaluer du code simple
 ➻ /ask : Répondre à un message ou fournir du texte
 ➻ /draw : Créer des images
 ➻ /upscale : Améliorer vos images
 ➻ /gpt : ChatGPT
 ➻ /Hokage : IA par Google
 ➻ /reverse : Recherche d'image inversée
 ➻ /imagine : Créer des images IA

Note :
• Hokage doit avoir des privilèges d'administrateur.
• Ces commandes fonctionnent sur les deux PM et groupes.
• Ces commandes peuvent être utilisées par n'importe quel membre de groupe.

Alimenté par Hyosh coder Bots..
"""

    SUPPORT_TXT = """Voici mes canaux et groupes de support. Si vous avez un problème, signalez-le à l'administrateur.
Alimenté par - @hyoshassistantbot"""

    STATUS_TXT = """<b>    
‣ Statistiques actuelles de Hokage :

• Fichiers totaux : <code>{}</code>
• Utilisateurs totaux : <code>{}</code>
• Groupes totaux : <code>{}</code>
• Stockage utilisé : <code>{}</code>
• Stockage libre : <code>{}</code>
</b>"""

    LOG_TEXT_G = """<b>#Nouveau_Grᴏᴜᴘ

◉ Groupe: {}(<code>{}</code>)
◉ Membres: {}
◉ Ajouté par: {}"""

    LOG_TEXT_P = """#Nouvel_Utilisateur
    
◉ ID Utilisateur: <code>{}</code>
◉ Nom d'utilisateur: {}"""

    ALRT_TXT = """{},
Faite votre propre demande 😤
"""

    OLD_ALRT_TXT = """Hé {},
vous utilisez l'un de mes anciens messages,
veuillez renvoyer la demande."""
    
    CUDNT_FND = """😴 Votre demande n'a pas été trouvée dans ma base de données.**\n\n» Peut-être que vous avez mal écrit, essayez à nouveau."""

    I_CUDNT = """<b>Désolé, aucun fichier n'a été trouvé pour votre demande {} 

Le film n'est pas disponible pour les raisons suivantes :

1) Pas encore sorti en O.T.T ou DVD

2) Tapez le nom avec l'année

3) Le film n'est pas disponible dans la base de données, contactez les admins pour signaler</b>"""

    I_CUD_NT = """<b>Je n'ai pas pu trouver de film lié à {}.

Le film n'est pas disponible pour les raisons suivantes :

1) Pas encore sorti en O.T.T ou DVD

2) Tapez le nom avec l'année

3) Le film n'est pas disponible dans la base de données, contactez les admins pour signaler</b>"""

    MVE_NT_FND = """<b>Désolé, aucun fichier n'a été trouvé pour votre demande 😕

Le film n'est pas disponible pour les raisons suivantes :

1) Pas encore sorti en O.T.T ou DVD

2) Tapez le nom avec l'année

3) Le film n'est pas disponible dans la base de données, contactez les admins pour signaler</b>"""

    TOP_ALRT_MSG = """Recherche dans ma base de données..."""

    MELCOW_ENG = """<b>›› Salut {}, bienvenue sur {} \n\nIci, tu peux rechercher tes films ou séries préférés en tapant simplement leur nom\n\n›› Si tu rencontres des problèmes concernant le téléchargement ou autre chose, envoie un message ici</b>"""

    DISCLAIMER_TXT = """<b>Ceci n'est pas un projet open source.

Tous les fichiers présents dans ce bot sont librement accessibles sur Internet ou postés par quelqu'un d'autre. Ce bot indexe simplement des fichiers qui sont déjà téléchargés sur Telegram. Nous respectons toutes les lois sur le droit d'auteur et agissons en conformité avec le DMCA et l'ECD. Si quelque chose viole la loi, merci de me contacter pour qu'il soit retiré rapidement. Il est interdit de télécharger, diffuser, reproduire, partager ou consommer du contenu sans permission explicite de l'auteur du contenu ou du détenteur des droits d'auteur. Si vous pensez que ce bot enfreint vos droits de propriété intellectuelle, contactez les chaînes concernées pour le retrait. Le bot ne possède aucun de ces contenus, il indexe simplement les fichiers présents sur Telegram.

 Maintenu par : <a href="https://t.me/hyoshassistantbot">Hyosh Coder</a></b>"""
    USERS_TXT = """👋 Salut {},

📚 Voici la liste de mes commandes pour tous les utilisateurs du bot ⇊
    
• /batch - Créer un lien de lot pour plusieurs fichiers.
• /link - Créer un lien de stockage pour un fichier unique.
• /pbatch - Comme <code>/batch</code>, mais les fichiers seront envoyés avec des restrictions de transfert.
• /plink - Comme <code>/link</code>, mais le fichier sera envoyé avec des restrictions de transfert.
• /id - Obtenir l'ID d'un utilisateur spécifié.
• /info  - Obtenir des informations sur un utilisateur.
• /imdb  - Obtenir les informations d'un film à partir de la source IMDb.
• /search  - Obtenir les informations d'un film à partir de diverses sources.
• /stats - Obtenir le statut des fichiers dans la base de données.
• /request - Envoyer une demande de film/série aux administrateurs du bot. (Fonctionne uniquement dans les groupes de support)
• /plan - Vérifier les plans d'abonnement premium disponibles.
• /myplan - Vérifier votre plan actuel."""

    GROUP_TXT = """👋 Salut {},

📚 Voici la liste de mes commandes pour tous les propriétaires de groupe ⇊
    
• /connect  - Connecter un chat particulier à votre message privé.
• /disconnect  - Se déconnecter d'un chat.
• /set_shortlink - Connecter votre site de raccourcisseur d'URL.
• /set_tutorial - Définir comment télécharger une vidéo.
• /remove_tutorial - Retirer les instructions de téléchargement de vidéo.
• /shortlink_info - Vérifier les informations de votre groupe.
• /setshortlinkon - Activer le lien court pour votre groupe.
• /setshortlinkoff - Désactiver le lien court pour votre groupe.
• /connections - Liste de toutes vos connexions.
• /settings - Modifier les paramètres selon vos souhaits.
• /filter - Ajouter un filtre dans un groupe.
• /filters - Liste de tous les filtres dans un groupe.
• /del - Supprimer un filtre spécifique dans un groupe.
• /delall - Supprimer tous les filtres dans un groupe.
• /purge - Supprimer tous les messages de la réponse à ce message jusqu'au message actuel."""

    ADMINS_TXT = """Salut {},
📚 Commandes admins ⇊
• /logs - Erreurs récentes.
• /delete - Supprimer un fichier de la DB.
• /users - Liste des utilisateurs et ID.
• /leave - Quitter un chat.
• /disable - Désactiver un chat.
• /ban - Bannir un utilisateur.
• /unban - Débannir un utilisateur.
• /channel - Liste des groupes connectés.
• /broadcast - Diffuser un message à tous.
• /grp_broadcast - Diffuser à tous les groupes.
• /gfilter - Ajouter des filtres globaux.
• /gfilters - Voir les filtres globaux.
• /delg - Supprimer un filtre global.
• /delallg - Supprimer tous les filtres.
• /deletefiles - Supprimer CamRip/PreDVD.
• /send - Envoyer un message à un utilisateur.
• /gsend - Envoyer à un groupe.
• /add_premium - Ajouter un utilisateur premium.
• /remove_premium - Retirer du premium.
• /premium_users - Liste utilisateurs premium.
• /get_premium - Infos utilisateur premium.
• /restart - Redémarrer le bot."""

    MANAGEMENT_TXT = """
👮🏻 Commandes pour admins et modérateurs.

🕵🏻 /settings - Gérer les paramètres du bot.
👮🏻 /ban - Bannir un utilisateur.
👮🏻 /mute - Mode lecture seule pour un utilisateur.
👮🏻 /kick - Expulser un utilisateur.
👮🏻 /unban - Retirer un utilisateur de la liste noire.
👮🏻 /report - Signaler un message à un admin [utilisateurs].
👮🏻 /fp - Envoyer un retour [utilisateurs].
👮🏻 /connect - Connecter votre groupe au bot.
👮🏻 /filter - Ajouter un filtre dans le groupe.
👮🏻 /filters - Liste des filtres dans le groupe.
👮🏻 /del - Supprimer un filtre spécifique.
👮🏻 /delall - Supprimer tous les filtres.
👮🏻 /purge - Supprimer des messages en réponse.
👮🏻 /promote - Promouvoir un utilisateur au rôle d'admin.
👮🏻 /demote - Rétrograder un utilisateur.

REMARQUE :
• Privilèges admin requis.
• Commandes fonctionnent en privé et en groupe.
• N'importe quel membre peut les utiliser.

Alimenté par Hyosh coder Bots.
"""


    SHORTLINK_INFO = """
 <b>❗<u>COMMENT GAGNER DE L'ARGENT AVEC LE BOT</u>❗

★ Maintenant, vous pouvez commencer à gagner de l'argent 💸 dès aujourd'hui avec notre bot simple et facile à utiliser !

›› Étape 1 : Ajoutez ce bot à votre groupe en tant qu'administrateur...

›› Étape 2 : Utilisez /connect dans votre groupe pour connecter le bot à votre messagerie privée.

›› Étape 3 : Cliquez sur le bouton suivant pour savoir comment connecter le site de raccourcissement de lien avec ce bot.

★ Ne tardez plus à commencer à gagner de l'argent avec votre groupe Telegram. Ajoutez notre bot aujourd'hui et commencez à gagner de l'argent 💰 !</b>
"""

    SHORTLINK_INFO2 = """<b>
❗<u>COMMENT CONNECTER VOTRE RACCOURCISSEUR DE LIENS</u>❗

›› Étape 4 : Si vous n'utilisez pas encore de site de raccourcissement de liens, créez d'abord un compte sur publicearn.com (vous pouvez également utiliser d'autres sites de raccourcissement de liens).

›› Étape 5 : Copiez votre API depuis le site Web, puis définissez simplement votre site Web et votre API en utilisant la commande /set_shortlink.

›  Exemple :</b> <code>/set_shortlink publicearn.com 1502a197c85d59929d50f1cba1d5e967d1e962</code>

<b>›› Étape 6 : Cliquez sur le bouton suivant pour savoir comment connecter votre tutoriel avec ce bot.

★ Ce bot convertira automatiquement les liens avec votre API et vous fournira vos liens.</b>
"""
    SHORTLINK_INFO3 = """<b>
❗<u>COMMENT CONNECTER VOTRE TUTORIEL</u>❗

›› Étape 7 : Utilisez /set_tutorial pour ajouter comment télécharger des vidéos pour votre site de raccourcissement de liens.

› Exemple :</b> <code>/set_tutorial https://t.me/How_to_Download_7x/35</code>

<b>›› Étape 8 : Si vous voulez vérifier quel raccourcisseur de liens vous avez connecté à votre groupe, envoyez la commande /shortlink_info à votre groupe.

★ C'est tout, vous pouvez maintenant gagner beaucoup d'argent 💸 en utilisant ce bot.</b>
"""
    
    SELECT = """
➢ Cliquez sur "Qualité" pour obtenir le fichier dans la qualité souhaitée.
➢ Cliquez sur "Langue" pour obtenir le fichier dans la langue souhaitée.
➢ Cliquez sur "Saison" pour obtenir le fichier dans la saison souhaitée.

➢ Cliquez sur "♨️ Envoyer tous les fichiers ♨️" pour obtenir tous les fichiers en un seul clic.

✯ Maintenu par : Hyosh Coder
"""

    REQINFO = """➢ Cliquez sur "Qualité" et changez la qualité.
➢ Cliquez sur "Langue" et changez la langue.
➢ Cliquez sur "Saison" et changez la saison.
➢ Cliquez sur "♨️ Envoyer tous les fichiers ♨️" et obtenez tous les fichiers."""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
Format de requête des séries
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

Allez sur Google ➠ Tapez le nom de la série ➠ Copiez le nom correct ➠ Collez dans ce groupe

Exemple : Loki S01E01

🚯 Ne pas utiliser ➠ ':(!,./)"""

    NORSLTS = """ 
#PasDeRésultats

Id : <code>{}</code>
Nom : {}

Message : <b>{}</b>"""
 
   # MERCI DE NE PAS ENLEVER LES CRÉDITS ❤️‍🩹
    
    CAPTION = """
<b>• {file_name}

• Alimenté par : <a href="https://t.me/botZflix">BotZFlix</a></b>"""

    IMDB_TEMPLATE_TXT = """
<b>Requête : {query}
Données IMDb :

‣ Titre : <a href={url}>{title}</a>
‣ Genres : {genres}
‣ Année : <a href={url}/releaseinfo>{year}</a>
‣ Note : <a href={url}/ratings>{rating}</a> / 10 (Basée sur {votes} évaluations d'utilisateurs)
‣ Langue : <code>{languages}</code></a>
‣ Durée : {runtime} minutes</a>

‣ Histoire : {plot}

‣ Requis par : {message.from_user.mention}</b>"""

    RESTART_TXT = """
<b>Bot redémarré !

📅 Date : <code>{}</code>
⏰ Heure : <code>{}</code>
🌐 Fuseau horaire : <code>UTC</code>
🛠️ Statut de la version : <code>v4.4 [Stable]</code></b>"""
    LOGO = """
hyosh coder 
"""

    PAGE_TXT = """pourquoi êtes-vous si curieux ⁉️"""

    PURCHASE_TXT = """sélectionnez votre méthode de paiement."""

    PREMIUM_TEXT = """<b>👋 salut {},
    
🎖️ <u>plans disponibles</u>

● <code>05$</code> ➛ <u>plan bronze</u> » <code>7 jours</code>
● <code>20$</code> ➛ <u>plan argent</u> » <code>30 jours</code>
● <code>30$</code> ➛ <u>plan or</u> » <code>90 jours</code>
● <code>50$</code> ➛ <u>plan platine</u> » <code>180 jours</code>
● <code>100$</code> ➛ <u>plan diamant</u> » <code>365 jours</code>

💵 identifiant UPI - <code>dm - @kingcey</code>
📸 code QR - <a href='https://graph.org/file/02e7ecc3e2693b481b914.jpg'>cliquez ici pour scanner</a>

⚜️ vérifiez votre plan actif en utilisant : /myplan

‼️ vous devez envoyer une capture d'écran après le paiement.</b>"""

    CPREMIUM_TEXT = """<b>👋 salut {},
    
🎖️ <u>plans disponibles</u> :

● <code>05$</code> ➛ <u>plan bronze</u> » <code>7 jours</code>
● <code>20$</code> ➛ <u>plan argent</u> » <code>30 jours</code>
● <code>30$</code> ➛ <u>plan or</u> » <code>90 jours</code>
● <code>50$</code> ➛ <u>plan platine</u> » <code>180 jours</code>
● <code>100$</code> ➛ <u>plan diamant</u> » <code>365 jours</code>

💵 identifiant UPI - <code>dm - @kingcey</code>
📸 code QR - <a href='https://graph.org/file/02e7ecc3e2693b481b914.jpg'>cliquez ici pour scanner</a>

⚜️ vérifiez votre plan actif en utilisant : /myplan

‼️ vous devez envoyer une capture d'écran après le paiement.</b>"""

    PLAN_TXT = """<b>👋 salut {},
    
🎁 <u>caractéristiques premium</u> :

○ pas besoin d'ouvrir les liens
○ fichiers directs   
○ expérience sans publicité 
○ lien de téléchargement à grande vitesse                         
○ streaming multi-joueurs de liens                           
○ films et séries illimités                                                                        
○ support complet de l'administrateur                              
○ la demande sera complétée en 1h [si disponible]

➛ utilisez /plan pour voir tous nos plans en une seule fois.
➛ vérifiez votre plan actif en utilisant : /myplan

‼️ après avoir envoyé une capture d'écran, veuillez nous accorder un peu de temps pour vous ajouter à la liste premium.</b>"""

    FREE_TXT = """<b>👋 Salut {},
    
🎉 <u>ESSAI GRATUIT</u> 🎉
❗ Seulement pour 5 minutes
 
○ Pas besoin d'ouvrir les liens
○ Streaming multi-joueurs avec liens
○ Expérience sans publicité

👨‍💻 Contactez le <a href='https://t.me/hyoshassistantbot'>propriétaire</a> pour obtenir votre essai.

➛ Utilisez /plan pour voir tous nos plans immédiatement.
➛ Vérifiez votre plan actif en utilisant : /myplan</b>"""

    BRONZE_TXT = """<b>👋 Salut {},
    
🥉 <u>PLAN BRONZE</u>
⏰ 7 jours
💸 Prix du plan ➛ 05$

➛ Utilisez /plan pour voir tous nos plans immédiatement.
➛ Vérifiez votre plan actif en utilisant : /myplan</b>"""

    SILVER_TXT = """<b>👋 Salut {},
    
🥈 <u>PLAN ARGENT</u>
⏰ 30 jours
💸 Prix du plan ➛ 20$

➛ Utilisez /plan pour voir tous nos plans immédiatement.
➛ Vérifiez votre plan actif en utilisant : /myplan</b>"""

    GOLD_TXT = """<b>👋 Salut {},
    
🥇 <u>PLAN OR</u>
⏰ 90 jours
💸 Prix du plan ➛ 30$

➛ Utilisez /plan pour voir tous nos plans immédiatement.
➛ Vérifiez votre plan actif en utilisant : /myplan</b>"""

    PLATINUM_TXT = """<b>👋 Salut {},

🏅 <u>PLAN PLATINUM</u>
⏰ 180 JOURS
💸 Prix du plan ➛ 50$

➛ Utilisez /plan pour voir tous nos plans en une seule fois.
➛ Vérifiez votre plan actif en utilisant : /myplan</b>"""

    DIAMOND_TXT = """<b>👋 Salut {},

💎 <u>PLAN DIAMANT</u>
⏰ 365 JOURS
💸 Prix du plan ➛ 100$

➛ Utilisez /plan pour voir tous nos plans en une seule fois.
➛ Vérifiez votre plan actif en utilisant : /myplan</b>"""

    OTHER_TXT = """<b>👋 Salut {},

🎁 <u>AUTRE PLAN</u>
⏰ JOURS PERSONNALISÉS
💸 Selon le nombre de jours que vous choisissez

🏆 Si vous souhaitez un nouveau plan à part de celui donné, vous pouvez contacter notre <a href='https://t.me/hyoshassistantbot'>PROPRIÉTAIRE</a> directement en cliquant sur le bouton de contact ci-dessous.

👨‍💻 Contactez le propriétaire pour obtenir votre autre plan.

➛ Utilisez /plan pour voir tous nos plans en une seule fois.
➛ Vérifiez votre plan actif en utilisant : /myplan</b>"""

    UPI_TXT = """<b>👋 Salut {},

⚜️ Payez le montant correspondant à votre plan et profitez d'un abonnement PREMIUM !

💵 ID UPI - <code>dm - @kingcey</code>

‼️ Vous devez envoyer une capture d'écran après le paiement.</b>"""

    QR_TXT = """<b>👋 Salut {},

⚜️ Payez le montant correspondant à votre plan et profitez d'un abonnement PREMIUM !

📸 QR Code - <a href='https://graph.org/file/02e7ecc3e2693b481b914.jpg'>Cliquez ici pour scanner</a>

‼️ Vous devez envoyer une capture d'écran après le paiement.</b>"""

    PREPLANS_TXT = """<b>👋 Salut {},

🎖️ <u>PLANS DISPONIBLES</u> :

● <code>10$</code> ➛ <u>PLAN BRONZE</u> » <code>7 JOURS</code>
● <code>60$</code> ➛ <u>PLAN ARGENT</u> » <code>30 JOURS</code>
● <code>180$</code> ➛ <u>PLAN OR</u> » <code>90 JOURS</code>
● <code>250$</code> ➛ <u>PLAN PLATINUM</u> » <code>180 JOURS</code>
● <code>400$</code> ➛ <u>PLAN DIAMANT</u> » <code>365 JOURS</code>

💵 ID UPI - <code>dm - @hyoshassistantbot</code>
📸 QR Code - <a href='https://graph.org/file/02e7ecc3e2693b481b914.jpg'>Cliquez ici pour scanner</a>

⚜️ Vérifiez votre plan actif en utilisant : /myplan

‼️ Vous devez envoyer une capture d'écran après le paiement.</b>"""

    DEVELOPER_TXT = """
Merci spécial ❤️ Développeur -

-Dev [Propriétaire de ce bot ]<a href='https://t.me/kingcey'>🇰ιηg¢єу</a>
"""

Script = script()
