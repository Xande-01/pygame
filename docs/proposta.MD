# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Informe o nome provisório do jogo.

**Nome:**

> Um Dia de Estudante

## 2. Integrantes do grupo

- Nome 1: Alexandre Martins
- Nome 2: Antônio Cardoso
- Nome 3: Gabriel Costa
- Nome 4: Rodrigo 

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

> IA na educação e confiabilidade de sistemas inteligentes.

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> O jogo aborda como estudantes de tecnologia devem utilizar ferramentas de Inteligência Artificial como apoio ao aprendizado de programação, destacando o perigo de confiar cegamente em respostas geradas por IA e a importância do estudo e da revisão humana. Na prática, o tema define o desafio principal: o jogador precisa absorver boas práticas de uso ético e verificação de erros durante os diálogos na aula para conseguir responder corretamente aos dilemas práticos do Quiz no laboratório e ser aprovado.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Exploração 2D / Novela Visual interativa com sistema de Perguntas e Respostas (Quiz).

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> O jogo acompanha a rotina de um estudante calouro do primeiro período de Engenharia de Software durante um dia de aula na faculdade, focado na disciplina de Introdução a Algoritmos e no uso responsável de IA. Na tela em visão 2D, o jogador controla o estudante pela sala, interage com colegas de turma e assiste às explicações do professor Laerte. Após absorver o conteúdo, o estudante segue para a aula de laboratório, onde encontra o desafio de realizar uma avaliação prática (Quiz) sobre o uso ético, seguro e eficiente de IA na resolução de problemas.

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> Concluir o dia letivo interagindo com o professor Laerte e com os colegas para absorver os conceitos da aula, chegando ao laboratório preparado para realizar o teste final e alcançar a pontuação mínima necessária para ser aprovado sem dificuldades.

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

- Regra 1: O jogador deve caminhar pela sala de aula e conversar obrigatoriamente com o professor Laerte e com os colegas para destravar o acesso à avaliação do laboratório.
- Regra 2: Durante as conversas na sala de aula, o professor e os colegas fornecem dicas sobre boas práticas de IA que servirão de base para responder às questões da prova.
- Regra 3: No laboratório, o jogador enfrenta uma bateria de perguntas de múltipla escolha (alternativas de A a E) simulando dilemas reais do uso de IA nos estudos e na programação.
- Regra 4: Cada resposta incorreta contabiliza uma falha na avaliação; o jogador deve manter o número de erros abaixo do limite máximo permitido (menos de 3 erros) para não reprovar.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> Responder corretamente à quantidade mínima exigida de questões no teste prático do laboratório, encerrando a aula e o dia letivo com aprovação.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> Atingir o limite máximo de 3 respostas erradas durante o teste prático do laboratório, resultando na reprovação ("bomba") do estudante na atividade.

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal:** Estudante calouro (controlado pelo jogador), além dos sprites dos colegas e do professor Laerte em cenários 2D.
- **Obstáculos ou desafios:** Tela de avaliação para o Quiz/Prova com opções de múltipla escolha simulando uma folha de caderno ou computador do laboratório.
- **Itens ou objetos de interação (se houver):** Colegas de turma, professor Laerte, cadeiras/mesas, portas de transição e a prova do laboratório.
- **Pontuação, vidas, tempo ou progresso:** Contabilização de acertos e erros no quiz e controle de progresso das conversas obrigatórias concluídas.

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

> - **W, A, S, D:** Movimentação do personagem pelo cenário (sala de aula e laboratório).
> - **E:** Interagir com personagens (professor Laerte e colegas), objetos do cenário e avançar caixas de diálogo.
> - **1, 2, 3, 4, 5:** Selecionar as alternativas correspondentes (A, B, C, D ou E) durante o teste de múltipla escolha.

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: Sincronização da transição entre o modo de movimentação livre e o modo de caixa de diálogo.
- Dificuldade 2: Posicionamento preciso das colisões com objetos e NPCs no cenário.
- Dificuldade 3: Troca de cena para a tela do Quiz de forma natural e agradável na janela do Pygame.

## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> Movimentação básica em tela única ou transição simples entre sala e laboratório, interação por caixa de texto com o professor e execução completa do quiz com tela final indicando aprovação ou reprovação.

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: Adição de efeitos sonoros, trilha de fundo e animações de caminhada.
- Melhoria 2: Refinamento visual dos gráficos e sprites, deixando os personagens e cenários mais detalhados.
- Melhoria 3: Adição de ações extras como correr pelo cenário, somadas a novas animações e menu inicial.

## 15. Organização inicial do código, recursos e originalidade

- **Organização inicial do código:** Estrutura modular em Python utilizando Pygame para gerenciamento de estados de tela (exploração, diálogo e quiz) e estruturas de listas/dicionários para armazenar falas, perguntas e gabaritos.
- **Recursos previstos:** Biblioteca Pygame, imagens em pixel art 2D para sprites/cenários e fontes de texto padrão para a interface.
- **Declaração de originalidade:** Declaramos que a proposta e o desenvolvimento deste projeto são de autoria própria dos integrantes do grupo, respeitando as diretrizes acadêmicas da disciplina.
