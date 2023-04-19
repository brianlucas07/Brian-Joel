import pandas as pd

nomes = input("Digite seu nome: ")
idade = input ("Digite sua idade: ")

coluna = {
    'nome': [nomes],
    'idade':[idade]
}

tabela = pd.DataFrame(coluna)
print(tabela)

for i in range(0,2):

    ad = input("Digite o nome para ser adicionado: ")
    id = input("Digite sua idade: ")
    tabela = tabela.append({'nome':ad, 'idade':id},ignore_index=True)
    print(tabela)
    
with open("Tabela.txt", 'w') as f:
    tabela1 = tabela.to_string(header=True, index=False)
    f.write(tabela1)



def simbolo(arq):
    dicionario = {}
    with open("Tabela.txt") as f:
     texto = f.read().replace("\t", " ") # terminada a leitura faz as substituições
     for i in range(len(texto.split("\n")) - 1) :
        dicionario.setdefault(texto.split("\n")[i],texto.split("\n")[i+1])
    return dicionario

dicionario = simbolo("Tabela.txt")
print(dicionario)

df = pd.read_table(
    'Tabela.txt', header=0)
print(df)

nn = "Davi"
dd = "5"

df1 = df.append({"nome":nn, "idade":dd}, ignore_index=True)
print(df1)
         
