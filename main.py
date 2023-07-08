import os 
import acessorios
import roupas
import moveis


#Tela de menu principal

print("TESTE")

a1 = "="*40
a2 = "="*15

def menuPrincipal():
    
    os.system('clear')
    
    print(a1)
    print(a2,' PyBaby ',a2)
    print(a1)
    
    print()
    
    print('\t1 - Acessórios')
    #print('\t2 - Fraldas')
    print('\t2 - Roupas')
    print('\t3 - Móveis')
    #print('\t5 - Relatórios')
    #print('\t0 - Finalizar programa')
    
    print()
    
    print(a1)
    
    esc = input('Selecione sua opção: ')
    return esc

esc = menuPrincipal()
while esc != '0':
    if esc == '1':
        acessorios.moduloAcessorios()
    elif esc == '2':
        roupas.moduloRoupas()
    elif esc == '3':
        moveis.moduloMoveis()
    else:
        print("Digite uma opção válida: ")

    print()
    esc = menuPrincipal()
    print()
