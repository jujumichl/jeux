import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN
#initialise pygame
pygame.init()
#créer une fenêtre qui fais 700 pixels par 800 pixels
largeur, hauteur = 700, 800
f1 = pygame.display.set_mode((largeur, hauteur))
# la nomme Dokémon
pygame.display.set_caption("Dokémon")
f1_width, f1_height = pygame.display.get_surface().get_size() #récupère les dimensions de l'écran
sizy = largeur, hauteur #crée une variable sizy
# charge et redimentionne l'image de fond a la taille de la variable sizy
titre = pygame.transform.scale(pygame.image.load("image/ecran_de_titre/ecranTitre.png"), sizy)
#charge le son et le joue en boucle
pygame.mixer.music.load("image/ecran_de_titre/ecranTitre.mp3")
pygame.mixer.music.play(-1)
# varible pour faire fonctionner la boucle principale
running = True
# taille et police de l'écriture
font = pygame.font.Font(None, 62)
# variable servant a faire clignoter le texte
clignotement = True
temps_clignotement = 500  # Temps de clignotement en millisecondes

clock = pygame.time.Clock()
# Boucle principale
while running:
    #gère les évenement de pygame (ex: si on ferme la fenêtre arreter la boucle)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # si on fait un click ou qu'on appuie sur une touche quelconque la fenêtre se ferme
        elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            running = False
    # affiche l'image de fond en x=0 et y=0
    f1.blit(titre, (0, 0))
    # fonction qui permet de faire clignoter le texte
    maintenant = pygame.time.get_ticks()
    if maintenant % (2 * temps_clignotement) < temps_clignotement:
        input_text_render = font.render("Appuyer pour commencer", True, (0,0,180))
        f1.blit(input_text_render, (150, f1_height - 150))

    pygame.display.flip()
    clock.tick(60)
# quitte le programme
pygame.quit()