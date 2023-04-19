import pandas as pd

nomes = input("Digite seu nome: ")
idade = input ("Digite sua idade: ")

coluna = {
    'nome': [nomes],
    'idade':[idade]
}

tabela = pd.DataFrame(coluna)
print(tabela)
ad = input("Digite o nome para ser adicionado: ")
id = input("Digite sua idade: ")
tabela = tabela.append({'nome':ad, 'idade':id},ignore_index=True)
print(tabela)

nm = input("Alterar idade do Brian: ")
tabela.loc[1,'idade'] = nm
print(tabela)

nd = int(input("Qual linha ser deletada? "))
tabela = tabela.drop(tabela.index[nd])

print(tabela)