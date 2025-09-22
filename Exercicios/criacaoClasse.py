class Cachorro:
    # Variável de classe (comum a todas as instâncias)
    especie = 'mamífero'

    # Construtor (método __init__)
    def __init__(self, nome, idade):
        # Atributos de instância (únicos para cada objeto)
        self.nome = nome
        self.idade = idade

    # Método de instância
    def descricao(self):
        return f"{self.nome} tem {self.idade} anos e é um {self.especie}."

    # Outro método
    def latir(self, som):
        return f"{self.nome} diz {som}."
    
    # Criando instâncias da classe Cachorro
meu_cachorro = Cachorro("Rex", 3)
outro_cachorro = Cachorro("Buddy", 5)

# Acessando atributos e chamando métodos
print(meu_cachorro.descricao())        # Saída: Rex tem 3 anos e é um mamífero.
print(outro_cachorro.latir("Woof!"))   # Saída: Buddy diz Woof!.