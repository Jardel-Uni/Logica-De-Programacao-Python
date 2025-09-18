# numero = [1, 2, 3, 4, 5]
# print(numero)
# print(numero [0]) #indice

cidades = ["Fortaleza", "Sobral", "Canindê"]
print(cidades)
print("-------------------------------")
cidades.append("Redenção") #add no final
cidades.remove("Fortaleza") #remove um item
print(cidades)
cidades.sort() #ordena em ordem alfabetica
print("-------------------------------")
print(cidades)
print(len(cidades)) # mostra o tamanho

#add mais cinco cidades
# while len(cidades) > 1:
#     novasCidade = ["Brasilia", "Rio de Janeiro", "São Paulo", "Recife", "Porto Alegre"]
#     cidades.append(novasCidade)
#     cidades = cidades
#     break

novasCidades = ["Brasilia", "Rio de Janeiro", "São Paulo", "Recife", "Porto Alegre"]
cidades.extend(novasCidades)
cidades.sort()

print("-------------------------------")
print(cidades)
print(len(cidades))

print("-------------------------------")
for cidades in cidades:
    print(cidades)    
    
