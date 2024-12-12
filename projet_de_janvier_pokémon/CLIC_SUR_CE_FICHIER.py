import pygame # importation des différentes ressources dont ont a besoin dans ce programme
from pygame.locals import QUIT, KEYDOWN, K_RETURN, MOUSEBUTTONDOWN, K_RSHIFT
import time
import random
from pooPoke import JeuPokemon
import EcranTitre,pokedex_programs 
# initialise pygame
pygame.init()

# Créer une fenêtre qui fait 700 x 800
largeur, hauteur = 700, 800
f1 = pygame.display.set_mode((largeur, hauteur))
# Récupérer les dimensions actuelles de l'écran
f1_width, f1_height = pygame.display.get_surface().get_size()
# Charge et redimensionne les images à la taille size
size = f1_width, f1_height  
attack = pygame.transform.scale(pygame.image.load("image/box.png"), (300, 100)) # box servant de fond pour les attaques
combat4 = pygame.transform.scale(pygame.image.load("image/fondDeCombatSon/fond_4.jpg"), size)
pygame.mixer.music.load("image/fondDeCombatSon/VS.mp3")  # Charge le son
# Jouer le son en boucle
pygame.mixer.music.play(-1)
# Variable: Police, variable booléenne et taille de fenêtre
font = pygame.font.Font(None, 62)
font1 = pygame.font.Font(None, 32)
attack_triggered = False
size1 = 300, 300
# Index du Pokémon actuellement en combat
pokemon_index = 0
# Attaques disponibles pour le Pokémon en combat
attaques_disponibles = []
text_attaques = None
# Données des Pokémons joueur
pokedex_pokemon = [
    {"name": "Scovilain", "type": "Plante/Feu", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Scovillain.png"),size1),
     "attack": {1:"Charge", 2: "Vive-Attaque", 3:"Grincement",4:"Jet de Sable"}, "stats":{"HP": 65,"HP_reference": 65, "Attack": 108, "Defense": 65, "vitesse": 75,"HP_reference": 65}},
    {"name": "Cotovol", "type": "Plante/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/cotovol.png"),size1),
     "attack":{1:"Rugissement", 2:"Charge", 3:"Chargeur", 4:"Ruse"},"stats":{"HP": 75, "Attack": 55, "Defense": 70, "vitesse": 110,"HP_reference": 75}},
    {"name": "Shaymin", "type": "Plante", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/shymin.png"),size1),
     "attack": {1:"Pouvoir Lunaire", 2:"Choc Mental", 3:"Rafale Psy", 4:"Croissance"},"stats":{"HP": 100, "Attack": 100, "Defense": 100, "vitesse": 100,"HP_reference": 100,}},
    {"name": "Éoko", "type": "Psy", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Eoko.png"),size1),
     "attack":{1:"Rayon Chargé",2: "Grincement", 3:"Chargeur", 4:"Force Poigne"},"stats":{"HP": 75, "Attack": 50, "Defense": 80, "vitesse": 65,"HP_reference": 75}},
    {"name": "Sulfura", "type": "Fée/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/sulfura.png"),size1),
     "attack":{1:"Griffe", 2: "Groz'Yeux", 3:"Mimi-Queue", 4:"Danse Flamme"},"stats":{"HP": 90,"Attack": 100, "Defense": 90, "vitesse": 90, "HP_reference": 90}},
    {"name": "Granbull", "type": "Fée", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/Granbull.png"),size1),
     "attack":{1:"Morsure", 2:"Groz'Yeux", 3:"Chant Canon", 4:"Regard Touchant"},"stats":{"HP": 90, "Attack": 120, "Defense": 75, "vitesse": 45, "HP_reference": 90}},
    {"name": "Dracaufeu", "type": "Feu/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/dracaufeu.png"),size1),
     "attack":{1:"Flammeche", 2:"Rugissement", 3:"Griffe", 4:"Pistolet à O"},"stats":{"HP": 78, "Attack": 84, "Defense": 78, "vitesse": 100,"HP_reference": 78,}},
    {"name": "Hyporoi", "type": "Eau/Dragon", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/hypoproi.png"),size1),
     "attack":{1:"Pistolet à O", 2:"Charge", 3:"Souplesse", 4:"Coup d'Boule"},"stats":{"HP": 75,"Attack": 95, "Defense": 95, "vitesse": 85, "HP_reference": 75}},
    {"name": "Dracolosse", "type": "Drangon/Vol", "image": pygame.transform.scale(pygame.image.load("image/Pokemon/dracolosse.png"),size1),
     "attack":{1:"Lézard'O", 2:"Colère", 3:"Coud'Boue", 4:"Draco-Rage"},"stats":{"HP": 91, "Attack": 134, "Defense": 95, "vitesse": 80, "HP_reference": 91}},
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
     "attack": {1:"Charge", 2: "Vive-Attaque", 3:"Grincement",4:"Jet de Sable"}, "stats":{"HP": 65,"HP_reference": 65, "Attack": 108, "Defense": 65, "vitesse": 75,"HP_reference": 65}},
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

