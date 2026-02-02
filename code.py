import random

cores_possiveis = ['R', 'G', 'B', 'Y', 'O', 'P']
#vai definir quantas cores a senha vai ter
tamanho_senha = 4
#gera a senha secreta e garante que cada cor será unica.
senha_secreta = random.sample(cores_possiveis, tamanho_senha)


print('Bem vindo ao jogo SENHA')
print(f'Eu gerei uma senha secreta com {tamanho_senha} cores diferentes.')
print('As cores sao R, G, B, Y, O, P. Você tem 10 tentativas para advinhar.')
print('Digite sua tentativa com 4 letras separadas por espaço (ex: R G B Y).')
print("-" * 50) 

#Define a quantidade de tentativas do jogador
tentativas_restantes = 10
#Controla se o jogador acertou a senha secreta
acertou = False

# O loop em while continuará enquanto o jogador tiver tentativas e nao tiver acertado a senha
while tentativas_restantes > 0 and not acertou:
    print(f"\nVocê tem {tentativas_restantes} tentativa(s).")
    
    tentativa = input("Digite sua tentativa. ex: R G B Y: ")
    
    # .upper() -> Converte tudo para maiúsculo (R g b y -> R G B Y)
    # .split() -> Separa o texto pelos espaços em uma lista (['R', 'G', 'B', 'Y'])
    palpite_jogador = tentativa.upper().split()

    #Contadores do palpite
    cores_posicao_certa = 0
    cores_posicao_errada = 0
    
    for cor_secreta, cor_palpite in zip(senha_secreta, palpite_jogador):
        if cor_secreta == cor_palpite:
            cores_posicao_certa += 1
            
    
    cores_em_comum = set(senha_secreta) & set(palpite_jogador)
    total_cores_certas = len(cores_em_comum)
    
    #O número de cores na posição errada é o total de cores certas menos aquelas que já contamos por estarem na posição certa.
    cores_posicao_errada = total_cores_certas - cores_posicao_certa
   
    print(f"Dica: Você acertou {cores_posicao_certa} cor(es) na posição certa.")
    print(f"Dica: Você acertou {cores_posicao_errada} cor(es) na posição errada.")
    
    #Verifica se o jogador venceu.
    if cores_posicao_certa == tamanho_senha:
        print("\nParabéns! Você adivinhou a senha secreta!")
        acertou = True #Nessa condicao, agr é true porque vai deixar de ser False pq o jogador acertou
        break 

    #Como ainda estamos no loop em While, a cada erro, o jogador perde uma chance de tentativa
    tentativas_restantes -= 1


#Isso aqui acontecerá se o jogador esgotar suas tentativas.
if not acertou:
    print("\nQue pena! Suas tentativas acabaram.")
    #'join' é um método de string que junta os elementos de uma lista.
    print(f"A senha secreta era: {' '.join(senha_secreta)}")
  
