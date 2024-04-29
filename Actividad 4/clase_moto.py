#se crea la clase moto
class Moto:
    __patente:str
    __marca: str
    __nombre: str
    __apellido: str
    __km: str
    def __init__(self,patente,marca,nombre,apellido,km):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__apellido = apellido
        self.__km = km
    def get_patente(self):
        return self.__patente

    def get_marca(self):
        return self.__marca

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_km(self):
        return self.__km
    
    def __lt__(self, other):
        return self.__patente < other.__patente
    
    #metodo necesario para porder imprimir los datos y no las direcciones de memoria
    def __str__(self):
        return f"Patente: {self.__patente}\nMarca: {self.__marca}\nConductor: {self.__nombre} {self.__apellido}\nKilometraje: {self.__km}\n========================"
