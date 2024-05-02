from random import randint
import time
#armazena enunciados, alternativas, e respostas corretas das questões
banco_questoes = [
    {
        'pergunta': 'Qual nome do Lucas?',
        'alternativas': ['A) Lucas', 'B) Caio', 'C) Miguel', 'D) Gabriel'],
        'correta': 'A'
    },
    {
        'pergunta': 'Qual número é maior 2^23, 4^13, 8^8, 2^25?',
        'alternativas': ['A) 2^23', 'B) 4^13', 'C) 8^8', 'D) 2^25'],
        'correta': 'B'
    },
    {
        'pergunta': 'Quem escreveu a obra "Dom Quixote"?',
        'alternativas': ['A) William Shakespeare', 'B) Miguel de Cervantes', 'C) Dante Alighieri', 'D) Machado de Assis'],
        'correta': 'B'
    },
    {
        'pergunta': 'Qual é o maior planeta do sistema solar?',
        'alternativas': ['A) Terra', 'B) Vênus', 'C) Júpiter', 'D) Saturno'],
        'correta': 'C'
    },
    {
        'pergunta': 'Qual é o maior oceano do mundo?',
        'alternativas': ['A) Oceano Atlântico', 'B) Oceano Índico', 'C) Oceano Pacífico', 'D) Oceano Ártico'],
        'correta': 'C'
    },
    {
        'pergunta': 'Quem pintou a Mona Lisa?',
        'alternativas': ['A) Leonardo da Vinci', 'B) Michelangelo', 'C) Pablo Picasso', 'D) Vincent van Gogh'],
        'correta': 'A'
    },
    {
        'pergunta': 'Qual é a capital da França?',
        'alternativas': ['A) Berlim', 'B) Londres', 'C) Paris', 'D) Roma'],
        'correta': 'C'
    },
    {
        'pergunta': 'Quem foi o primeiro homem a pisar na Lua?',
        'alternativas': ['A) Neil Armstrong', 'B) Buzz Aldrin', 'C) Yuri Gagarin', 'D) Alan Shepard'],
        'correta': 'A'
    },
    {
        'pergunta': 'Qual é a capital do Canadá?',
        'alternativas': ['A) Toronto', 'B) Ottawa', 'C) Montreal', 'D) Vancouver'],
        'correta': 'B'
    },
    {
        'pergunta': 'Qual é o símbolo químico do ouro?',
        'alternativas': ['A) Au', 'B) Ag', 'C) Fe', 'D) Cu'],
        'correta': 'A'
    },
    {
        'pergunta': 'Quem escreveu "Romeu e Julieta"?',
        'alternativas': ['A) William Shakespeare', 'B) Charles Dickens', 'C) Jane Austen', 'D) Oscar Wilde'],
        'correta': 'A'
    },
    {
        'pergunta': 'Qual é o maior deserto do mundo?',
        'alternativas': ['A) Deserto do Saara', 'B) Deserto de Atacama', 'C) Deserto do Gobi', 'D) Deserto da Arábia'],
        'correta': 'A'
    },
    {
        'pergunta': 'Quem foi o primeiro presidente do Brasil?',
        'alternativas': ['A) Dom Pedro II', 'B) Getúlio Vargas', 'C) José Sarney', 'D) Marechal Deodoro da Fonseca'],
        'correta': 'D'
    },
    {
    'pergunta': 'Quem foi o líder do movimento pela independência do Brasil em 1822?',
    'alternativas': ['A) Dom Pedro II', 'B) Dom João VI', 'C) José Bonifácio', 'D) Tiradentes'],
    'correta': 'C'
    },
    {
    'pergunta': 'Quem foi a primeira mulher a ganhar um Prêmio Nobel?',
    'alternativas': ['A) Marie Curie', 'B) Rosalind Franklin', 'C) Ada Lovelace', 'D) Dorothy Hodgkin'],
    'correta': 'A'
    }
]
#armazena indices de questões já utilizadas
indice_questoes_anteriores = []  

def encontrarIndiceNovaPergunta():
    """
        Encontra um índice de uma pergunta não feita

    Returns:
        int: retorna índice da pergunta encontrada, se ja tiver achado 15 perguntas retorna -1
    """    
    while True:
        indice_questao_atual = randint(0,14)
        if not indice_questao_atual in indice_questoes_anteriores:
            indice_questoes_anteriores.append(indice_questao_atual) 
            return indice_questao_atual
        if len(indice_questoes_anteriores) == 15:
            return -1

def exibirPerguntaEAlternativas(indice_nova_pergunta):
    """
       exibe perguntas e alternativas

    Args:
        indice_nova_pergunta (int): indice de uma pergunta 
    """    
    print(banco_questoes[indice_nova_pergunta]['pergunta'])
    #para formatar exibição das alternativas
    for alternativa in range(4):
        print(banco_questoes[indice_nova_pergunta]['alternativas'][alternativa])

