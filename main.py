import pygame
from pygame.locals import *
import time
import random



class Labirinto():

    def __init__(self, formato):
        self.formato = formato

    # Atualizando o print(labirinto) para imprimir o labirinto 2x2 ao invés do enderço de memória do objeto
    def __str__(self):
        tamanho_coluna = len(self.formato)
        for x in range(0, tamanho_coluna):
            for y in range(0, tamanho_coluna):
                print(str(self.formato[x][y]) + " ", end="")
            print("")
        return ""

    def verifica_vizinhos(self, posL, posC):

        # 3 4 5
        # 2 X 6
        # 1 8 7

        vizinhos = []

        # 1
        try:
            if(self.formato[posL+1][posC - 1] == -1):
                vizinhos.append(1)
        except:
            pass

        # 2
        try:
            if (self.formato[posL][posC - 1] == -1):
                vizinhos.append(2)
        except:
            pass

        # 3
        try:
            if (self.formato[posL - 1][posC - 1] == -1):
                vizinhos.append(3)
        except:
            pass

        try:
            # 4
            if (self.formato[posL - 1][posC] == -1):
                vizinhos.append(4)
        except:
            pass

        try:
            # 5
            if (self.formato[posL - 1][posC + 1] == -1):
                vizinhos.append(5)
        except:
            pass

        try:
            # 6
            if (self.formato[posL][posC + 1] == -1):
                vizinhos.append(6)
        except:
            pass

        try:
            # 7
            if (self.formato[posL + 1][posC + 1] == -1):
                vizinhos.append(7)
        except:
            pass

        try:
            # 8
            if (self.formato[posL + 1][posC] == -1):
                vizinhos.append(8)
        except:
            pass

        if(self.formato[posL][posC] == 10):
            self.formato[posL][posC] = len(vizinhos) + 10

        return vizinhos

    def set_valor(self, mapa, linha, coluna, valor):
        mapa[linha][coluna] = valor

    def verifica_fronteira(self, fronteira, x, y):
        try:
            return fronteira.index((x, y)) != -1
        except:
            return False

def mostrar_valor(x,y):
    try:
        valor = str(labirinto.formato[x][y] - 10)
        pygame.draw.rect(surface, gray, pygame.Rect(y * 50, x * 50, 50, 50))
        img = font.render(valor, True, black)
        surface.blit(img, (y * 50 + 14.5, x * 50 + 12.5))
    except:
        pass
zeros = []
visitados = []

def verifica_se_zero(x,y):
    try:
        if(labirinto.formato[x][y + 1] == 10 and not labirinto.verifica_fronteira(zeros, x, y + 1)):
            if x >= 0 and y+1 >= 0:
                zeros.append((x, y + 1))
        if (labirinto.formato[x][y - 1] == 10 and not labirinto.verifica_fronteira(zeros, x, y - 1)) and labirinto.formato[x][y - 1] != -1:
            if x >= 0 and y-1 >= 0:
                zeros.append((x, y - 1))
        if (labirinto.formato[x + 1][y] == 10 and not labirinto.verifica_fronteira(zeros, x + 1, y) and labirinto.formato[x + 1][y] != -1):
            if x + 1 >= 0 and y >= 0:
                zeros.append((x + 1, y))
        if (labirinto.formato[x - 1][y] == 10 and not labirinto.verifica_fronteira(zeros, x - 1, y) and labirinto.formato[x - 1][y] != -1):
            if x - 1 >= 0 and y >= 0:
                zeros.append((x - 1, y))
        if (labirinto.formato[x + 1][y + 1] == 10 and not labirinto.verifica_fronteira(zeros, x + 1, y + 1) and labirinto.formato[x + 1][y + 1] != -1):
            if x + 1 >= 0 and y + 1>= 0:
                zeros.append((x + 1, y + 1))
        if (labirinto.formato[x - 1][y + 1] == 10 and not labirinto.verifica_fronteira(zeros, x - 1, y + 1) and labirinto.formato[x - 1][y + 1] != -1):
            if x - 1>= 0 and y + 1 >= 0:
                zeros.append((x - 1, y + 1))
        if (labirinto.formato[x + 1][y - 1] == 10 and not labirinto.verifica_fronteira(zeros, x + 1, y - 1) and labirinto.formato[x + 1][y - 1] != -1):
            if x + 1 >= 0 and y - 1 >= 0:
                zeros.append((x + 1, y - 1))
        if (labirinto.formato[x - 1][y - 1] == 10 and not labirinto.verifica_fronteira(zeros, x - 1, y - 1) and labirinto.formato[x - 1][y - 1] != -1):
            if x - 1 >= 0 and y - 1 >= 0:
                zeros.append((x - 1, y - 1))


    except:
        pass


# Celula Livre
cl = 10
# Bomba
bb = 10

# Exemplo de labirinto 1
labirinto1 = [[cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl],
              [cl, bb, bb, cl, bb, cl],
              [cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl]]

# Exemplo de labirinto 2
labirinto2 = [[cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl],
              [cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl, cl]]

labirinto = Labirinto(labirinto2)


tamanho_coluna = len(labirinto.formato)

for x in range(0, tamanho_coluna):
    for y in range(0, tamanho_coluna):
        valor = random.randrange(0,11,1)
        if valor == 0:
            bomba = -1
            labirinto.set_valor(labirinto2, x, y, bomba)
        else:
            pass

for x in range(0, tamanho_coluna):
    for y in range(0, tamanho_coluna):
        labirinto.verifica_vizinhos(x, y)

print(labirinto)

# Booleano para o while do labirinto
jogo = True

# Inicializando tela no pygame
tamanho_coluna = len(labirinto.formato)
vertical = 50 * tamanho_coluna
horizontal = 50 * tamanho_coluna
metade_celula = horizontal/24
surface = pygame.display.set_mode((horizontal, vertical))
tamanho_quadrado_coluna = int(horizontal / tamanho_coluna)
tamanho_quadrado_linha = int(vertical / tamanho_coluna)
print(tamanho_quadrado_linha)
contador = 0

# Inicializando cor
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

for x in range(tamanho_coluna):
    for y in range(tamanho_coluna):
        pygame.draw.rect(surface, green, pygame.Rect(y * 50, x * 50, 50, 50))

fronteira = []

pygame.init()




while jogo:

    #print(labirinto.verifica_vizinhos(4,1))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


    sysfont = pygame.font.get_default_font()
    t0 = time.time()
    font = pygame.font.SysFont(None, 48)

    img = font.render("10", True, blue)


    # Desenhando labirinto
    for x in range(tamanho_coluna):
        for y in range(tamanho_coluna):
            pygame.draw.rect(surface, black, pygame.Rect(y * 50, x * 50, 50, 50), 1)
            contador += 50

    if pygame.mouse.get_pressed()[0]:
        linha = int(pygame.mouse.get_pos()[1] / 50)
        coluna = int(pygame.mouse.get_pos()[0] / 50)

                        #if labirinto.formato[x][y] == 10 and not labirinto.verifica_fronteira(fronteira, x, y):
                        #    fronteira.append((x, y))
                        #    ultimo_fronteira = fronteira.pop()
                        #    linha_fronteira = ultimo_fronteira[0]
                        #    coluna_fronteira = ultimo_fronteira[1]
                        #    print(linha_fronteira, coluna_fronteira)
