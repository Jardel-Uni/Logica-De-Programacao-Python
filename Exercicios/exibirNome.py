import tkinter as tk

def obter_nome():
    # Esta função será chamada quando o botão for clicado
    nome_digitado = caixa_entrada.get()
    print(f"O nome digitado é: {nome_digitado}")
    # Aqui você pode fazer o que quiser com o nome, como exibir em outro label, etc.

# 1. Criar a janela principal
janela_principal = tk.Tk()
janela_principal.title("Entrada de Nome") # Define o título da janela

# 2. Criar o rótulo de instrução (Label)
label_instrucao = tk.Label(janela_principal, text="Por favor, digite seu nome:")
label_instrucao.pack(pady=5) # Posiciona o rótulo na janela e adiciona um pequeno espaçamento vertical

# 3. Criar a caixa de entrada (Entry)
caixa_entrada = tk.Entry(janela_principal, width=50) # Define a largura da caixa
caixa_entrada.pack(pady=5)

# 4. Criar o botão para submeter o nome
botao_submit = tk.Button(janela_principal, text="Enviar", command=obter_nome)
botao_submit.pack(pady=10)

# 5. Iniciar o loop principal da aplicação (para manter a janela aberta)
janela_principal.mainloop()