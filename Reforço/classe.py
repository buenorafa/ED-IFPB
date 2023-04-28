class Copo:
    # volume, material, marca
    def __init__(self, volume, material, marca) -> None:
        self.__volume = volume
        self.__material = material
        self.__marca = marca

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, quantidade):
        self.__volume = quantidade

    def esvaziar(self):
        self.__volume = 0

    def encher(self, quantidade):
        self.__volume += quantidade

    def __len__(self):
        return self.__volume

    def __str__(self) -> str:
        return f'Volume: {self.__volume}\nMaterial: {self.__material}\nMarca: {self.__marca}'


copo1 = Copo(500, 'Aluminio', 'Tramontina')

print(copo1.volume)
copo1.volume = 0
copo1.esvaziar()
