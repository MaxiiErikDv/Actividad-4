#se crea la clase pedido
class Pedido:
    __patente=str
    __idP=int
    __comidas=str
    __tiempoEst=str
    __tiemReal=str
    __precio=float
    
    def __init__(self,patenteP,IdPed,comidas,Testim,precio,Treal=0):
        self.__patente=patenteP
        self.__idP=IdPed
        self.__comidas=comidas
        self.__tiempoEst=Testim
        self.__tiemReal=Treal
        self.__precio=precio
    #metodo necesario para porder imprimir los datos y no las direcciones de memoria
    def get_patente(self):
        return self.__patente
    
    def get_idP(self):
        return self.__idP
    
    def mod_tiempo_real(self, tiempo_real):
        self.__tiemReal = tiempo_real
    
    def get_tiempoReal(self):
        return self.__tiemReal
    
    def get_tiempoEst(self):
        return self.__tiempoEst
    
    def get_precio (self):
        return self.__precio
    
    def __lt__(self, other):
        return self.__patente < other.__patente
    
    def __str__(self):
        return f"Patente: {self.__patente}\nId Pedido: {self.__idP}\nComidas: {self.__comidas}\nTiempo estimado: {self.__tiempoEst}\nTiempo real: {self.__tiemReal}\nPecio:{self.__precio}\n========================"
        