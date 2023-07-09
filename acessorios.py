import os 


#Tela de esolha de acessórios

a1 = "="*40
a2 = "="*15

def acessorios():
  
    os.system('clear')
  
    print(a1)
    print(a2,' Cadastrar Acessórios ',a2)
    print(a1)
    print()
    
    print('Escolha o que deseja fazer : ')
    print('\t1 - Adicionar acessório')
    print('\t2 - Remover acessório')
    print('\t3 - Ver estoque de acessórios')

    # print('\t1 - Brinquedo')
    # print('\t2 - Chupeta')
    # print('\t3 - Escova de cabelo')
    # print('\t4 - Escova de desntes')
    # print('\t6 - Fraldas descartáveis')
    # print('\t7 - Mamadeira')

    print()
    print(a1)

    esc = input('Selecione o  que deseja: ')
    return esc  

esc = acessorios()


def adicionarAcessorio():
    
    acessorios = []
    
    id = int(input("Digite o código do acessório: "))
    nome = input("Nome do acessório: ")
    marca = input("Digite a marca do acessório: ")
    idade = int(input("Faixa etaria: "))
    valor = float(input("Valor do acessórios: "))
    tipo = input("Tipo do acessório: ")

    acessorio = {
        'id' : id,
        'nome': nome,
        'marca': marca,
        'idade': idade,
        'valor': valor,
        'tipo': tipo
    }
    
    #acessorios.append(acessorio)

    
    with open("dados.dat", "a") as arquivo:
        arquivo.write(f"{acessorio['id']},{acessorio['nome']},{acessorio['marca']},{acessorio['idade']},{acessorio['valor']},{acessorio['tipo']}\n")

    print("Acessório adicionado com sucesso!!")



    
def removerAcessorios():

    id = input("Digite o código do acessório que deseja remover: ")

    for acessorio in acessorios:
        if acessorio["id"] == id:
            acessorios.remove(acessorio)
            print("Acessório removido!!")
            return
    print("Acessório não encontrado!!")

removerAcessorios(acessorios)
