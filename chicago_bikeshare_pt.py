# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import sys
import math

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")
print("Cabeçalhos:")
cabeçalho = data_list[0]
print(cabeçalho)
input("Aperte Enter começar a avaliar o teste...")


# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
data_list = data_list[1:]
for i  in range(20):
    print(data_list[i])
input("Aperte Enter para ir para a tarefa 2 ...")


# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i  in range(20):
    print(data_list[i][6])
input("Aperte Enter para ir para a tarefa 3...")


# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
"""
Função para pegar todos os dados de uma coluna desejada através de seu índice.
    Argumentos:
        data  : O array com os dados extraidos do csv .
        index : O indíce da coluna.
    Retorna:
        Uma lista com os valores da coluna.
"""
def column_to_list(data, index):
    column_list = [linha[index] for linha in data]
    return column_list

print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------
input("Aperte Enter para ir para a tarefa 4...")


# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
for linha in data_list:
    if linha[6] == "Male":
        male += 1
    elif linha[6] == "Female":
        female +=1
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------
input("Aperte Enter para ir para a tarefa 5...")


# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
"""
Função para contar a quantidade de genêros.
    Argumentos:
        data_list  : O array com os dados extraidos do csv .
    Retorna:
        Uma lista com os valores da quantidade de generos masculinos e femeninos.
"""
def count_gender(data):
    male = 0
    female = 0
    for linha in data:
        if linha[6] == "Male":
            male += 1
        elif linha[6] == "Female":
            female +=1       
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------
input("Aperte Enter para ir para a tarefa 6...")


# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
"""
Função para pegar o gênero mais popular.
    Argumentos:
        data_list  : O array com os dados extraidos do csv.
    Retorna:
        Uma string a resposta sobre qual é o genero mais popular.
"""
def most_popular_gender(data):
    male = 0
    female = 0
    for linha in data:
        if linha[6] == "Male":
            male += 1
        elif linha[6] == "Female":
            female +=1
    if male == female:
        return "Equal"
    elif male > female:
        return  "Male"
    else:
        return "Female"

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------
input("Aperte Enter para ir para a tarefa 7...")


# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
"""
Função para pegar os tipos de usuários para exebição em grafíco .
    Argumentos:
        data  : O  array com os dados extraidos do csv.
        types : Um array tipos de usuários.
    Retorna:
        Uma array com os valores da contagem de tipos de usuários.
"""
def user_type_graph(data,types):
    tipos = {}
    for linha in data:
        for tipo in types:
            if linha[5] == tipo:
                tipos[tipo] = tipos.get(tipo,0) + 1
            else :  
                tipos[tipo] = tipos.get(tipo,0) + 0 #Atribuindo 0 para preservar a ordem das quantidades dos tipos que são passados no eixo x  
    return tipos

print("\nTAREFA 7: Verifique o gráfico!")
user_type_list = column_to_list(data_list, -3)
types = list(dict(zip(user_type_list, user_type_list)).keys()) #Usei esse tipo de chamada pois não conhecia o set() apresendato posteriormente e apresentou um gráfico mais agradavel
quantity = user_type_graph(data_list,types)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity.values())
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por Usuários')
plt.show(block=True)
input("Aperte Enter para ir para a tarefa 8...")


# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem registros de generos vazios que não entram na contagem de generos masculinos e femininos, logo a soma das quantidades dos generos é diferente do tamanho total da lista de registros "
print("resposta:", answer)
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------
input("Aperte Enter para ir para a tarefa 9...")


# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
"""
Função para pegar a mediana da lista  .
    Argumentos:
        lista_tratada : O array com os dados extraidos do csv.
    Retorna:
        O valor da mediana em formato int .
"""
def mediana(lista_tratada):    
    lista_tratada.sort() 
    lstLen= len(lista_tratada) 
    index = lstLen // 2 
    if (lstLen % 2 == 1): 
        return lista_tratada[index] 
    else: 
        return (lista_tratada[index] + lista_tratada[index - 1]) / 2

trip_duration_list = column_to_list(data_list, 2)
#Tratando a lista para poder usar as funções de max e min (que no caso fiquei na dúvida se podia usar ou não ) 
#Usei pois percebi que dava para reduzir código evitando criar duas micro-funções  
lista_tratada = [int(valor) for valor in trip_duration_list]
min_trip = min(lista_tratada)
max_trip = max(lista_tratada)
median_trip = mediana(lista_tratada)
mean_trip = math.ceil(sum(lista_tratada) / len(trip_duration_list))
print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------
input("Aperte Enter para ir para a tarefa 10...")


# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------
input("Aperte Enter para ir para a tarefa 11...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
    Argumentos:
        param1: O primeiro parâmetro.
        param2: O segundo parâmetro.
    Retorna:
        Uma lista de valores x.
"""
input("Aperte Enter para ir para a tarefa 12...")


# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"
"""
Função para contar items para o desafio.
    Argumentos:
        column_list: Os dados da coluna do desafio.
    Retorna:
        Uma lista de listas sendo item_types os tipos de valores da coluna e count_items valores para a soma do desafio.
"""
def count_items(column_list):
    item_types = []
    count_items = []
    item_types = set(column_list)
    count_items = [1 for linha in column_list]
    return item_types, count_items
if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

print("\nTeste finalizado")
