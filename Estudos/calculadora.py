# numeroUm = 10
# numeroDois = 30

# soma = numeroDois + numeroUm

# print(soma)

# print("Insira o primeiro numero")
# numeroUm = input()

# print("Insira o segundo numero")
# numeroDois = input()

# print("Resultado da soma dos numeros")
# resultado = int(numeroUm) + int(numeroDois)

# print(resultado)

def somar(valor):
    for i in range (1,11):
        print(i, "+" , valor, "=" , int(i) + valor)

def subtrair(valor):
    for i in range (1, 11):
        print(i, "-" , valor, "=" , int(i) - valor)

def multiplicar(valor):
    for i in range (1, 11):
        print(i, "x" , valor, "=" , int(i) * valor)

print(somar(2))
print("------------------------")
print(subtrair(2))
print("------------------------")
print(multiplicar(2))
print("------------------------")



  