# Chemin du fichier texte
fichier_equipe_pokemon = "note/equipe_pokemon.txt" # joueur
fichier_equipe_pokemon2 = "note/equipe_pokemon_2.txt"# adversaire
#fichier_attaque_selectionnee = "note/dammageJ.txt"
#fichier_attaque_selectionnee1 = "note/dammageA.txt"
fichier_switch="note/switch.txt"#joueur
fichier_switch1 = "note/switch1.txt"#adversare
################################################################################
# 								Joueur											
################################################################################
# Ouvre le fichier en mode lecture
with open(fichier_equipe_pokemon, 'r') as fichier:
    # Lit les 6 premières lignes
    noms_pokemon_choisis = fichier.readlines()[-6:]
################################################################################
#								Adversaire										
################################################################################
# Ouvre le fichier en mode lecture
with open(fichier_equipe_pokemon2, 'r') as fichier:
    # Lit les 6 premières lignes
    noms_pokemon_choisis2 = fichier.readlines()[-6:]
    
# Définis une variable pour suivre l'index de l'attaque sélectionnée
selected_attack_index = 0
# Définis une variable pour gérer le clignotement
show_selected_attack = True
start_flash_time = pygame.time.get_ticks()


# Fonction pour choisir une attaque aléatoire pour le Pokémon adverse
def choisir_attaque_adverse(attaques_disponibles1):
    return random.choice(list(attaques_disponibles1.values()))
###############################################################################################################################
# Fonction indispensable dans le programme
jeu = JeuPokemon()
##############################################################################################################
#                                    Fonctions de dégats
##############################################################################################################
def dammage1():
    ###################################################################################
    # 							Adversaire
    ###################################################################################
    # Enregistre les dégâts infligés par l'attaque adverse
    degats_adversaire = jeu.degats(premier_pokemon,premier_pokemon1)
    # Soustrait les dégâts des PV actuels du Pokémon adverse
    premier_pokemon1["stats"]["HP"] -= degats_adversaire
    # stock le résultat dans la variable pv1
    pv1 = premier_pokemon1["stats"]["HP"]
    return pv1

def dammagee():
    ###################################################################################
    # 							Joueur
    ###################################################################################
    # Enregistre les dégâts infligés par l'attaque adverse
    degats_joueur = jeu.degats(premier_pokemon1,premier_pokemon)
    # Soustrais les dégâts des PV actuels du Pokémon adverse
    premier_pokemon["stats"]["HP"] -= degats_joueur
    #stocke le résultat dans la variable pv
    pv=  premier_pokemon["stats"]["HP"]
    return pv

