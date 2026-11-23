import json
import pygame

def carregar_perguntas(caminho="data/perguntas.json"):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def calcular_resultado(perguntas, respostas_usuario):
    acertos = 0
    erros = 0
    for pergunta, resposta in zip(perguntas, respostas_usuario):
        if resposta == pergunta["correta"]:
            acertos += 1
        else:
            erros += 1
    return acertos, erros

def verificar_aprovacao(erros, limite_erros=3):
    return erros < limite_erros

def iniciar_estado_quiz(perguntas):
    return {
        "perguntas": perguntas,
        "respostas": [None] * len(perguntas),  
        "pergunta_atual": 0,
        "acertos": 0,
        "erros": 0,
        "mostrar_dica": False,
        "tempo_transicao": None,             
        "finalizado": False
    }

def processar_eventos_quiz(evento, estado, botao_ia):
    if estado["finalizado"]:
        return

    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if botao_ia.collidepoint(evento.pos):
            estado["mostrar_dica"] = not estado["mostrar_dica"]

    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_LEFT and estado["pergunta_atual"] > 0:
            estado["pergunta_atual"] -= 1
            estado["tempo_transicao"] = None   
            estado["mostrar_dica"] = False

        elif evento.key == pygame.K_RIGHT and estado["pergunta_atual"] < len(estado["perguntas"]) - 1:
            estado["pergunta_atual"] += 1
            estado["tempo_transicao"] = None
            estado["mostrar_dica"] = False

        elif evento.key == pygame.K_RETURN and None not in estado["respostas"]:
            acertos, erros = calcular_resultado(estado["perguntas"], estado["respostas"])
            estado["acertos"] = acertos
            estado["erros"] = erros
            estado["finalizado"] = True

        teclas_opcoes = {
            pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3, pygame.K_4: 4, pygame.K_5: 5
        }
        if evento.key in teclas_opcoes:
            estado["respostas"][estado["pergunta_atual"]] = teclas_opcoes[evento.key]
            if estado["pergunta_atual"] < len(estado["perguntas"]) - 1:
                estado["tempo_transicao"] = pygame.time.get_ticks()


def atualizar_transicao(estado):
    if estado["tempo_transicao"] is not None:
        agora = pygame.time.get_ticks()
        if agora - estado["tempo_transicao"] >= 800:
            estado["perguna_atual"] += 1
            estado["tempo_transicao"] = None
            estado["mostrar_dica"] = False

def desenhar_quiz(tela, fonte, estado, botao_ia):
    tela.fill((25, 28, 36))

    if estado["finalizado"]:
        aprovado = verificar_aprovacao(estado["erros"])
        texto_fim = f"APROVADO! ({estado['acertos']} acertos, {estado['erros']} erros)" if aprovado else f"REPROVADO! ({estado['erros']} erros)"
        cor = (80, 220, 100) if aprovado else (220, 80, 80)
        tela.blit(fonte.render(texto_fim, True, cor), (220, 250))
        return

    indice = estado["pergunta_atual"]
    pergunta = estado["perguntas"][indice]
    resposta_marcada = estado["respostas"][indice]

    # Placar no topo
    respondidas = sum(1 for r in estado["respostas"] if r is not None)
    hud = f"Questao {indice + 1}/{len(estado['perguntas'])} | Respondidas: {respondidas}/{len(estado['perguntas'])}"
    tela.blit(fonte.render(hud, True, (200, 200, 200)), (30, 20))

    # Enunciado
    tela.blit(fonte.render(pergunta["enunciado"], True, (255, 255, 255)), (30, 80))

    # Alternativas e o X na opção que estiver salva na lista
    for i, texto_alt in enumerate(pergunta["alternativas"], start=1):
        marcador = "[X] " if resposta_marcada == i else "[ ] "
        cor_alt = (255, 220, 100) if resposta_marcada == i else (220, 220, 220)
        tela.blit(fonte.render(marcador + texto_alt, True, cor_alt), (40, 150 + i * 45))

    # Botão da IA e Hover "Dica"
    pygame.draw.rect(tela, (60, 130, 230), botao_ia, border_radius=8)
    tela.blit(fonte.render("IA", True, (255, 255, 255)), (botao_ia.x + 15, botao_ia.y + 10))
    if botao_ia.collidepoint(pygame.mouse.get_pos()):
        tela.blit(fonte.render("Dica", True, (150, 220, 255)), (botao_ia.x, botao_ia.y - 30))

    if estado["mostrar_dica"]:
        tela.blit(fonte.render(pergunta["dica_ia"], True, (120, 255, 200)), (30, 440))

    # Rodapé com os controles
    instrucao = "Setas <- ->: Navegar | 1-5: Marcar"
    if None not in estado["respostas"]:
        instrucao += " | ENTER: Entregar Prova!"
    tela.blit(fonte.render(instrucao, True, (160, 160, 180)), (30, 505))