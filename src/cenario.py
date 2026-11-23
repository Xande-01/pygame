import pygame

# Dimensões provisórias
LARGURA = 1000
ALTURA = 600

# Personagem (representado por um retângulo)
jogador = pygame.Rect(480, 450, 35, 45)
velocidade = 5

# Objetos que bloqueiam a movimentação
obstaculos = []

# Mesa do professor
obstaculos.append(pygame.Rect(420, 150, 160, 50))

# Carteiras dos alunos
for x in [180, 400, 620]:
    for y in [280, 380]:
        obstaculos.append(pygame.Rect(x, y, 100, 45))

# Área ocupada pelo professor
professor = pygame.Rect(480, 115, 35, 35)

# Controla se o diálogo está aberto
dialogo_aberto = False


def perto_do_professor():
    # Cria uma área maior ao redor do professor
    area_interacao = professor.inflate(100, 100)

    # Verifica se o jogador está próximo
    return jogador.colliderect(area_interacao)


def alternar_dialogo():
    global dialogo_aberto

    if dialogo_aberto:
        dialogo_aberto = False

    elif perto_do_professor():
        dialogo_aberto = True

def desenhar_cenario(tela):
    # Fundo da sala de aula
    tela.fill((220, 210, 190))

    # Quadro
    pygame.draw.rect(tela, (40, 100, 70), (350, 30, 300, 80))

    # Mesa do professor
    pygame.draw.rect(tela, (130, 80, 40), (420, 150, 160, 50))

    # Cadeiras dos alunos
    for x in [180, 400, 620]:
        for y in [280, 380]:
            pygame.draw.rect(tela, (160, 110, 70), (x, y, 100, 45))

    # Professor provisório
    pygame.draw.rect(tela, (200, 70, 70), (480, 115, 35, 35))



def movimentar_jogador():
    if dialogo_aberto:
        return
    teclas = pygame.key.get_pressed()

    # Guarda a posição anterior
    posicao_anterior = jogador.copy()

    # Movimentação
    if teclas[pygame.K_w]:
        jogador.y -= velocidade

    if teclas[pygame.K_s]:
        jogador.y += velocidade

    if teclas[pygame.K_a]:
        jogador.x -= velocidade

    if teclas[pygame.K_d]:
        jogador.x += velocidade

    # Limita o jogador à janela
    jogador.clamp_ip(pygame.Rect(0, 0, LARGURA, ALTURA))

    # Verifica colisão com os móveis
    for obstaculo in obstaculos:
        if jogador.colliderect(obstaculo):
            jogador.topleft = posicao_anterior.topleft
            break



def desenhar_jogador(tela):
    pygame.draw.rect(tela, (50, 100, 220), jogador)



def desenhar_interacao(tela):
    fonte = pygame.font.Font(None, 28)

    if dialogo_aberto:
        # Caixa de diálogo
        caixa = pygame.Rect(100, 430, 800, 130)

        pygame.draw.rect(tela, (30, 30, 50), caixa)
        pygame.draw.rect(tela, (255, 255, 255), caixa, 2)

        nome = fonte.render("Professor Laerte", True, (255, 200, 100))
        tela.blit(nome, (120, 445))

        texto = fonte.render(
            "A IA ajuda nos estudos, mas devemos verificar suas respostas.",
            True,
            (255, 255, 255)
        )
        tela.blit(texto, (120, 490))

        instrucao = fonte.render(
            "Pressione E para fechar",
            True,
            (180, 180, 180)
        )
        tela.blit(instrucao, (120, 525))

    elif perto_do_professor():
        mensagem = fonte.render(
            "Pressione E para conversar",
            True,
            (0, 0, 0)
        )
        tela.blit(mensagem, (380, 75))
