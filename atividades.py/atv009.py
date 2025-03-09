# Importamos a biblioteca random para usar números aleatórios
#import random

# Aqui, o computador sorteia um número entre 1 e 100
#numero_secreto = random.randint(1, 100)

# Exibimos uma mensagem inicial para o jogador
#print("Bem-vindo ao jogo da adivinhação!")  # Mensagem de boas-vindas
#print("Tente adivinhar o número que estou pensando (entre 1 e 100).")  # Explicando o objetivo

# Inicializamos a variável que conta o número de tentativas do jogador
#tentativas = 0

# Criamos uma variável chamada 'acertou' para verificar se o jogador acertou o número
# Começa como False porque o jogador ainda não acertou
#acertou = False

# Começamos um loop que só vai terminar quando o jogador acertar o número
#while not acertou:  # Enquanto o jogador não acertar
    # Solicitamos um número ao jogador
    #chute = int(input("Digite seu palpite: "))  # Lemos o palpite do jogador e convertemos para inteiro

    # A cada tentativa, incrementamos o contador de tentativas
    #tentativas += 1

    # Verificamos se o chute do jogador é menor que o número secreto
    #if chute < numero_secreto:
        #print("Muito baixo! Tente novamente.")  # Informamos que o palpite foi muito baixo
    # Verificamos se o chute do jogador é maior que o número secreto
    #elif chute > numero_secreto:
        #print("Muito alto! Tente novamente.")  # Informamos que o palpite foi muito alto
    # Caso nenhuma das condições acima seja verdadeira, o jogador acertou
    #else:
        # Exibimos uma mensagem de parabéns e informamos o número de tentativas
        #print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        # Alteramos a variável 'acertou' para True, encerrando o loop
        #acertou = True
try:
    import random

   
    numero_secreto = random.randint(1, 100)

    print("Bem-vindo ao jogo de adivinhação!")
    print("Vamos, tente adivinhar o número que estou pensando entre (1 e 100).")

    tentativas = 0
    acertou = False

   
    while not acertou:

        chute = int(input("Digite seu palpite: "))
        tentativas += 1 

   
        if chute < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif chute > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acertou = True

except ValueError:
  
    print("Por favor, digite um número válido.")