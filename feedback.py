import pygame as _pygame
import json
import os
import menu as _menu
import ranking as _ranking
import pygame_textinput

# Classe responsavel pelo feedback
class Feedback(object):

    # Mostra o ranking
    def showFeedback(screen, trash_list):
        feedback_sprite = _pygame.image.load(os.path.join("sprites","feedback.jpg"))
        textinput = pygame_textinput.TextInput()
        myfont = _pygame.font.SysFont("Myriad Pro", 30)
        clock = _pygame.time.Clock()
        while True:
            screen.blit(feedback_sprite, (0,0))
            events = _pygame.event.get()
            textinput.update(events)
            screen.blit(textinput.get_surface(), (250, 500))

            Feedback.buildText(trash_list, screen, myfont)

            # Atualiza
            _pygame.display.update()
            clock.tick(0)

            for event in _pygame.event.get():
                if event.type == _pygame.QUIT:
                    _pygame.quit()
                if event.type == _pygame.KEYDOWN:
                    if event.key == _pygame.K_ESCAPE or event.key == _pygame.K_RETURN:
                        Feedback.updateRanking(textinput.input_string, Feedback.getTotalHits(trash_list), Feedback.getWrongHits(trash_list))
                        _ranking.Ranking.showRanking(screen)

    def getTotalHits(trash_list):
        total = 0
        for t in trash_list:
            total += t.hit
        return total

    def getWrongHits(trash_list):
        total = 0
        for t in trash_list:
            total += t.hitwrong
        return total

    # Efetua a criação de lista de strings
    def buildText(trash_list, screen, myfont):
        trash_label = []
        for t in trash_list:
            trash_label.append("Lixeira: {}, Acertos: {}, Erros: {}".format(t.name, t.hit, t.hitwrong))
        index = 0
        for i in trash_label:
            index += 1
            label = myfont.render(i, 1, (255,255,0))      
            screen.blit(label, (190, 100 + (index * 40)))

    def updateRanking(name, totalHits, totalWrong):
        ranking_list = _ranking.Ranking.loadFile()
        ranking_list.append({'name': name, 'hit': totalHits, 'wrong': totalWrong})
        _ranking.Ranking.write(ranking_list)
