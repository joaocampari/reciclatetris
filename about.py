import pygame as _pygame
import json
import os
import menu as _menu

class About(object):

    def showAbout(screen):
        about_sprite = _pygame.image.load(os.path.join("sprites","about.jpg"))
        myfont = _pygame.font.SysFont("Myriad Pro", 30)

        while True:
            index = 0
            screen.blit(about_sprite, (0,0))
            labels = ['Senhor lixão está jogando lixo na rua, precisamos ajudar', 'o Grupo RRR na reciclagem desses resíduos é importante eles sejam ',
                    'colocados em seu devido lugar. Em busca de um mundo limpo', 'e reciclado. Reduzir, reutilizar e reciclar',
                    'são os alicerces de uma sociedade limpa.']
            for i in labels:
                index += 1
                label = myfont.render(i, 1, (255,255,0))      
                screen.blit(label, (170, 100 + (index * 40)))
            _pygame.display.flip()
            for event in _pygame.event.get():
                    
                if event.type == _pygame.QUIT:
                    _pygame.quit()
                if event.type == _pygame.KEYDOWN:
                    if event.key == _pygame.K_ESCAPE:
                        _menu.Menu.showMenu(screen)


