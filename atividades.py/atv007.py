try:
    numero = int(input("Digite um número: "))
    
    while numero < 0:
        print("Digite um número positivo.")
        numero = int(input("Digite um número: "))

   
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}.")

except ValueError:
    print("Por favor, digite um número inteiro válido.")