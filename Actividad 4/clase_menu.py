from gestor_motos import GestorMotos
from gestor_pedidos import GestorPedidos
from clase_moto import Moto
from clase_pedido import Pedido
   
class Menu:
    def __init__(self, gestor_motos, gestor_pedidos):
        self.__GestMotos = gestor_motos
        self.__GestPedi = gestor_pedidos

    def mostrar_menu(self):
        # Esta función muestra el menú de opciones al usuario.
        print("------ Menú de opciones ------")
        print("1. Leer datos de las motos desde un archivo .CSV")
        print("2. Leer datos de los pedidos desde un archivo .CSV")
        print("3. Cargar nuevos pedidos")
        print("4. Modificar tiempo real de entrega")
        print("5. Mostrar tiempo promedio de entrega por moto")
        print("6. Generar listado de pago de comisiones")
        print("7. Mostrar datos")
        print("8. Finalizar")

    def MenuDeOpciones(self):
        #Esta función accede a los metodos que llaman cada opción del menú
        bandera = True
        while bandera:
            self.mostrar_menu()
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                print("Seleccionó la opción 1: Leer datos de las motos desde un archivo .CSV")
                self.__GestMotos.cargar()
                self.__GestMotos.ordenar_motos()
                print("Datos leídos con éxito\n=======================")
                #self.__GestMotos.mostrar()
            elif opcion == "2":
                print("Seleccionó la opción 2: Leer datos de los pedidos desde un archivo .CSV")
                self.__GestPedi.cargar()
                self.__GestPedi.ordenar_pedidos()
                print("Datos leídos con éxito\n=======================")
                #self.__GestPedi.mostrar()
            elif opcion == "3":
                print("Seleccionó la opción 3: Cargar nuevos pedidos")
                print()
                self.__GestPedi.nuevoPedido(self.__GestMotos)
                print("Pedido cargado con éxito.")
                #self.__GestPedi.mostrar()
            elif opcion == "4":
                print("Seleccionó la opción 4: Modificar tiempo real")
                self.__GestPedi.modificar()
            elif opcion == "5":
                print("Seleccionó la opción 5: Mostrar tiempo promedio de entrega por moto\n")
                patente_moto = input("Ingrese la patente de la moto: ")
                if self.__GestMotos.Buscar(patente_moto):
                    self.__GestPedi.Promedio(patente_moto)
                else:
                    print("Moto no encontrada")
            elif opcion == "6":
                print("Seleccionó la opción 6: Generar listado de pago de comisiones\n")
                print("------ Generar listado de pago de comisiones ------")
                motos = self.__GestMotos.reglista()
                for moto in motos:
                    patente_moto = moto.get_patente()
                    conductor = f"{moto.get_nombre()} {moto.get_apellido()}"
                    print(f"Patente de moto: {patente_moto}")
                    print(f"Conductor: {conductor}")

                    # Inicializar variables para el cálculo de totales
                    total_tiempo_real = 0
                    total_precio_pedidos = 0

                    # Imprimir encabezado de la tabla de pedidos
                    print("Identificador de pedido\t\t\tTiempo estimado\t\t\tTiempo realt\t\t\tPrecio")
                    
                    # Filtrar los pedidos correspondientes a esta moto
                    pedidos_moto = [pedido for pedido in self.__GestPedi.reglista() 
                                    if pedido.get_patente() == patente_moto]

                    # Imprimir detalles de cada pedido y calcular totales
                    for pedido in pedidos_moto:
                        id_pedido = pedido.get_idP()
                        tiempo_estimado = pedido.get_tiempoEst()
                        tiempo_real = pedido.get_tiempoReal()
                        precio_pedido = pedido.get_precio()
                        print(f"{id_pedido}\t\t\t\t\t{tiempo_estimado}\t\t\t\t{tiempo_real}\t\t\t\t{precio_pedido}") #\t da espacios en la misma linea
                        
                        # Calcular totales
                        if tiempo_real:
                            total_tiempo_real += int(tiempo_real)
                        total_precio_pedidos += precio_pedido
                    
                    # Calcular la comisión (20% del total de precios de los pedidos)
                    comision = total_precio_pedidos * 0.20

                    # Imprimir totales y comisión
                    print(f"Total:\t\t\t\t\t\t\t\t\t\t\t\t\t${total_precio_pedidos}")
                    print(f"Comisión: ${comision:.2f} (20% del total)")
                    print("____________________________________\n")
                    
                    
            elif opcion=="7":
                print("Seleccionó la opción 7: Mostrar datos\n")
                print("Se mostraran los datos de las motos:\n")
                self.__GestMotos.mostrar()
                print()
                print("Se mostraran los datos de los pedidos:\n")
                self.__GestPedi.mostrar()
            elif opcion == "8":
                print("Seleccionó la opción 8: Finalizar")
                print()
                bandera = False
            else:
                print("Opción no válida. Por favor, seleccione una opción válida del menú.")