import pygame as _pygame
import json
import os
import menu as _menu

# Classe responsavel pelo ranking
class Ranking(object):

    # Mostra o ranking
    def showRanking(screen):
        ranking_sprite = _pygame.image.load(os.path.join("sprites","ranking.jpg"))
        myfont = _pygame.font.SysFont("Myriad Pro", 30)

        while True:
            index = 0
            screen.blit(ranking_sprite, (0,0))
            for i in Ranking.buildText():
                index += 1
                label = myfont.render(i, 1, (255,255,0))      
                screen.blit(label, (190, 100 + (index * 40)))
            _pygame.display.flip()
            for event in _pygame.event.get():
                    
                if event.type == _pygame.QUIT:
                    _pygame.quit()
                if event.type == _pygame.KEYDOWN:
                    if event.key == _pygame.K_ESCAPE:
                        _menu.Menu.showMenu(screen)


    # Efetua a criação de lista de strings
    def buildText():
        rankLabel = []
        rank = Ranking.loadFile()
        for r in rank:
            rankLabel.append("{} - Acertos: {}, Erros: {}".format(r['name'], r['hit'], r['wrong']))
        return rankLabel

    # Carrega o arquivo que lista o ranking
    def loadFile():
        ranking = []
        with open('ranking.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            for p in data:
                ranking.append(p)

            sorted_list = sorted(ranking, key=lambda kv: kv['hit'])
            sorted_list.reverse()
            return sorted_list

    def write(ranking_updated):
        with open('ranking.json', 'w') as json_file:
            json.dump(ranking_updated, json_file)

