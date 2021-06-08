#Declaração das varáveis utilizadas
valor_compra = 0    
valor_venda = 0
porcentagem = 0
lucro_menor_10 = 0
lucro_10_20 = 0
lucro_maior_20 = 0

#Entradas dos valores e verificação da porcentagem do lucro
for contador in range(10):
    valor_compra = float(input(f"Qual é o valor de compra do {contador+1}º produto? R$"))
    valor_venda = float(input(f"Qual é o valor de venda do {contador+1}° produto? R$"))
    porcentagem = ((valor_venda-valor_compra)/valor_venda)*100
    print(f"Porcetagem do lucro {porcentagem:.2f}%")
    #Teste para ver em qual categoria se encaixa
    if porcentagem < 10:
        lucro_menor_10 = lucro_menor_10+1
    elif porcentagem >= 10 and porcentagem <=20:
        lucro_10_20 = lucro_10_20+1
    elif porcentagem > 20:
        lucro_maior_20 = lucro_maior_20+1
    

print(f"Lucro menor que 10%: {lucro_menor_10} produtos.")
print(f"Lucro entre 10% e 20%: {lucro_10_20} produtos.")
print(f"Lucro maior que 20%: {lucro_maior_20} produtos.")



