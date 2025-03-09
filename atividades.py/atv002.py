import os

mensagens = []
nome = input("Nome: ")

while True:
    # Limpar terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
            print("________________________________")

    # Ler o texto da nova mensagem
    texto = input("Mensagem: ")
    if texto == "fim":
        break

    # Adicionar mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
