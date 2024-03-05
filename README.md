# HID



pour la conception de notre application de gestion des HID (comme HID nous avons pris le clavier).
1.nous avons créer notre projet dans le logiciel Pycharm et par consequent le langage de programmation utilisé est Python, nous av
nous avons donc installer Pygame grace à la commande : pip install pygame

2. ensuite , nous avons importer la bibliothéque pygame avec la commande: import pygame

3.initialisation de pygame
pygame.init()
#permet d'initialiser ces sous-systèmes nécessaires à l'exécution de votre application.

4. Configuration de la fenêtre de l'application
nous avons d'abord defini la largeur et la hauteur de la fenetre
fenetre = pygame.display.set_mode((largeur, hauteur))
# cette fonction nous permet de créer la fenetre 
pygame.display.set_caption("Gestion des HID (Clavier)")
# cette fonction defini le nom de la fenetre
Ensuite , on defini les couleurs de la fenetre 
et la police avec la fonction 
police = pygame.font.Font(None, 36)

5.À chaque itération de la boucle principale, nous gérons les événements en utilisant la fonction
pygame.event.get()
pygame.QUIT 
#est un événement qui se produit lorsque l'utilisateur clique sur le bouton de fermeture de la fenêtre
pygame.KEYDOWN 
#est un événement qui se produit lorsqu'une touche du clavier est enfoncée
pygame.key.name(event.key)
#permet de recuperer le nom de la touche enfoncée

pygame.display.flip()
# toutes les couleurs, police defini sur la surface fenetre sera visible à l'ecran 