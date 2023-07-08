import os 

#Tela de escolha de móveis

a1 = "="*40
a2 = "="*15

def moveis():

    os.system('clear')

    print(a1)
    print(a2,' Móveis ',a2)
    print(a1)
    print()

    print('\t1 - Berço')
    print('\t2 - Comoda')
    print('\t3 - Cadeira')
    print('\t4 - Redinha')
    #print('\t4 - ')
    #print('\t5 - ')

    print()
    print(a1)

    esc = input('Selecione o  que deseja: ')
    return esc

esc = moveis()



while esc != '0':
    if esc == '1':

        arq = open('compras.txt', 'w')
        arq.write('Berço')
        
        arq.close()

    elif esc == '2':

        arq = open('compras.txt', 'w')
        arq.write('comoda')
        
        arq.close()
    
    elif esc == '3':

        arq = open('compras.txt', 'w')
        arq.write('cadeira')
        
        arq.close()
    
    elif esc == '4':

        arq = open('compras.txt', 'w')
        arq.write('redinha')
        
        arq.close()


    else:
    
        print("Digite uma opcção válida: ")
    
    print()
    esc = moveis()
    print()
