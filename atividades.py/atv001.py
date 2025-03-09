
nota1 = float(input("Digite a nota do primeiro aluno: "))
nota2 = float(input("Digite a nota do segundo aluno: "))
nota3 = float(input("Digite a nota do terceiro aluno: "))


media = (nota1 + nota2 + nota3) / 3


maior_nota = max(nota1, nota2, nota3)
if maior_nota == nota1:
    aluno_maior_nota = print("primeiro aluno tirou a nota maior")
elif maior_nota == nota2:
    aluno_maior_nota = print("segundo aluno tirou a nota maior")
else:
    aluno_maior_nota = print ("terceiro aluno tirou a nota maior")


media_resultado = "maior ou igual a 7" if media >= 7 else "menor que 7"

print(f"Média: {media:.2f} | Maior nota: {maior_nota} | Média geral: {media_resultado}")
# 'media' é exibida com 2 casas decimais, graças ao '.2f'.
# 'maior_nota' insere a maior nota encontrada entre as entradas.
# 'media_resultado' exibe o texto associado ao resultado da média geral.
# O caractere '|' é usado para separar visualmente as informações na saída.