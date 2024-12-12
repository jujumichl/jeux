import pygame
import random
import pooPoke
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN

pygame.init() #initialise pygame

# Créer la fenêtre de 700 x 800 pixels
largeur, hauteur = 700, 800
f1 = pygame.display.set_mode((largeur, hauteur))
# créer une surface dédier a l'affichage des stats des pokémons
details_surface = pygame.Surface((200, 345))
details_surface.fill((0, 0, 0)) # efface cette surface
# Récupérer les dimensions actuelles de la fenêtre
f1_width, f1_height = pygame.display.get_surface().get_size()
#nomme la fenêtre dokémon
pygame.display.set_caption("Dokémon")
# créer la variable size qui sert a redimentionner des images, sert principalement pour le fond
size = f1_width, f1_height
pokedex_image = pygame.transform.scale(pygame.image.load("image/fondPokedexSon/pokedex.png"),size) # image de fond
#charger le son
pygame.mixer.music.load("image/fondPokedexSon/pokedex.mp3")
# Jouer le son en boucle
pygame.mixer.music.play(-1)
#variables
pokedex_x, pokedex_y = 0, 0 
size1= 300,300 # variable servant a redimentionner les images des pokémons 
# Chemin du fichier bloc note qui contient l'équipe du joueur
fichier_bloc_note = "note/equipe_pokemon.txt"
# Chemin du deuxième fichier bloc note qui contient l'équipe adverse
fichier_bloc_note_2 = "note/equipe_pokemon_2.txt"
# Liste pour stocker l'équipe de Pokémon du joueur
team_pokemon = []
# # Liste pour stocker l'équipe de Pokémon de l'adversaire
team_pokemon_2 = []
# Données des Pokémon
pokedex_pokemon = [
    {"name": "Scovilain", "type": "Plante/Feu", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Scovillain.png"),size1),
     "attack": {1:"Charge", 2: "Vive-Attaque", 3:"Grincement",4:"Jet de Sable"}, "stats":{"HP": 65, "Attack": 108, "Defense": 65, "vitesse": 75,"HP_reference": 65}},
    {"name": "Cotovol", "type": "Plante/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/cotovol.png"),size1),
     "attack":{1:"Rugissement", 2:"Charge", 3:"Chargeur", 4:"Ruse"},"stats":{"HP": 75, "Attack": 55, "Defense": 70, "vitesse": 110,"HP_reference": 75}},
    {"name": "Shaymin", "type": "Plante", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/shymin.png"),size1),
     "attack": {1:"Pouvoir Lunaire", 2:"Choc Mental", 3:"Rafale Psy", 4:"Croissance"},"stats":{"HP": 100, "Attack": 100, "Defense": 100, "vitesse": 100,"HP_reference": 100}},
    {"name": "Éoko", "type": "Psy", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Eoko.png"),size1),
     "attack":{1:"Rayon Chargé",2: "Grincement", 3:"Chargeur", 4:"Force Poigne"},"stats":{"HP": 75, "Attack": 50, "Defense": 80, "vitesse": 65,"HP_reference": 75}},
    {"name": "Sulfura", "type": "Fée/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/sulfura.png"),size1),
     "attack":{1:"Griffe", 2: "Groz'Yeux", 3:"Mimi-Queue", 4:"Danse Flamme"},"stats":{"HP": 90,"Attack": 100, "Defense": 90, "vitesse": 90, "HP_reference": 90}},
    {"name": "Granbull", "type": "Fée", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Granbull.png"),size1),
     "attack":{1:"Morsure", 2:"Groz'Yeux", 3:"Chant Canon", 4:"Regard Touchant"},"stats":{"HP": 90, "Attack": 120, "Defense": 75, "vitesse": 45,"HP_reference": 90}},
    {"name": "Dracaufeu", "type": "Feu/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/dracaufeu.png"),size1),
     "attack":{1:"Flammeche", 2:"Rugissement", 3:"Griffe", 4:"Pistolet à O"},"stats":{"HP": 78, "Attack": 84, "Defense": 78, "vitesse": 100,"HP_reference": 78}},
    {"name": "Hyporoi", "type": "Eau/Dragon", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/hypoproi.png"),size1),
     "attack":{1:"Pistolet à O", 2:"Charge", 3:"Souplesse", 4:"Coup d'Boule"},"stats":{"HP": 75,"Attack": 95, "Defense": 95, "vitesse": 85, "HP_reference": 75}},
    {"name": "Dracolosse", "type": "Drangon/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/dracolosse.png"),size1),
     "attack":{1:"Lézard'O", 2:"Colère", 3:"Coud'Boue", 4:"Draco-Rage"},"stats":{"HP": 91, "Attack": 134, "Defense": 95, "vitesse": 80,"HP_reference": 91}},
    {"name": "Symbios", "type": "Psy", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/symbios.png"),size1),
     "attack":{1:"Griffe", 2:"Groz'Yeux", 3:"Rayon Chargé", 4:"Boul'Armure"},"stats":{"HP": 110, "Attack": 65, "Defense": 75, "vitesse": 30,"HP_reference": 110}},
    {"name": "Exagide", "type": "Acier/Spectre", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/exagideB.png"),size1),
     "attack":{1:"Tranche", 2:"Éclat Magique", 3:"Lame-Feuille", 4:"Mur Lumière"},"stats":{"HP": 60, "Attack": 50, "Defense": 140, "vitesse": 60,"HP_reference": 60}},
    {"name": "Nymphali", "type": "Fée", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/nymphali.png"),size1),
     "attack":{1:"Jet de Sable", 2:"Vent Féérique", 3:"Séduction", 4:"Rafale Psy"},"stats":{"HP": 95, "Attack": 65, "Defense": 65, "vitesse": 60,"HP_reference": 95}},
    {"name": "Yveltal", "type": "Ténèbre/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/yveltal.png"),size1),
     "attack":{1:"Tranche", 2:"Cru-Aile", 3:"Hurlement", 4:"Vent Mauvais"},"stats":{"HP": 126, "Attack": 131, "Defense": 95, "vitesse": 99,"HP_reference": 126}},
    {"name": "Tortank", "type": "Eau", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/tortank.png"),size1),
     "attack":{1:"Charge", 2:"Mimi-Queue", 3:"Pistolet à O", 4:"Rugissement"},"stats":{"HP": 79, "Attack": 83, "Defense": 100, "vitesse": 78,"HP_reference": 79}},
    {"name": "Zamazenta", "type": "Combat/Acier", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/zamazenta.png"),size1),
     "attack":{1:"Griffe", 2:"Groz'Yeux", 3:"Tranche", 4:"Coup d'Boule"},"stats":{"HP": 92, "Attack": 120, "Defense": 140, "vitesse": 128,"HP_reference": 92}}
]
# Donnée des pokémons Adverse
pokedex_pokemon1 = [
    {"name": "Scovilain_", "type": "Plante/Feu", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Scovillain.png"),size1),
     "attack": {1:"Charge", 2: "Vive-Attaque", 3:"Grincement",4:"Jet de Sable"}, "stats":{"HP": 65, "Attack": 108, "Defense": 65, "vitesse": 75,"HP_reference": 65}},
    {"name": "Cotovol_", "type": "Plante/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/cotovol.png"),size1),
     "attack":{1:"Rugissement", 2:"Charge", 3:"Chargeur", 4:"Ruse"},"stats":{"HP": 75, "Attack": 55, "Defense": 70, "vitesse": 110,"HP_reference": 75}},
    {"name": "Shaymin_", "type": "Plante", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/shymin.png"),size1),
     "attack": {1:"Pouvoir Lunaire", 2:"Choc Mental", 3:"Rafale Psy", 4:"Croissance"},"stats":{"HP": 100, "Attack": 100, "Defense": 100, "vitesse": 100,"HP_reference": 100,}},
    {"name": "Éoko_", "type": "Psy", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Eoko.png"),size1),
     "attack":{1:"Rayon Chargé",2: "Grincement", 3:"Chargeur", 4:"Force Poigne"},"stats":{"HP": 75, "Attack": 50, "Defense": 80, "vitesse": 65,"HP_reference": 75}},
    {"name": "Sulfura_", "type": "Fée/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/sulfura.png"),size1),
     "attack":{1:"Griffe", 2: "Groz'Yeux", 3:"Mimi-Queue", 4:"Danse Flamme"},"stats":{"HP": 90,"Attack": 100, "Defense": 90, "vitesse": 90, "HP_reference": 90}},
    {"name": "Granbull_", "type": "Fée", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Granbull.png"),size1),
     "attack":{1:"Morsure", 2:"Groz'Yeux", 3:"Chant Canon", 4:"Regard Touchant"},"stats":{"HP": 90, "Attack": 120, "Defense": 75, "vitesse": 45, "HP_reference": 90}},
    {"name": "Dracaufeu_", "type": "Feu/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/dracaufeu.png"),size1),
     "attack":{1:"Flammeche", 2:"Rugissement", 3:"Griffe", 4:"Pistolet à O"},"stats":{"HP": 78, "Attack": 84, "Defense": 78, "vitesse": 100,"HP_reference": 78,}},
    {"name": "Hyporoi_", "type": "Eau/Dragon", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/hypoproi.png"),size1),
     "attack":{1:"Pistolet à O", 2:"Charge", 3:"Souplesse", 4:"Coup d'Boule"},"stats":{"HP": 75,"Attack": 95, "Defense": 95, "vitesse": 85, "HP_reference": 75}},
    {"name": "Dracolosse_", "type": "Drangon/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/dracolosse.png"),size1),
     "attack":{1:"Lézard'O", 2:"Colère", 3:"Coud'Boue", 4:"Draco-Rage"},"stats":{"HP": 91, "Attack": 134, "Defense": 95, "vitesse": 80, "HP_reference": 91}},
    {"name": "Symbios_", "type": "Psy", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/symbios.png"),size1),
     "attack":{1:"Griffe", 2:"Groz'Yeux", 3:"Rayon Chargé", 4:"Boul'Armure"},"stats":{"HP": 110, "Attack": 65, "Defense": 75, "vitesse": 30,"HP_reference": 110}},
    {"name": "Exagide_", "type": "Acier/Spectre", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/exagideB.png"),size1),
     "attack":{1:"Tranche", 2:"Éclat Magique", 3:"Lame-Feuille", 4:"Mur Lumière"},"stats":{"HP": 60, "Attack": 50, "Defense": 140, "vitesse": 60,"HP_reference": 60}},
    {"name": "Nymphali_", "type": "Fée", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/nymphali.png"),size1),
     "attack":{1:"Jet de Sable", 2:"Vent Féérique", 3:"Séduction", 4:"Rafale Psy"},"stats":{"HP": 95, "Attack": 65, "Defense": 65, "vitesse": 60,"HP_reference": 95}},
    {"name": "Yveltal_", "type": "Ténèbre/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/yveltal.png"),size1),
     "attack":{1:"Tranche", 2:"Cru-Aile", 3:"Hurlement", 4:"Vent Mauvais"},"stats":{"HP": 126, "Attack": 131, "Defense": 95, "vitesse": 99,"HP_reference": 126}},
    {"name": "Tortank_", "type": "Eau", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/tortank.png"),size1),
     "attack":{1:"Charge", 2:"Mimi-Queue", 3:"Pistolet à O", 4:"Rugissement"},"stats":{"HP": 79, "Attack": 83, "Defense": 100, "vitesse": 78,"HP_reference": 79}},
    {"name": "Zamazenta_", "type": "Combat/Acier", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/zamazenta.png"),size1),
     "attack":{1:"Griffe", 2:"Groz'Yeux", 3:"Tranche", 4:"Coup d'Boule"},"stats":{"HP": 92, "Attack": 120, "Defense": 140, "vitesse": 128,"HP_reference": 92}}
]

