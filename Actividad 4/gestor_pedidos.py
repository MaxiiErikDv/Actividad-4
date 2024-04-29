from clase_pedido import Pedido
import csv
#Se crea la clase "GestorPedidos"
class GestorPedidos:
    __listaP=[] #Se define una lista donde se almacenaran los datos
    def __init__(self) -> None:
        self.__listaP=[]
    def cargar (self):
        with open(r"D:\Documentos\Maxi ;)\&&Informatica\LCC\Segundo Año\Programacion Orientada a Objetos\Unidad 2 2023\Codigos\Actividad 4\datos_pedidos.csv",'r')as archivo:
            reader=csv.reader(archivo,delimiter=',')
            next(reader)
            for fila in reader:
                Patente,Id,Comidas,TiempoEstimado,Precio=fila
                pedido=Pedido(Patente,int(Id),Comidas,TiempoEstimado,float(Precio))
                self.__listaP.append(pedido)
            archivo.close()
    def mostrar (self):
        for i in range(len(self.__listaP)):
            print(self.__listaP[i]) 
    
    def nuevoPedido(self,gestor_motos):
        print("A continuacion ingresara los datos del nuevo pedido:")
        Pat=input("Ingrese la patente de la moto a asigar al pedido:")
        band = gestor_motos.Buscar(Pat)
        if band==True:
            id=int(input("ID del pedido:"))
            Com=input("Comidas:")
            Test=input("Tiempo estimado:")
            Precio=float(input("Precio total:"))
            datospedido=Pedido(Pat,id,Com,Test,Precio)
            self.__listaP.append(datospedido)
            print("Pedido asignado a la moto con patente:",Pat)
            
    def modificar(self):
        patente = input("Ingrese el número de patente: ")
        id_pedido = int(input("Ingrese el identificador del pedido: "))
        tiempo_real = input("Ingrese el tiempo real de entrega: ")
        for pedido in self.__listaP:
            if pedido.get_patente() == patente and pedido.get_idP() == id_pedido:
                pedido.mod_tiempo_real(tiempo_real)
                print("Tiempo real de entrega modificado con éxito.")
                return
        print("El pedido no fue encontrado. Verifique los datos ingresados.")
        
    def Promedio(self,patente):
        tiempo_total = 0
        cantidad_pedidos = 0
        for pedido in self.__listaP:
            if pedido.get_patente() == patente:
                tiempo_real = pedido.get_tiempoReal()
                if tiempo_real:
                    tiempo_total += int(tiempo_real)
                    cantidad_pedidos += 1
        if cantidad_pedidos > 0:
            tiempo_promedio = tiempo_total / cantidad_pedidos
            print(f"Tiempo promedio de entrega para la moto {patente}: {tiempo_promedio} minutos\n")
        else:
            print("No hay pedidos registrados para esta moto.")
            
    def reglista(self):
        return self.__listaP
    
    def ordenar_pedidos(self):
        self.__listaP.sort()