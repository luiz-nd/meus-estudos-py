salario = float(input("informe seu salário:") )

if salario <= 3000:
    print ("Programador Junior")

elif salario > 3000 and  salario <= 6000:
    print ("Programador Pleno")

elif salario > 6000 and salario <= 15000:
    print ("Progaramador Senior")

else:
    print("Gerente de Projetos")