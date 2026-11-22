
import pygame
import sys

pygame.init()

LARGURA = 1920
ALTURA = 1080

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Um Dia de Estudante")

clock = pygame.time.Clock()

fonte = pygame.font.Font("assets/Bungee-Regular.ttf", 25)
fonte_nome = pygame.font.Font("assets/Bungee-Regular.ttf", 28)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
COR_NOME = (230, 140, 180)


dialogos = [
    {
        "nome": "Player",
        "texto": "Teste 1."
    },

    {
        "nome": "Player",
        "texto": "Teste 2."
    },

    {
        "nome": "Player",
        "texto": "Teste 3."
    },

    {
        "nome": "Player",
        "texto": "Teste 4."
    }
]


indice = 0

texto_atual = dialogos[indice]["texto"]

letras_exibidas = 0

velocidade_texto = 35

tempo_anterior = 0

dialogo_finalizado = False


caixa = pygame.Rect(
    35, 385, 890, 125
)


def desenhar_texto(texto, x, y, largura):

    palavras = texto.split(" ")

    linha = ""

    for palavra in palavras:

        teste = linha + palavra + " "

        if fonte.size(teste)[0] > largura:

            imagem = fonte.render(
                linha, True, BRANCO
            )

            tela.blit(imagem, (x, y))

            y += 32

            linha = palavra + " "

        else:
            linha = teste

    imagem = fonte.render(
        linha, True, BRANCO
    )

    tela.blit(imagem, (x, y))


def avancar_dialogo():

    global indice
    global texto_atual
    global letras_exibidas
    global dialogo_finalizado


    if letras_exibidas < len(texto_atual):

        letras_exibidas = len(texto_atual)

    else:

        indice += 1

        if indice >= len(dialogos):

            dialogo_finalizado = True

        else:

            texto_atual = dialogos[indice]["texto"]

            letras_exibidas = 0


while True:

    clock.tick(60)

    tempo_atual = pygame.time.get_ticks()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            if evento.key in (pygame.K_SPACE, pygame.K_RETURN):

                if not dialogo_finalizado:
                    avancar_dialogo()

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if evento.button == 1:

                if not dialogo_finalizado:
                    avancar_dialogo()


    if not dialogo_finalizado:

        if letras_exibidas < len(texto_atual):

            intervalo = 1000 / velocidade_texto

            if tempo_atual - tempo_anterior >= intervalo:

                letras_exibidas += 1

                tempo_anterior = tempo_atual



    if not dialogo_finalizado:

        superficie = pygame.Surface(
            (caixa.width, caixa.height),
            pygame.SRCALPHA
        )

        superficie.fill((15, 15, 25, 220))

        tela.blit(superficie, caixa.topleft)

        pygame.draw.rect(
            tela,
            BRANCO,
            caixa,
            2,
            border_radius=8
        )


        nome = dialogos[indice]["nome"]

        nome_imagem = fonte_nome.render(
            nome, True, COR_NOME
        )

        tela.blit(
            nome_imagem,
            (caixa.x + 20, caixa.y + 10)
        )

        texto_visivel = texto_atual[:letras_exibidas]

        desenhar_texto(
            texto_visivel,
            caixa.x + 20,
            caixa.y + 55,
            caixa.width - 40
        )


    
        if letras_exibidas == len(texto_atual):

            indicador = fonte.render(
                "▼", True, BRANCO
            )

            tela.blit(
                indicador,
                (caixa.right - 35, caixa.bottom - 30)
            )

    else:

        mensagem = fonte.render(
            "Acabou kk",
            True,
            BRANCO
        )

        tela.blit(
            mensagem,
            (LARGURA // 2 - 90, ALTURA // 2)
        )


    pygame.display.flip()
