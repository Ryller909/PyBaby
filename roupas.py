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

    print('\t1 - Calções')
    print('\t2 - Camisas')
    print('\t3 - Fraldas de pano')
    print('\t4 - Luvas')
    print('\t5 - Meias')
    print('\t6 - Toucas')

    print()
    print(a1)

    esc = input('Selecione o que deseja: ')
    return esc

esc = roupas()