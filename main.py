import random, sys, copy, os, pygame
from pygame.locals import *
from config import *

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

    #inicialização do pygame e setup basico das variaveis globais
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    pygame.display.set_caption('StarPusher')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    

    #dicionario global que vai ter todos os objetos surface retornado por pygame.image.load()
    IMAGESDICT = {'uncovered goal': pygame.display.load('./assets/RedSelector.png'),
                'covered goal': pygame.image.load('Selector.'),
                'star': pygame.image.load('./assets/Star.png'),
                'corner': pygame.image.load('./assets/Wall_Block_Tall.png'),
                'wall': pygame.image.load('./assets/Wood_Block_Tall.png'),
                'inside': pygame.image.load('./assets/Plain_Block.png'),
                'outside floor': pygame.image.load('./assets/Grass_Block'),
                'title': pygame.image.load('./assets/star_title.png'),
                'princess': pygame.image.load('./assets/princess.png'),
                'boy': pygame.image.load('./assets/boy.png'),
                'catgirl': pygame.image.load('./assets/catgirl.png'),
                'horngirl': pygame.image.load('./assets/horngirl.png'),
                'pinkgirl': pygame.image.load('./assets/pinkgirl'),
                'rock': pygame.image.load('./assets/Rock.png'),
                'short tree': pygame.image.load('./assets/Tree_Short.png'),
                'tall tree': pygame.image.load('./assets/Tree_Tall.png'),
                'ugly tree': pygame.image.load('Tree_Ugly.png')}
    

    # esses valores sao globais, e mapeiam o personagem que aparece
    TILEMAPPING = {'x': IMAGESDICT['corner'],
                   '#': IMAGESDICT['wall'],
                   'o': IMAGESDICT['inside Floor'],
                   ' ': IMAGESDICT['outside floor']}
    
    OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
                        '2': IMAGESDICT['short tree'],
                        '3': IMAGESDICT['tall tree'],
                        '4': IMAGESDICT['ugly tree']}
    
    #player images é todas as possibilidades de personagem que o jogador pode ser
    #current image é a imagem atual do jogador
    currentImage = 0
    PLAYERIMAGES = [IMAGESDICT['princess'],
                    IMAGESDICT['boy'],
                    IMAGESDICT['catgirl'],
                    IMAGESDICT['horngirl'],
                    IMAGESDICT['pnkgirl']]
    
    startScreen() #mostra o titulo da tela antes do jogador presionar a tecla

    #ler os niveis pelo arquivo txt, veja readLevelFile() para mais detalhes
    #veja o formato desse arquivo e como fazer seus proprios niveis

    levels = readLevelFile('starPusherLevels.txt')
    curentLevelIndex = 0

    #loop principal, esse loop roda um unico nivel,
    #quando o jogador termina o nivel o proximo nivel é carregado

    while True:
        result = runLevel(levels, currentLevelIndex)

        if result in ('solved', 'next'):
            #vai para o proximo nivel
            currentLevelIndex += 1
            if currentLevelIndex >= len(levels):
                #se naot iver mais niveis volta para o primeiro
                currentLevelIndex = 0
            elif result == 'back':
                #vai para o nivel anterior
                currentLevelIndex -= 1
                if currentLevelIndex < 0:
                    #se nao tiver um nivel anterior vai para o ultimo
                    currentLevelIndex = len(levels)-1
            elif result == 'reset':
                pass #nao faz nada, da um recall no loop runLevel() para resetar o nivel

    
def runLevel(levels, levelNum):
    global currentImage
    levelObj = levels[levelNum]
    mapObj = decorateMap(levelObj['mapObj'],
                         levelObj['startState']['player'])
    gameStateObj = copy.deepcopy(levelObj['startState'])

    