#police
font = pygame.font.Font(None, 26)
#variable pour définir le pokémon séléctionner
selected_pokemon = None
# condition pour faire fonctionner le progamme
en_cours = True 
# Variable pour stocker la saisie du nom du Pokémon et pour la noter dans l'équipe
input_text = ""
# définition servant a montrer les détail des pokémons séléctionner
def show_pokemon_details(selected_pokemon):
    details_surface.fill((0, 0, 0))  # Efface la surface précédente

    if selected_pokemon:
        #texte pour les détails du Pokémon
        font = pygame.font.Font(None, 24)
        text_y = 10
        #Récupère et affiche le nom du pokémon afficher
        text = font.render(f"Nom: {selected_pokemon['name']}", True, (255, 255, 255))
        details_surface.blit(text, (10, text_y))
        text_y += 30
        # récupère les attaques associer au pokémon afficher
        text = font.render("Attaques:", True, (255, 255, 255))
        details_surface.blit(text, (10, text_y))
        text_y += 30
        # affiche les attaques du Pokémon les unes en dessous des autres
        for attack, n in selected_pokemon['attack'].items():
            text = font.render(f"{attack}: {n}", True, (255, 255, 255))
            details_surface.blit(text, (20, text_y))
            text_y += 30
        # Récupère les statistique du pokémons actuellement afficher
        text = font.render("Statistiques:", True, (255, 255, 255))
        details_surface.blit(text, (10, text_y))
        text_y += 30
        # affiche toutes les statistique du pokémon actuellement afficher
        for stat, value in selected_pokemon['stats'].items():
            text = font.render(f"{stat}: {value}", True, (255, 255, 255))
            details_surface.blit(text, (20, text_y))
            text_y += 30

