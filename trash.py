
import pygame as pygame
import os
import trashtype

class Trash(object):
      def __init__(self, name, trash_type, pos):
         self.name = name
         self.trash_type = trash_type
         self.sprite = getSpriteLocation(trash_type)
         self.pos = pos

      # Blita na tela o lixo
      def blitTrash(self, screen, pos):
         self.pos = pos
         screen.blit(self.sprite, pos)

      # Blita na tela o lixo
      def throwTrash(self, screen, pos):
        self.blitTrash(screen, pos)

# Retorna a imagem criada de acordo com o tipo de lixo
def getSpriteLocation(trash_type):
   if trash_type == trashtype.TrashType.GLASS:
      return loadImage("trash_glass")
   elif trash_type == trashtype.TrashType.METAL:
      return loadImage("trash_metal")
   elif trash_type == trashtype.TrashType.PAPER:
      return loadImage("trash_paper")
   elif trash_type == trashtype.TrashType.PLASTIC:
      return loadImage("trash_plastic")

# Carrega o objeto de imagem
def loadImage(name):
   return pygame.image.load(os.path.join("sprites", name + ".png"))

       
