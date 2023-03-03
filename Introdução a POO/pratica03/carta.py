# Classe das cartas
class Carta():
    # Método Construtor
    # Quando utilizamos o método construtor, obrigatóriamente este será executado da hora da instanciação de um objeto.
    # Podemos usar o type hint de Python para explicitar qual será o tipo de determinado parâmetro
    #   numero: str
    # Ou também podemos deixar um parâmetro com um valor defaut, caso não seja passado nenhum parâmetro e que também determinará o tipo de dados a ser usado nesse parâmetro.
    #   pontos=0
    def __init__(self, numero: str, naipe: str, pontos=0):
        # Atributos da classe Carta
        self.numero = numero
        self.naipe = naipe
        self.pontos = pontos

    # Métodos
    def getNaipe(self):
        return self.naipe

    def getNumero(self):
        return self.numero

    def getPontos(self):
        return self.pontos

    def setPontos(self, pontos):
        self.pontos = pontos

    def __str__(self):
        return f"{self.numero} de {self.naipe}"