# Boucle principale
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.KEYDOWN:
            # Gère les touches du clavier pour la sélection et la sortie
            if event.key == pygame.K_ESCAPE:
                en_cours = False
            # lettre choisi pour séléctionner chaque pokémons
            elif event.key == pygame.K_1:
                selected_pokemon = pokedex_pokemon[0]
            elif event.key == pygame.K_2:
                selected_pokemon = pokedex_pokemon[1]
            elif event.key == pygame.K_3:
                selected_pokemon = pokedex_pokemon[2]
            elif event.key == pygame.K_4:
                selected_pokemon = pokedex_pokemon[3]
            elif event.key == pygame.K_5:
                selected_pokemon = pokedex_pokemon[4]
            elif event.key == pygame.K_6:
                selected_pokemon = pokedex_pokemon[5]
            elif event.key == pygame.K_7:
                selected_pokemon = pokedex_pokemon[6]
            elif event.key == pygame.K_8:
                selected_pokemon = pokedex_pokemon[7]
            elif event.key == pygame.K_9:
                selected_pokemon = pokedex_pokemon[8]
            elif event.key == pygame.K_0:
                selected_pokemon = pokedex_pokemon[9]
            elif event.key == pygame.K_a:
                selected_pokemon = pokedex_pokemon[10]
            elif event.key == pygame.K_z:
                selected_pokemon = pokedex_pokemon[11]
            elif event.key == pygame.K_e:
                selected_pokemon = pokedex_pokemon[12]
            elif event.key == pygame.K_r:
                selected_pokemon = pokedex_pokemon[13]
            elif event.key == pygame.K_t:
                selected_pokemon = pokedex_pokemon[14]
            elif event.key == pygame.K_RETURN:
                # La touche "Entrer" est pressée, ajoute le Pokémon à l'équipe
                if selected_pokemon and len(team_pokemon) < 6:
                    team_pokemon.append(selected_pokemon['name'])
                    # Écrit le nom du Pokémon dans le fichier bloc note
                    with open(fichier_bloc_note, 'a') as f:
                        f.write(f"{selected_pokemon['name']}\n")
                    # Choisis aléatoirement un Pokémon pour l'équipe adverse
                    random_pokemon_2 = random.choice(pokedex_pokemon1)
                    team_pokemon_2.append(random_pokemon_2['name'])
                    # Écrit le nom du Pokémon dans le deuxième fichier bloc note
                    with open(fichier_bloc_note_2, 'a') as f_2:
                        f_2.write(f"{random_pokemon_2['name']}\n")
            

    # Dessine les détails du pokémons séléctionner
    f1.blit(pokedex_image, (pokedex_x, pokedex_y))
    show_pokemon_details(selected_pokemon)
    if selected_pokemon:
        f1.blit(selected_pokemon["image"], (225, 250))

    # Affiche le texte donnant les instruction
    input_text_render = font.render(f"Pour séléctionner un pokémon appuyer sur une lettre comprise entre a et o inclus", True, (0, 180, 0))
    f1.blit(input_text_render, (10, f1_height - 225))
    input_text_render = font.render(f"et pour ajouter le pokémon séléctionner dans ton équipe appuie sur 'Entré'.", True, (0, 180, 0))
    f1.blit(input_text_render, (10, f1_height - 200))
    input_text_render = font.render(f"Attention tout choix de pokémon dans son équipe est définitif !!", True, (180, 0, 0))
    f1.blit(input_text_render, (10, f1_height - 175))
    input_text_render = font.render(f"Pour ajouter le pokémon les lettres sont dans l'ordre alphabéthique", True, (180, 0, 0))
    f1.blit(input_text_render, (10, f1_height - 150))
    # Affiche les Pokémon dans l'équipe
    team_text = font.render(f"Équipe: {', '.join(team_pokemon)}", True, (255, 0, 0))
    f1.blit(team_text, (10, f1_height - 250))
    
    f1.blit(details_surface, (500, 0))

    pygame.display.flip()
    # Vérifie si l'équipe est complète
    if len(team_pokemon) >= 6 and len(team_pokemon_2) >= 6:
        en_cours = False  # Sort de la boucle si l'équipe est complète
pygame.quit()
