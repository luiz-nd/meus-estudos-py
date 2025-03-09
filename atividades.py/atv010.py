
while True:
    try:
        print("Bem-vindo à Calculadora!")
        print("Operações disponíveis:")
        print("  +  -> Adição")
        print("  -  -> Subtração")
        print("  *  -> Multiplicação")
        print("  /  -> Divisão")

       
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        
        
        operacoes = input("Escolha a operação (+, -, *, /): ")

       
        if operacoes == "+":
            resultado = num1 + num2
        elif operacoes == "-":
            resultado = num1 - num2
        elif operacoes == "*":
            resultado = num1 * num2
        elif operacoes == "/":
            if num2 != 0:
                resultado = num1 / num2
                resultado = round(resultado, 3)  
            else:
                resultado = "Erro: Divisão por zero não é permitida."
        else:
            resultado = "Erro: Operação inválida."
        
        print(f"Resultado: {resultado}")

    except ValueError:
        print("Por favor, digite um número válido.")
    continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if continuar != 's':
        print("Obrigado por usar a calculadora. Até mais!")
        break 


    

