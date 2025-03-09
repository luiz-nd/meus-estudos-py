try:
    
    nota1 = float(input("Digite um número de 0 a 10: "))
  
    while nota1 < 0 or nota1 > 10:
        print("Número inválido! Digite um número entre 0 e 10.")
        nota1 = float(input("Digite novamente a primeira nota: "))
    
    nota2 = float(input("Digite um número de 0 a 10: "))
    

    while nota2 < 0 or nota2 > 10:
        print("Número inválido! Digite um número entre 0 e 10.")
        nota2 = float(input("Digite novamente a segunda nota: "))
    
    nota3 = float(input("Digite um número de 0 a 10: "))
    

    while nota3 < 0 or nota3 > 10:
        print("Número inválido! Digite um número entre 0 e 10.")
        nota3 = float(input("Digite novamente a terceira nota: "))
    
    media = (nota1 + nota2 + nota3) / 3 

   
    if media >= 7:
        print("Classificação: Aprovado")
    elif 5 <= media <= 6.9:
        print("Classificação: Recuperação")
    else:
        print("Classificação: Reprovado")
    
    print(f"Média: {media:.2f}")

except ValueError:
    print("Por favor, digite um número válido.")

    # while nota1 < 0 or nota1 > 10:
    #     print("numero invalido! digite um numero entre 0 e 10.")
    #     nota1 = float(input("digite novamente a primeira nota:"))

    # while nota2 < 0 or nota2 > 10:
    #     print("numero invalido! digite um numero entre 0 e 10.")
    #     nota2 = float(input("digite novamente a segunda nota:"))
    