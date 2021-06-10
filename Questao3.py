#Utilize o VisuAlg para desenvolver um código que leia um arquivo contendo o nome e saldo da conta bancária de 15 clientes diferentes 
#e ao final imprima na tela o nome e saldo da conta bancária de todos os clientes que têm saldo negativo na conta incluindo a seguinte mensagem: 
#O cliente tem saldo negativo - entrar em contato, e além disso grave um arquivo contendo o nome e saldo da conta bancária de todos esses clientes que têm 
#saldo negativo na conta.

#Para que o código possa ser elaborado corretamente, crie um arquivo no formato utilizado pelo VisuAlg contendo o nome e saldo da conta 
#bancária de 15 clientes e defina alguns saldos negativos.

def adicionador_clientes(clientes):   #Funçao para adicionar clientes e seus saldos a lista
    for i in range(15):
        adicionar_clientes.writelines(input("Digite o nome: "))
        adicionar_clientes.writelines("  R$ ")
        adicionar_clientes.writelines(input("Digite o saldo da conta: R$"))
        print("\n")
        adicionar_clientes.writelines("\n")
        

def ler_negativos(lista): #Função para ler os negativos e adicioná-los a uma lista
    adicionar_negativos = open("listaNegativos.txt", "w")
    print("\nClientes com saldo negativo: \n")
    for linha in lista:
        if "-" in linha:
            print(f"{linha} ----- O cliente tem saldo negativo - entrar em contato!")
            adicionar_negativos.writelines(linha)

    print("\n---------------------------------------------------------")
    print("Lista com clientes negativos gerada: 'listaNegativos.txt'")
    print("---------------------------------------------------------")
    adicionar_negativos.close()

            


adicionar_clientes = open("listaClientes.txt", "w")
adicionador_clientes(adicionar_clientes)
adicionar_clientes.close()


lista = open("listaClientes.txt", "r")
ler_negativos(lista)
lista.close()









