#feito por IA
import tkinter as tk
from tkinter import simpledialog, messagebox
#----------

#nome = input("Digite o seu nome: ")
#idade = input("Digite sua idade: ")


#print("Digite o primeiro numero")
#primeiroNumero = input()


#print("Digite o segundo numero")
#segundoNumero = input()

#soma = int(primeiroNumero) + int(segundoNumero)

#print("A soma dos dois numeros é: ", soma)


#feito por IA
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

primeiro_numero = simpledialog.askstring("Entrada", "Digite o primeiro número:")
segundo_numero = simpledialog.askstring("Entrada", "Digite o segundo número:")

if primeiro_numero is not None and segundo_numero is not None:
    try:
        soma = int(primeiro_numero) + int(segundo_numero)
        messagebox.showinfo("Resultado", f"A soma dos dois números é: {soma}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite apenas números inteiros.")
else:
    messagebox.showwarning("Aviso", "Entrada cancelada.")

root.destroy()
#----------