import pygame

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre de l'application
largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Gestion des HID (Clavier)")

# Couleurs
ROSE = (255, 192, 203)
NOIR = (0, 0, 0)

# Police de caractères
police = pygame.font.Font(None, 36)

# Boucle principale
en_cours = True
while en_cours:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.KEYDOWN:
            touche = pygame.key.name(event.key)
            print("Touche enfoncée :", touche)

    # Rafraîchissement de l'écran
    fenetre.fill(ROSE)
    pygame.display.flip()

# Terminaison de l'application
pygame.quit()