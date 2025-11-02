#CRIE UMA CLASSE MAE CHAMADA ANIMAL COM O SEGUINTE ATRIBUTO: NOME, E MÉTODO: EMITIR_SOM() -> IMPRIME 'SOM GENÉRICO ANIMAL'
#CRIE 3 SUBCLASSES E SOBRESCREVE O MÉTODO EMITIR_SOM DE ACORDO COM CADA ANIMAL; CACHORRO, GATO E PASSARO
#CRUE UMA LISTA COM OBJETOS DESSAS CLASSES E PERCORRA COM UM LOOP CHAMANDA O MÉTODO EMITIR_SOM()

# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico de animal.")

# Subclasses com comportamentos diferentes
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

class Passaro(Animal):
    def emitir_som(self):
        print("Piu piu!")

# Criando uma lista com vários animais diferentes
zoologico = [
    Cachorro("Rex"),
    Gato("Mimi"),
    Passaro("Loro"),
    Gato("Tigre"),
    Cachorro("Bob")
]

# Todos os objetos respondem ao mesmo método de formas diferentes
for animal in zoologico:
    print(f"{animal.nome} faz:", end=" ")
    animal.emitir_som()
