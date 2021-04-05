from Functions import func

alfabeto = []
n = int(input("Informe quantos caracteres tem o alfabeto: "))

for _ in range(n):
    palavra = input("Insira {0} caractere ao alfabeto: ".format(_ + 1))
    alfabeto.append(palavra)

k = int(input("informe quantos caracteres cada palavra deve conter: "))

Qcomb = func.QtdCombinacoes(n, k)

print('{0} combinações possiveis.'.format(Qcomb))
if (Qcomb>1000):
    print('A quantidade de combinações é muito alto, '
          '\npara evitar um elevado consumo de moemoria a '
          '\naplicação sera encerrada')
    exit()
else:
    comand = input('Deseja mostrar todas as combinações possiveis S/N: ')
    print('====================================================================')
    permsList = list(func.produto(alfabeto,k ,Qcomb))

    if str.upper(comand)==str.upper('s'):
        func.ImprimirPalavras(permsList)
    else:
        x = int(input('Informe qauntas palavras a serem exibidas: '))
        func.ImprimirPalavras(permsList[:x])
