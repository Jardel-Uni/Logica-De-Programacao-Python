import tkinter as tk
from tkinter import messagebox

numeroUm = 10
numeroDois = 20 

root = tk.Tk()
root.withdraw()  # Esconde a janela principal

soma =  numeroUm + numeroDois
subtracao = numeroDois - numeroUm
multiplicacao = numeroUm * numeroDois
divisao = numeroDois / numeroUm

print("Resultado soma = ", soma)
print("Resultado subtração = ", subtracao)
print("Resultado multiplicação = ", multiplicacao)
print("Resultado divisão = ", divisao)

messagebox.showinfo("Resultados", f" Soma: {soma}\n Subtração: {subtracao}\n Multiplicação: {multiplicacao}\n Divisão: {divisao}")