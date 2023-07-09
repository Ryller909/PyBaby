import os 


#Tela de escolha de roupas

a1 = "="*40
a2 = "="*15

def roupas():

    os.system('clear')
    
    print(a1)
    print(a2,' Roupas ',a2)
    print(a1)
    print()

    print('Escolha o que deseja fazer: ')
    print('\t1 - Adicionar roupa')
    print('\t2 - Remover roupa')
    print('\t3 - Ver estoque de roupas')

    # print('\t1 - Calções')
    # print('\t2 - Camisas')
    # print('\t3 - Fraldas de pano')
    # print('\t4 - Luvas')
    # print('\t5 - Meias')
    # print('\t6 - Toucas')

    print()
    print(a1)

    esc = input('Selecione o que deseja: ')
    return esc

esc = roupas()



def adicionarRoupa():
    
    roupas = []
    
    id = int(input("Digite  código da roupa: "))
    marca = input("Marca da roupa: ")
    idade = int(input("Faixa etaria: "))
    valor = float(input("Valor da roupa: "))
    tipo = input("Tipo da roupa: ")
    tamanho = input("Tamanho da roupa: ")

    roupa = {
        'id': id,
        'marca': marca,
        'iadade': idade,
        'valor': valor,
        'tipo': tipo,
        'tamanho': tamanho
    }
    
    #roupas.append(roupa)

    
    with open("dados.dat", "a") as arquivo:
        arquivo.write(f"{roupa['id']},{roupa['marca']},{roupa['idade']},{roupa['valor']},{roupa['tipo']},{roupa['tamanho']}\n")

    print("Roupa adicionada com sucesso!! ")


def removerRoupas():

    id = input("Digite o código da roupa que deseja remover: ")

    for roupa in roupas:
        if roupa["id"] == id:
            roupas.remove(roupa)
            print("Roupa removido!!")
            return
    print("Roupa não encontrado!!")

removerRoupas(roupas)
