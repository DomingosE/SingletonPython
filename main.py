# Criação da classe Singleton
class Singleton:
    _instancia = None

# Criação da função que será responsável por uma nova instancia
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

# Criação de uma função que será responsável pela propriedade de uma classe Singleton
    def __init__(self):
        self.propriedade = "Exemplo de propriedade em uma classe Singleton"

# As variáveis singleton1 e singleton2 estão recebendo o valor que está dentro da Classe Singleton
singleton1 = Singleton()
singleton2 = Singleton()

# Os prints abaixo irão printar "Exemplo de propriedade em uma classe Singleton" por duas vezes na execução no terminal
print(singleton1.propriedade)
print(singleton2.propriedade)

# A variável singleton1 recebe o valor "Nova propriedade"
singleton1.propriedade = "Nova propriedade"

# Os prints abaixo irão printar "Nova propriedade" por duas vezes na execução no terminal
print(singleton1.propriedade)
print(singleton2.propriedade)