def obterRespDaPergunta(indice_nova_pergunta):
    """
    Obtem resposta do usuário 

    Args:
        indice_nova_pergunta (int): indice de uma pergunta não feita

    Returns:
        string: retorna uma string, ja validada, representando a alternativa
    """    
    while True:
        try:
            resp = input('\nResposta: ').upper().strip()
            if isRespValid(resp):
                return resp
            print('Informe uma opção válida!')
            animacaoCarregamento()
            exibirPerguntaEAlternativas(indice_nova_pergunta)
        except Exception as ex:
            print(ex, '\n')
            animacaoCarregamento()
            exibirPerguntaEAlternativas(indice_nova_pergunta)

def isRespValid(resp):
    """
    Verifica se a resposta do usuário é valida

    Args:
        resp (string): resposta do usuário

    Returns:
        booleam: retorna True se for resp válida e False se for inválida
    """    
    alternativas_validas = ['A', 'B', 'C', 'D']
    if resp in alternativas_validas:
        return True
    return False

def animacaoCarregamento(acao = None ):
    """Simula um carregamento adicionando 5 pontinhos de 0.3 em 0.3 segundos
    """    
    for i in range(5):  # Define a quantidade de pontos
        print('Carregando',acao, '.' * i, end='\r')  # Imprime os pontos
        time.sleep(0.3)

def verificar_resposta(indice_nova_pergunta, resp):
    """
       Destina-se a verificar se a resposta do usuário é certa ou não

    Args:
        indice_nova_pergunta (int): indice da pergunta feita
        resp (int): resposta que usuário deu a pergunta

    Returns:
        bool: true se resposta certa, false se não
    """    
    resposta_correta = banco_questoes[indice_nova_pergunta]['correta']
    if resposta_correta == resp:
        print('Acertou!!!')
        animacaoCarregamento('nova pergunta')
        return True
    print('Errou!!!')
    animacaoCarregamento('nova pergunta')
    return False
    
def atualizarPontuacao(resp_eh_correta, pontuacao_por_rodada, pontuacao_geral):
    """
       Destina-se a atualizar a pontuação do usuário

    Args:
        resp_eh_correta (bool): true se correto, false se nao
        pontuacao (int): pontuação de cada rodada
        pontuacao_geral (int): pontuação de todas as rodadas

    Returns:
        _type_: _description_
    """    
    if resp_eh_correta:
        return pontuacao_por_rodada+1, pontuacao_geral+(pontuacao_por_rodada+1)
    return pontuacao_por_rodada, pontuacao_geral

def passarDeNivelIsOk(pontuacao_por_rodada, nivel, pontuacao_geral):
    """
       Destina-se a verificar se o usuário esta apto para ir para o próximo nível

    Args:
        pontuacao_por_rodada (int): pontuação de cada rodada
        nivel (int): nível que o usuario se encontra no jogo
        pontuacao_geral (int): pontação do usuário em todo o jogo

    Returns:
        bool: se esta apto true, senao, false
    """    
    if  pontuacao_por_rodada == 5:
        print(f'Parabéns, passou para o nível {nivel+1}')
        return True
    print(f'Infelizmente você perdeu, parou no nível {nivel} e fez {pontuacao_geral} pontos')
    return False   
    
def imprimirMensagemGanhador(pontuacao_geral):
    """
        Destina-se a imprimir mensagem se usuario zerar o jogo

    Args:
        pontuacao_geral (int): pontuaçao geral do usuario no jogo
    """    
    print(f'Parabens por ter zerado nosso jogo! Sua pontuação foi de {pontuacao_geral}')

def zerouOjogo(nivel, pontuacao_geral, pontuacao_por_rodada):
    """
        Destina-se a verificar se o usuario zerou o jogo

    Args:
        nivel (int): nivel atual do usuario no jogo
        pontuacao_geral (_type_): pontuação de toda as rodadas somadas
        pontuacao_por_rodada (_type_): pontuação de cada rodada

    Returns:
        bool: true se ganhou, false se perdeu
    """    
    if nivel == 3 and pontuacao_por_rodada == 5:
        imprimirMensagemGanhador(pontuacao_geral)
        return True
    return False

def main():
    """
       Destina-se a chamar funções para que o programa funcione
    """     
    nivel = 1
    pontuacao_geral = 0
    questoes_respondidas = 0
    pontuacao_por_rodada = 0
    while True:
        indice_nova_pergunta = encontrarIndiceNovaPergunta()
        exibirPerguntaEAlternativas(indice_nova_pergunta)
        resp = obterRespDaPergunta(indice_nova_pergunta)
        questoes_respondidas += 1
        resp_eh_correta = verificar_resposta(indice_nova_pergunta, resp)
        pontuacao_por_rodada, pontuacao_geral = atualizarPontuacao(resp_eh_correta, pontuacao_por_rodada, pontuacao_geral)
        if nivel == 3 and questoes_respondidas == 5:
            if zerouOjogo(nivel, questoes_respondidas, pontuacao_por_rodada):
                break
        if questoes_respondidas == 5:
            if passarDeNivelIsOk(pontuacao_por_rodada, nivel, pontuacao_geral):
                questoes_respondidas = 0
                pontuacao_por_rodada=0
                nivel+=1  
                continue
            break

main()