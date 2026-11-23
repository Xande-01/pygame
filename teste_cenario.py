
import pygame

from src.cenario import (
    desenhar_cenario,
    movimentar_jogador,
    desenhar_jogador,
    alternar_dialogo,
    desenhar_interacao
)

pygame.init()

tela = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Teste - Sala de Aula")

relogio = pygame.time.Clock()

def main():
    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_e:
                    alternar_dialogo()

        movimentar_jogador()

        desenhar_cenario(tela)
        desenhar_jogador(tela)
        desenhar_interacao(tela)

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()