import os 
import pickle


#Tela de escolha de funcionarios

a1 = "="*40
a2 = "="*15

def funcionarios():

    os.system('clear')

    print(a1)
    print(a2,' Funcionários ',a2)
    print(a1)
    print()

    print('\t1 - Cadastrar novo Funcionários')
    print('\t2 - Remover Funcionários')
    print('\t3 - Ver funcionários')
    #print('\t4 - Redinha')
    #print('\t4 - ')
    #print('\t5 - ')

    print()
    print(a1)

    esc = input('Selecione o  que deseja: ')
    return esc

esc = funcionarios()


def cadastrarFuncionario():

    funcionarios = []
    
    id = int(input("Digite o código do funcionário: "))
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o valor do sálario: "))

    funcionario = {
        'id' : id,
        'nome' : nome,
        'cargo' : cargo,
        'salario' : salario
    }

    #funcionarios.append(funcionario)

    with open("dados.dat", "a") as arquivo:
        arquivo.write(f"{funcionario['id']},{funcionario['nome']},{funcionario['cargo']},{funcionario['salario']}\n")

    print("Funcionário cadastrado com sucesso!!")


def removerFuncionario():

    id = input("Digite o código do funcionário que deseja remover: ")

    for funcionario in funcionarios:
        if funcionario["id"] == id:
            funcionarios.remove(funcionario)
            print("Funcionário removido!!")
            return
    print("Funcionário não encontrado!!")

removerFuncionario(funcionarios)







# while esc != '0':
#     if esc == '1':
#         print()
#     elif esc == '2':
#         print()
#     elif esc == '3':
#         print()
#     else :
#         print()



