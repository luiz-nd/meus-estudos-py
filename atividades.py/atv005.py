#numero = int(input("Digite um numero :"))

#if numero % 2 == 0:
 #print("Esse numero é par")

#else:
 #print("Esse numero é impar ")

try:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")