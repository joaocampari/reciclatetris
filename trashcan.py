import pygame as pygame
import os
import trashtype

# Classe de Lixeiras
class TrashCan(object):
    def __init__(self, name, trash_type, pos):
        self.name = name
        self.trash_type = trash_type
        self.pos = pos
        self.sprite = getSpriteLocation(trash_type)
        self.hit = 0
        self.hitwrong = 0

    # Blita a lixeira
    def blitTrash(self, screen):
        screen.blit(self.sprite, self.pos)
    
    # Incrementa atributo hit
    def hitSuccess(self):
        self.hit = self.hit + 1
    
    # Incrementa atributo hit wrong
    def hitWrong(self):
        self.hitwrong = self.hitwrong + 1

    # Verifica colisão entre lixo e lixeira
    # Valida tipo da lixeira compativel com lixo e eixos x e y
    def verifyCollide(self, trash):
        xc, yc = self.pos
        xt, yt = trash.pos
        isCollided = ((xt >= xc) and (xt <= xc + 200)) and ((yt >= yc-40) and (yt <= yc+140))
        if isCollided and trash.trash_type == self.trash_type:
            self.hitSuccess()
            print("{} Lixeira, sucesso do lixo {}".format(self.trash_type, trash.trash_type))
            return True
        elif isCollided and trash.trash_type != self.trash_type:
            self.hitWrong()
            print("{} Lixeira, tentou colocar objeto  do tipo {}".format(self.trash_type, trash.trash_type))
            return False
        
# Retorna a imagem criada de acordo com o tipo de lixeira
def getSpriteLocation(trash_type):
    if trash_type == trashtype.TrashType.GLASS:
        return loadImage("glass")
    elif trash_type == trashtype.TrashType.METAL:
        return loadImage("metal")
    elif trash_type == trashtype.TrashType.PAPER:
        return loadImage("paper")
    elif trash_type == trashtype.TrashType.PLASTIC:
        return loadImage("plastic")

# Carrega o objeto de imagem
def loadImage(name):
    return pygame.image.load(os.path.join("sprites", name + ".png"))


        