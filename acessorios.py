import os 


#Tela de esolha de acessórios

a1 = "="*40
a2 = "="*15

def acessorios():
  
    os.system('clear')
  
    print(a1)
    print(a2,' Acessórios ',a2)
    print(a1)
    print()
    
    print('\t1 - Brinquedo')
    print('\t2 - Chupeta')
    print('\t3 - Escova de cabelo')
    print('\t4 - Escova de desntes')
    print('\t6 - Fraldas descartáveis')
    print('\t7 - Mamadeira')

    print()
    print(a1)

    esc = input('Selecione o  que deseja: ')
    return esc  

esc = acessorios()