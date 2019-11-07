import pygame as _pygame
import os
import game as _game
import ranking as _ranking
import about as _about

# Classe responsavel pelo menu
class Menu(object):
    _pygame.init()
    _pygame.display.set_caption("Reciclatetris")

    # Movimenta seta de escolha (menu)
    def getArrowPosition(pos):
        if pos == 0:
            return (165, 58)
        elif pos == 1:
            return (165, 150)
        elif pos == 2:
            return (165, 220)

    # Mostra o menu
    def showMenu(screen):
        home_sprite = _pygame.image.load(os.path.join("sprites","home.jpg"))
        arrow = _pygame.image.load(os.path.join("sprites","arrow.png"))
        arrow_position = 0
      
        while True:
            screen.blit(home_sprite, (0,0))      
            for event in _pygame.event.get():
                
                if event.type == _pygame.QUIT:
                    _pygame.quit()
                if event.type == _pygame.KEYDOWN:
                    if event.key == _pygame.K_UP:
                        if arrow_position == 0:
                            arrow_position = 2
                        elif arrow_position <= 2 and arrow_position != 0:
                            arrow_position -= 1

                    if event.key == _pygame.K_DOWN:
                        if arrow_position == 2:
                            arrow_position = 0
                        elif arrow_position >= 0 and arrow_position != 2:
                            arrow_position += 1
                    
                    if event.key == _pygame.K_RETURN:
                        Menu.navigateTo(arrow_position, screen)

            screen.blit(arrow, Menu.getArrowPosition(arrow_position))
            _pygame.display.flip()

    # Faz a navegação entre classes de acorda com a posição da seta
    def navigateTo(arrow_position, screen):
        if arrow_position == 0:
            _game.Game.showGame(screen);
        if arrow_position == 1:
            _ranking.Ranking.showRanking(screen)
        if arrow_position == 2:
            _about.About.showAbout(screen)

