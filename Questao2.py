def consoante_ou_vogal (letra):
    vogais = ["a","e","i","o","u","y","A","E","I","O","U","Y"] # Vogais ....Escolhi colocar Y como uma vogal, pois pode ser classificado assim
    consoantes= ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","X","Z"] #Consoantes
    if letra in vogais:
        print(f"A letra {letra} é uma vogal!")
    elif letra in consoantes:
        print(f"A letra {letra} é uma consoante!")
    elif letra == "w" or letra == "W": # W pode ser uma consoante ou uma volga
        print(f"{letra} pode ser uma vogal ou consoante!")
    elif letra.isnumeric(): #Verificando se o caractere é numérico
        print(f"{letra} é um número!")
    else:
        print(f"{letra} é um caractere especial!") #Caso seja digitado um caractere especial

letra = input("Digite uma letra: ")
if len(letra)>1 or len(letra)<1: # Verificar se está sendo digitado apenas um caractere
    print("Inválido! Digite apenas uma letra!")
else:
    consoante_ou_vogal(letra)


