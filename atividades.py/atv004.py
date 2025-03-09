# Coleta de números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Cálculo da média
media = (numero1 + numero2 + numero3) / 3

# Identificação do maior número
maior_numero = max(numero1, numero2, numero3)

if maior_numero == numero1:
    print("O maior número é o primeiro.")
elif maior_numero == numero2:
    print("O maior número é o segundo.")
else:
    print("O maior número é o terceiro.")

# Verificação da média
media_resultado = "Maior ou igual a 7" if media >= 7 else "Menor que 7"
print(f"A média é {media:.2f} e é {media_resultado}.")

