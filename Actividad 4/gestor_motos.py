import csv
from clase_moto import Moto

#se crea la clase GestorMotos
class GestorMotos:
    __lista=[]
    def __init__(self) -> None:
        self.__lista=[]
    def cargar (self):
        #se abre el cvs
        with open(r"D:\Documentos\Maxi ;)\&&Informatica\LCC\Segundo Año\Programacion Orientada a Objetos\Unidad 2 2023\Codigos\Actividad 4\datos_Motos.csv",'r') as archivo:
            reader= csv.reader(archivo,delimiter=',')
            next(reader)#se salta la primera fila, generalmente son los encabezados
            
            #se cargan los datos del csv, en la clase moto y posteriormente al gestor
            for fila in reader:
                Patente,Marca,Nombre,Apellido,Kilometraje=fila
                moto=Moto(Patente,Marca,Nombre,Apellido,int(Kilometraje))
                self.__lista.append(moto)
            #se cierra el archivo
            archivo.close()
            
    def mostrar (self):
        for i in range(len(self.__lista)):
            print(self.__lista[i]) 
    
    #Se crea un metodo Buscar para validar la existencia de la patente
    def Buscar(self, Pat):
    # Verificamos la existencia de la moto
        for moto in self.__lista:
            if moto.get_patente() == Pat:
                print("La moto se encontró en la base de datos")
                return True
        print("La moto no se encontró en la base de datos")
        return False
    def reglista(self):
        return self.__lista
    
    def ordenar_motos(self):
        self.__lista.sort()