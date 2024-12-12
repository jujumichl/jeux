class JeuPokemon:
    def __init__(self):
        # Initialisation du jeu
        #Donnée des pokémons
        self.equipe_pokemon = [
            {"name": "Scovilain", "type": "Plante/Feu", "attack": {1: "Charge", 2: "Vive-Attaque", 3: "Grincement", 4: "Jet de Sable"},
             "stats": {"HP": 65, "Attack": 108, "Defense": 65, "vitesse": 75}},
            {"name": "Cotovol", "type": "Plante/Vol","attack":{1:"Rugissement", 2:"Charge", 3:"Chargeur", 4:"Ruse"},
             "stats":{"HP": 75, "Attack": 55, "Defense": 70, "vitesse": 110}},
            {"name": "Shaymin", "type": "Plante","attack": {1:"Pouvoir Lunaire", 2:"Choc Mental", 3:"Rafale Psy", 4:"Croissance"},
             "stats":{"HP": 100, "Attack": 100, "Defense": 100, "vitesse": 100}},
            {"name": "Éoko", "type": "Psy", "attack":{1:"Rayon Chargé",2: "Grincement", 3:"Chargeur", 4:"Force Poigne"},
             "stats":{"HP": 75, "Attack": 50, "Defense": 80, "vitesse": 65}},
            {"name": "Sulfura", "type": "Fée/Vol","attack":{1:"Griffe", 2: "Groz'Yeux", 3:"Mimi-Queue", 4:"Danse Flamme"},
             "stats":{"HP": 90, "Attack": 100, "Defense": 90, "vitesse": 90}},
            {"name": "Granbull", "type": "Fée", "attack":{1:"Morsure", 2:"Groz'Yeux", 3:"Chant Canon", 4:"Regard Touchant"},
             "stats":{"HP": 90, "Attack": 120, "Defense": 75, "vitesse": 45}},
            {"name": "Dracaufeu", "type": "Feu/Vol","attack":{1:"Flammeche", 2:"Rugissement", 3:"Griffe", 4:"Pistolet à O"},
             "stats":{"HP": 78, "Attack": 84, "Defense": 78, "vitesse": 100}},
            {"name": "Hyporoi", "type": "Eau/Dragon","attack":{1:"Pistolet à O", 2:"Charge", 3:"Souplesse", 4:"Coup d'Boule"},
             "stats":{"HP": 75, "Attack": 95, "Defense": 95, "vitesse": 85}},
            {"name": "Dracolosse", "type": "Drangon/Vol","attack":{1:"Lézard'O", 2:"Colère", 3:"Coud'Boue", 4:"Draco-Rage"},
             "stats":{"HP": 91, "Attack": 134, "Defense": 95, "vitesse": 80}},
            {"name": "Symbios", "type": "Psy", "attack":{1:"Griffe", 2:"Groz'Yeux", 3:"Rayon Chargé", 4:"Boul'Armure"},
             "stats":{"HP": 110, "Attack": 65, "Defense": 75, "vitesse": 30}},
            {"name": "Exagide", "type": "Acier/Spectre","attack":{1:"Tranche", 2:"Éclat Magique", 3:"Lame-Feuille", 4:"Mur Lumière"},
             "stats":{"HP": 60, "Attack": 50, "Defense": 140, "vitesse": 60}},
            {"name": "Nymphali", "type": "Fée", "attack":{1:"Jet de Sable", 2:"Vent Féérique", 3:"Séduction", 4:"Rafale Psy"},
             "stats":{"HP": 95, "Attack": 65, "Defense": 65, "vitesse": 60}},
            {"name": "Yveltal", "type": "Ténèbre/Vol","attack":{1:"Tranche", 2:"Cru-Aile", 3:"Hurlement", 4:"Vent Mauvais"},
             "stats":{"HP": 126, "Attack": 131, "Defense": 95, "vitesse": 99}},
            {"name": "Tortank", "type": "Eau", "attack":{1:"Charge", 2:"Mimi-Queue", 3:"Pistolet à O", 4:"Rugissement"},
             "stats":{"HP": 79, "Attack": 83, "Defense": 100, "vitesse": 78}},
            {"name": "Zamazenta", "type": "Combat/Acier","attack":{1:"Griffe", 2:"Groz'Yeux", 3:"Tranche", 4:"Coup d'Boule"},
             "stats":{"HP": 92, "Attack": 120, "Defense": 140, "vitesse": 128}}
        ]

    def charger_noms_pokemon(self):
        """Fonction qui récupère les noms des Pokémon situés sur la dernière ligne du bloc-notes"""
        with open("note/equipe_pokemon.txt", "r") as fichier:
            noms_pokemon = fichier.readlines()
            return [nom.strip() for nom in noms_pokemon]

    def gerer_defense(self, defenseur, degats):
        """Fonction qui gère la défense et réduit les dégâts selon la défense du Pokémon"""
        if defenseur["stats"]["Defense"]== 140:
            degats_reduit= degats*(1-50/100)
        elif defenseur["stats"]["Defense"]==65:
            degats_reduit= degats*(1-10/100)
        elif defenseur["stats"]["Defense"]== 70 or defenseur["stats"]["Defense"]== 75 or defenseur["stats"]["Defense"]== 78:
            degats_reduit= degats*(1-15/100)
        elif defenseur["stats"]["Defense"]==80:
            degats_reduit= degats*(1-20/100)
        elif defenseur["stats"]["Defense"]==95 or defenseur["stats"]["Defense"]==90:
            degats_reduit= degats*(1-25/100)
        elif defenseur["stats"]["Defense"]==100:
            degats_reduit= degats*(1-30/100)
        else:
            # Si la défense n'est pas spécifiée, pas de réduction
            degats_reduit = degats
        return degats_reduit

    def augmenter_degats(self, attaquant, degats):
        """Fonction qui augmente les dégâts en fonction du nombre de points d'attaque"""
        if attaquant["stats"]["Attack"]== 140:
            degats_augmente= degats*(1+50/100)
        elif attaquant["stats"]["Attack"]==50 or attaquant["stats"]["Attack"]==55:
            degats_augmente= degats*(1+5/100)
        elif attaquant["stats"]["Attack"]== 65:
            degats_augmente= degats*(1+10/100)
        elif attaquant["stats"]["Attack"]==83 or attaquant["stats"]["Attack"]== 84:
            degats_augmente= degats*(1+20/100)
        elif attaquant["stats"]["Attack"]==95:
            degats_augmente= degats*(1+25/100)
        elif attaquant["stats"]["Attack"]==100:
            degats_augmente= degats*(1+30/100)
        elif attaquant["stats"]["Attack"]==108:
            degats_augmente= degats*(1+35/100)
        elif attaquant["stats"]["Attack"]== 120:
            degats_augmente= degats*(1+40/100)
        elif attaquant["stats"]["Attack"]==131 or attaquant["stats"]["Attack"]==134:
            degats_augmente= degats*(1+45/100)
        return degats_augmente
    
    
    def degats(self, attaquant, defenseur):
        """ Augmente les dégâts en fonction des statistiques d'attaque de l'attaquant"""
        degats_augmentes = self.augmenter_degats(attaquant, 10)

        # Gère la défense du défenseur et réduit les dégâts
        degats_reduits = self.gerer_defense(defenseur, degats_augmentes)
        
        return round(degats_reduits)
    
    def switchPokemon(self, pv_joueur_actuels):
        """ Fonction qui permet de changer automatiquement de pokémon quand un pokémon est KO"""
        fichier_equipe_pokemon="note/equipe_pokemon.txt"
        fichier_switch = "note/switch.txt"
        # Vérifie si les PV du Pokémon sont égaux à zéro 
        if pv_joueur_actuels<=0:
            # Retire le nom du Pokémon du fichier d'équipe
            with open(fichier_equipe_pokemon, 'r') as file:
                noms_pokemon_choisis = file.readlines()[-6:]

            if noms_pokemon_choisis:
                # Supprime le nom du Pokémon de la liste
                nom_pokemon_defait = noms_pokemon_choisis.pop(0).strip()

                # Met à jour le fichier avec les noms restants
                with open(fichier_equipe_pokemon, 'w') as file:
                    file.writelines(noms_pokemon_choisis)

                print(f"Votre pokémon {nom_pokemon_defait} a été vaincu!")

                # Charge le prochain Pokémon de la liste
                if noms_pokemon_choisis:
                    # Obtient le premier Pokémon de la nouvelle liste
                    prochain_pokemon_nom = noms_pokemon_choisis[0].strip()

                    # Met à jour les attaques disponibles pour le nouveau Pokémon
                    for pokemon in self.equipe_pokemon:
                        if pokemon["name"] == prochain_pokemon_nom:
                            attaques_disponibles = pokemon["attack"]
                            break
                    switch= 2
                    with open(fichier_switch, 'w') as file:
                        file.write(str(switch))
                    print(f"Prochain Pokémon : {prochain_pokemon_nom}")
                    print ("")
                    return switch

                else:
                    print("Tous vos Pokémon ont été vaincus! GAME OVER")
                    switch=3
                    compteur=0
                    with open(fichier_switch, 'w') as file:
                        file.write(str(switch))
                    return switch
        else:
            switch=1
            with open(fichier_switch, 'w') as file:
                file.write(str(switch))
            return switch
        
    def switchPokemon1(self, pv_joueur_actuels):
        """Fonction qui change de pokémon si il ses pv sont inférieur ou égale a 0"""
        fichier_equipe_pokemon_2="note/equipe_pokemon_2.txt"
        fichier_switch1 = "note/switch1.txt"
        # Vérifie si les PV du Pokémon sont égaux à zéro 
        if pv_joueur_actuels<=0:
            # Retire le nom du Pokémon du fichier d'équipe
            with open(fichier_equipe_pokemon_2, 'r') as file:
                noms_pokemon_choisis = file.readlines()[-6:]

            if noms_pokemon_choisis:
                # Supprime le nom du Pokémon de la liste
                nom_pokemon_defait = noms_pokemon_choisis.pop(0).strip()

                # Met à jour le fichier avec les noms restants
                with open(fichier_equipe_pokemon_2, 'w') as file:
                    file.writelines(noms_pokemon_choisis)

                print(f"Le Pokémon Adverse {nom_pokemon_defait} a été vaincu!")

                # Charge le prochain Pokémon de la liste
                if noms_pokemon_choisis:
                    # Obtient le premier Pokémon de la nouvelle liste
                    prochain_pokemon_nom = noms_pokemon_choisis[0].strip()

                    # Met à jour les attaques disponibles pour le nouveau Pokémon
                    for pokemon in self.equipe_pokemon:
                        if pokemon["name"] == prochain_pokemon_nom:
                            attaques_disponibles = pokemon["attack"]
                            break
                    switch1= 2
                    with open(fichier_switch1, 'w') as file:
                        file.write(str(switch1))
                    print(f"Prochain Pokémon Adverse: {prochain_pokemon_nom}")
                    print ("")
                    return switch1
                else:
                    print("Tous les Pokémon Adverse ont été vaincus! Winner !!")
                    switch1=3
                    with open(fichier_switch1, 'w') as file:
                        file.write(str(switch1))
                    return switch1
        else:
            switch1=1
            with open(fichier_switch1, 'w') as file:
                file.write(str(switch1))
            return switch1

# optionnel:
    # creer une fonction qui permet de changer de pokémons
    # creer une fonction qui attaque en fonction de la vitesse du pokémon
    # généraliter (atq forte, atq moyenne, attq normal, atq faible)