import pygame as _pygame
from pygame import mixer
import os
import trash
import trashtype
import trashcan
import random
import feedback

# Classe do jogo
class Game(object):
    # Iniciando pygame
    _pygame.init()
    _pygame.display.set_caption("Reciclatetris")

    # Variaveis globais
    global tc_plastic
    global tc_glass
    global tc_metal
    global tc_paper
    global t_actual
    global monster_pos
    global hitwrong

    # Inicia lixeiras
    def initTrashCans():
        global tc_plastic 
        global tc_glass
        global tc_metal
        global tc_paper

        tc_plastic = trashcan.TrashCan("PET", trashtype.TrashType.PLASTIC, (5,385))
        tc_glass = trashcan.TrashCan("VIDRAÇA", trashtype.TrashType.GLASS, (220,385))
        tc_metal = trashcan.TrashCan("METALLICA", trashtype.TrashType.METAL, (480,385))
        tc_paper = trashcan.TrashCan("PAPÉLITO", trashtype.TrashType.PAPER, (715,385))

    # Blita lixeiras
    def blitTrashCans(screen):
        tc_plastic.blitTrash(screen)
        tc_glass.blitTrash(screen)
        tc_metal.blitTrash(screen)
        tc_paper.blitTrash(screen)

    # Lança novo lixo
    def throwTrashNew(screen, pos):
        global t_actual
        t_actual = trash.Trash("trash", random.choice(list(trashtype.TrashType)), pos)
        t_actual.throwTrash(screen, pos)

    # Lança lixo existente (util para mudar posição a cada clock)
    def throwTrash(screen, pos):
        global t_actual
        t_actual = trash.Trash("trash", t_actual.trash_type, pos)
        t_actual.throwTrash(screen, pos)

    # Variavel 'main' da classe, inicia o jogo
    def showGame(screen):
        # Seta global
        global monster_pos
        global hitwrong

        # Seta clock
        Game.setClock()

        # Inicializa timer
        start_ticks = _pygame.time.get_ticks() #starter tick

        # Inicia musica
        Game.playTetrisMusic()
        # Inicializa lixos
        Game.initTrashCans()

        # Inicia Imagens
        home_sprite = _pygame.image.load(os.path.join("sprites","bg_game.jpg"))
        monster_sprite = _pygame.image.load(os.path.join("sprites","monster.png"))
        
        # Lança primeiro lixo apenas para popular variavel global
        Game.throwTrashNew(screen, (100, 20))

        # Variavel auxiliar para movimentar o senhor lixão
        aux = 5

        # Variavel auxiliar para detectar posição x do senhor lixão
        monsterx = 10

        while True:
            seconds = (_pygame.time.get_ticks() - start_ticks) / 1000
            if seconds > 20:
                Game.stopMusic()
                feedback.Feedback.showFeedback(screen, Game.getTrashList())

            # Movimenta senhor lixão no eixo x
            if monsterx >= 780:
                monsterx = 700
                aux = -8
            elif monsterx <= 9:
                monsterx = 10
                aux = 8
            
            monsterx = monsterx + aux

            # Blita fundo e senhor lixão
            screen.blit(home_sprite, (0,0))      
            screen.blit(monster_sprite, (monsterx, 0))  

            # Blita lata de lixos
            Game.blitTrashCans(screen)
            monster_pos = monsterx

            # Atual posição
            x,y = t_actual.pos

            
            for event in _pygame.event.get():

                if event.type == _pygame.QUIT:
                    _pygame.quit()
                if event.type == _pygame.KEYDOWN:  
                    if event.key == _pygame.K_RIGHT:
                        if x < 987 and x > 950:
                            x = 10
                        else:
                            x = x + 30
                    elif event.key == _pygame.K_LEFT:
                        if x > 0 and x < 30 :
                            x = 900
                        else:
                            x = x - 30
                        
                            
            # Incrementa +1
            Game.throwTrash(screen, (x, y+1))

            # Verifica lixeiras
            Game.checkCollide(screen, tc_plastic)
            Game.checkCollide(screen, tc_metal)
            Game.checkCollide(screen, tc_paper)
            Game.checkCollide(screen, tc_glass)

            _pygame.display.flip()

    def getTrashList():
        trash_list = []
        trash_list.append(tc_plastic)
        trash_list.append(tc_metal)
        trash_list.append(tc_paper)
        trash_list.append(tc_glass)
        return trash_list

    # Verifica colisão entre o lixo e lixeira
    def checkCollide(screen, trashcan_o):
        x,y = t_actual.pos
        if (trashcan_o.verifyCollide(t_actual) == True or  trashcan_o.verifyCollide(t_actual) == False) or y >= 600:
            global monster_pos
            Game.throwTrashNew(screen, (monster_pos + 30, 20))

    # Define o clock do jogo
    def setClock():
        clock = _pygame.time.Clock()
        clock.tick(400)
    
    # Define musica que toca
    def playTetrisMusic():
        mixer.init()
        mixer.music.load("tetris.mp3")
        mixer.music.play(-1)

    def stopMusic():
        mixer.music.stop()



