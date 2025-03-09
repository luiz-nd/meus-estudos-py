#carro = float(input("fale a velocidade desse carro: "))

#if carro <= 220:
 #print("Esse é um carro medio ")

#elif carro >= 250:
 #print("Esse carro e rapido")

def escolher_carro():
    print("Escolha o tipo de carro:")
    tipo = input("Digite 'esportivo' ou 'luxo': ").lower()

  
    if tipo == "esportivo":
        print("Você escolheu um carro esportivo!")
        marca = input("Escolha a marca: 'Porsche' ou 'Ferrari': ").lower()
        
        if marca == "porsche":
            print("Parabéns! O Porsche é uma máquina incrível!")
        elif marca == "ferrari":
            print("Parabéns! A Ferrari é um símbolo de desempenho e luxo!")
        else:
            print("Marca não reconhecida. Tente novamente!")

   
    elif tipo == "luxo":
        print("Você escolheu um carro de luxo!")
        marca = input("Escolha a marca: 'Audi' ou 'Mercedes': ").lower()
        
        if marca == "audi":
            print("Parabéns! O Audi é sinônimo de sofisticação e inovação!")
        elif marca == "mercedes":
            print("Parabéns! A Mercedes é um ícone de luxo e performance!")
        else:
            print("Marca não reconhecida. Tente novamente!")

  
    else:
        print("Opção de tipo de carro não reconhecida. Tente novamente!")


escolher_carro()