import os 
import pickle


#Tela de escolha de móveis

moveis = {}

try:
    arqMoveis =  open("moveis.dat", "rb")
    moveis = pickle.load(arqMoveis)
    arqMoveis.close()
except:
    arqMoveis = open("moveis.dat", "wb")
    arqMoveis.close()

def atualizarArquivo():
    arqMoveis = open("moveis.dat", "wb")
    pickle.dump(moveis,arqMoveis)
    arqMoveis.close()



a1 = "="*40
a2 = "="*15

def moveis():

    os.system('clear')

    print(a1)
    print(a2,' Móveis ',a2)
    print(a1)
    print()

    print('Escolha o que deseja fazer: ')
    print('\t1 - Adicicionar móvel')
    print('\t2 - Remover móvel')
    print('\t3 - Ver estoque de móveis')
    #print('\t4 - Redinha')
    #print('\t4 - ')
    #print('\t5 - ')

    print()
    print(a1)

    esc = input('Selecione o  que deseja: ')
    return esc

esc = moveis()



def adicionarMoveis():
    
    moveis = []
    
    id = int(input("Digite o codigo do móvel: "))
    marca = input("Marca do móvel: ")
    valor = float(input("Preço do móvel: "))
    tipo = input("Tipo do móvel: ")
    material = input("Matérial do móvel: ")

    movel = {
        'id': id,
        'marca': marca,
        'valor': valor,
        'tipo': tipo,
        'material': material
    }
    
    #moveis.append(movel)

    
    with open("dados.dat", "a") as arquivo:
        arquivo.write(f"{movel['id']},{movel['marca']},{movel['valor']},{movel['tipo']},{movel['material']}\n")

    print("Móvel adicionado com sucesso: ")


def removerMoveis():

    id = input("Digite o código do funcionário que deseja remover: ")

    for movel in moveis:
        if movel["id"] == id:
            moveis.remove(movel)
            print("Móvel removido!!")
            return
    print("Móvel não encontrado!!")

removerMoveis(moveis)



# while esc != '0':
#     if esc == '1':

#         arq = open('compras.dat', 'w')
#         arq.write('Berço')
        
#         arq.close()

#     elif esc == '2':

#         arq = open('compras.dat', 'w')
#         arq.write('comoda')
        
#         arq.close()
    
#     elif esc == '3':

#         arq = open('compras.dat', 'w')
#         arq.write('cadeira')
        
#         arq.close()
    
#     elif esc == '4':

#         arq = open('compras.dat', 'w')
#         arq.write('redinha')
        
#         arq.close()


#     else:
    
#         print("Digite uma opcção válida: ")
    
#     print()
#     esc = moveis()
#     print()