# Boucle principale
running = True
while running:
    current_time = pygame.time.get_ticks() #gère le temps
    elapsed_flash_time = current_time - start_flash_time # gère le cignotement
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False # si la croix est cliquer sortir de la fenêtre
        elif event.type == KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                running = False # si la touche "échape" est presser sortir de la fenêtre
            elif event.key == pygame.K_RETURN:
                # La touche "Entrer" est pressée, déclenche l'affichage de l'attaque
                attack_triggered = True
            elif event.key == K_RSHIFT:
                # La touche "shift droit" (maj droite) est pressée, met fin a l'attaque
                attack_triggered = False
                ########################################################
                #					 Adversaire							
                ########################################################
                pv1=dammage1()
                jeu.switchPokemon1(pv1)
                with open(fichier_switch1, 'r') as file: # lis et convertis les lignes lu dans le fichier_switch1 en int
                    switch_result1 = int(file.read().strip())
                ########################################################
                #						Joueur							
                ########################################################
                pv = dammagee()
                jeu.switchPokemon(pv)
                with open(fichier_switch, 'r') as file: # Idem que pour adversaire mais avec le fichier_switch
                    switch_result = int(file.read().strip())
                if switch_result==2: # si le résultat lu dans le fichier_switch est 2 dans ce cas on change de pokémon
                    # Ouvre le fichier en mode lecture
                    with open(fichier_equipe_pokemon, 'r') as fichier:
                        # Lit les 6 premières lignes
                        noms_pokemon_choisis = fichier.readlines()[-6:]
                    if noms_pokemon_choisis is not None:
                        # Affichez le premier Pokémon de la liste
                        premier_pokemon = None
                        for pokemon in pokedex_pokemon:
                            # .strip() = supprimer les espaces inutiles se trouvant au allentour des mots
                            if pokemon["name"] == noms_pokemon_choisis[0].strip():
                                premier_pokemon = pokemon
                                # Stocke les attaques disponibles pour ce Pokémon
                                attaques_disponibles = pokemon["attack"]
                                

                        if premier_pokemon is not None:
                            # Affichez l'image du 1er pokémon joueur
                            f1.blit(premier_pokemon["image"], (10, 500))
                            premier_pokemon["stats"]["HP"]= premier_pokemon["stats"]["HP_reference"]
                            # Position du texte des PV et réinitialisation des pv du pokémon
                            pv_text = font.render(f"PV: {premier_pokemon['stats']['HP']}", True, (255, 255, 255))
                            position_pv = (10, 450)
                            f1.blit(pv_text, position_pv)
                    else:
                        print("Erreur : Pokémon non trouvé dans le Pokédex")
                elif switch_result ==3: # si le résultat lu dans le fichier_switch est 3 arrêter la boucle
                    running=False
                ########################################################
                #					Adversaire							                        
                ########################################################
                if switch_result1==2: # si le résultat lu dans le fichier_switch1 est 2 dans ce cas on change de pokémon
                    with open(fichier_equipe_pokemon2, 'r') as fichier:
                        # Lit les 6 premières lignes
                        noms_pokemon_choisis2 = fichier.readlines()[-6:]
                    if noms_pokemon_choisis2:
                        # Affichez le premier Pokémon de la liste
                        premier_pokemon2 = None
                        for pokemon2 in pokedex_pokemon1:
                            if pokemon2["name"] == noms_pokemon_choisis2[0].strip():
                                premier_pokemon2 = pokemon2
                                attaques_disponibles2 = pokemon2["attack"]

                        if premier_pokemon2 is not None:
                            # Affichez l'image du 1er Pokémon adverse
                            f1.blit(premier_pokemon2["image"], (400, 300))
                            premier_pokemon2["stats"]["HP"]= premier_pokemon2["stats"]["HP_reference"]
                            pv_text1 = font.render(f"PV: {premier_pokemon2['stats']['HP']}", True, (255, 255, 255))
                            # Position du texte des pv
                            position_pv1 = (400, 150)
                            f1.blit(pv_text1, position_pv1)

                    else:
                        print("Erreur : Pokémon non trouvé dans le Pokédex")
                elif switch_result1 ==3: # si le résultat lu dans le fichier_switch1 est 3 dans ce cas arrêter la boucle
                    running=False

                
        if event.type == MOUSEBUTTONDOWN:
            #permet de naviguer entre les attaques
            if event.button == 4:  # Molette vers le haut
                selected_attack_index = (selected_attack_index - 1) % len(attaques_disponibles)
            elif event.button == 5:  # Molette vers le bas
                selected_attack_index = (selected_attack_index + 1) % len(attaques_disponibles)

    f1.blit(combat4, (0, 0))# affiche le fond 
    
    ########################################################################################
    # 								Joueur													
    ########################################################################################
    # Vérifie qu'il y ai au mons 1 pokémon choisi
    if noms_pokemon_choisis:
        # Affichez le premier Pokémon de la liste
        premier_pokemon = None
        for pokemon in pokedex_pokemon:
            if pokemon["name"] == noms_pokemon_choisis[0].strip():
                premier_pokemon = pokemon
                # Stocke les attaques disponibles pour ce Pokémon
                attaques_disponibles = pokemon["attack"]

        if premier_pokemon is not None:
            # Affichez l'image du 1er pokémon joueur
            f1.blit(premier_pokemon["image"], (10, 500))
            # Position du texte des PV
            position_pv = (10, 450)
        else:
            print("Erreur : Pokémon non trouvé dans le Pokédex")
    # Rafraîchir l'interface graphique avec les nouveaux PV
    pv_text = font.render(f"PV: {premier_pokemon['stats']['HP']}", True, (255, 255, 255))
    f1.blit(pv_text, position_pv)
    ########################################################################################
    #								Adversaire												
    ########################################################################################
    # Idem que au dessus mais pour l'adversaire
    if noms_pokemon_choisis2:
        # Affichez le premier Pokémon de la liste
        premier_pokemon1 = None
        for pokemon1 in pokedex_pokemon1:
            if pokemon1["name"] == noms_pokemon_choisis2[0].strip():
                premier_pokemon1 = pokemon1
                attaques_disponibles1 = pokemon1["attack"]

        if premier_pokemon1 is not None:
            # Affichez l'image du 1er Pokémon adverse
            f1.blit(premier_pokemon1["image"], (400, 300))
            # Position du texte des PV
            position_pv1 = (400, 150)

        else:
            print("Erreur : Pokémon non trouvé dans le Pokédex")

    # Rafraîchir l'interface graphique avec les nouveaux PV
    pv_text1 = font.render(f"PV: {premier_pokemon1['stats']['HP']}", True, (255, 255, 255))
    f1.blit(pv_text1, position_pv1)
    
    if attack_triggered == True:
    ########################################################################################
    #								Adversaire												
    ########################################################################################
        if noms_pokemon_choisis2:
            # Choix aléatoire de l'attaque pour le Pokémon adverse
            attaque_adverse = choisir_attaque_adverse(attaques_disponibles1)
            #a garder de côter pour une pottentielle amélioration de projets
            #with open(fichier_attaque_selectionnee1, 'w') as file:
                #file.write(attaque_adverse)
        f1.blit(attack, (400, f1_height - 110))
    ########################################################################################
    # 								Joueur													
    ########################################################################################
        # Clignotement de l'attaque sélectionnée
        if elapsed_flash_time < 500:  # Clignote pendant 500 ms
            show_selected_attack = True
        elif 500 <= elapsed_flash_time < 1000:  # Masque pendant 500 ms
            show_selected_attack = False
        else:  # Réinitialise le temps après 1000 ms
            start_flash_time = pygame.time.get_ticks()

        # Affichez l'attaque sélectionnée avec le clignotement
        if show_selected_attack:
            selected_attack = list(attaques_disponibles.values())[selected_attack_index]
            selected_attack_text = font1.render(f"Choix: {selected_attack}", True, (0, 0, 0))
            f1.blit(selected_attack_text, (425, f1_height - 75))
        

    pygame.display.flip()

pygame.quit() #quitte la fenêtre pygame