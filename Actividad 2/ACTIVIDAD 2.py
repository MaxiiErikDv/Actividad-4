class Caja_de_ahorros:
    __nro_cuenta__: str
    __nro_cuentacuil__: str
    __apellido__: str
    __nombre__: str
    __saldo__: float
    def __init__(self, nro_cuenta, cuil, apellido, nombre, saldo):
        self.__nro_cuenta__=nro_cuenta
        self.__cuil__=cuil
        self.__apellido__=apellido
        self.__nombre__=nombre
        self.__saldo__=saldo
    def mostrar_Datos (self):
        print(f"El número de cuenta es: {self.__nro_cuenta__}")
        print(f"Cuil: {self.__cuil__}")
        print(f"Apellido: {self.__apellido__}")
        print(f"Nombre: {self.__nombre__}")
        print(f"Saldo: ${self.__saldo__}")
    def extraer(self,importe):
        if importe <= self.__saldo__:
            self.__saldo__-= importe
            print(f"Se extrajo ${importe:.2f}. Saldo restante: ${self.__saldo__:.2f}")
            return self.__saldo__
        else:
            print("Saldo insuficiente para realizar la extracción.")
            return -1 
    def depositar (self,importe):
        if importe > 0:
            self.__saldo__ = self.__saldo__ + importe
            print(f"Se realizo un deposito de ${importe:.2f}. Saldo actual: ${self.__saldo__:.2f}")
        else:
            print("Importe erroneo")
    def validar_cuil(self):
        if len(self.__cuil__) != 13 or self.__cuil__[2] != '-' or self.__cuil__[11] != '-':
            # Verifica la longitud y los guiones en las posiciones correctas
            return False
        else:
            lista = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
            self.__cuil__ = self.__cuil__.replace("-", "")  # Elimina los guiones
            aux = 0
            for i in range(10):
                aux += int(self.__cuil__[i]) * lista[i]  # Multiplica y suma los dígitos
            aux = 11 - (aux % 11)   # Calcula el dígito verificador restando el resto de la division a 11
            if self.__cuil__[10] == str(aux):
                print("El digito verificador es correcto")
            else:
                print("El digito verificador es incorrecto")
    def retornarCuil (self):
        return self.__cuil__
    def retornarNombre (self):
        return self.__nombre__
    def retornarApellido(self):
        return self.__apellido__

def test():
    print("Se comenzara la carga de datos de los objetos: ")
    nro_cuenta = (input('NUMERO DE CUENTA:'))
    cuil = (input('CUIL (con guiones):'))
    apellido = (input('APELLIDO:'))
    nombre = (input('NOMBRE:'))
    saldo = 0
    caja=Caja_de_ahorros(nro_cuenta, cuil, apellido, nombre,saldo)
    print("Datos cargados exitosamente.")
    #MENU DE OPCIONES DE CARGA
    while True:
        print("\nMENU DE OPCIONES:")
        print("1. Realizar un depósito")
        print("2. Realizar una extracción")
        print("3. Validar CUIT")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == '1':
            importe_deposito = float(input("Ingrese el importe a depositar: "))
            caja.depositar(importe_deposito)
        elif opcion == '2':
            importe_extraccion = float(input("Ingrese el importe a extraer: "))
            caja.extraer(importe_extraccion)
        elif opcion == '3':
            caja.validar_cuil()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    caja.mostrar_Datos()  # Imprimir los datos de la caja de ahorros al final
    return caja 

def cargarCajas (lista):
    for i in range (3):
        c= test()
        print(c)
        lista.append(c)

class contenedor:
    def __init__(self):
        self.__arreglo__ = []
        self.__tamano__ = 3

    def carga(self):
        print("Se comenzara la carga de datos de los objetos: ")
        for i in range(self.__tamano__):
            nro_cuenta = input('NUMERO DE CUENTA:')
            cuil = input('CUIL (con guiones):')
            apellido = input('APELLIDO:')
            nombre = input('NOMBRE:')
            saldo = 0
            caja = Caja_de_ahorros(nro_cuenta, cuil, apellido, nombre, saldo)
            self.__arreglo__.append(caja)

    def mostrarNyASaldoCuil(self, ncuil):
        for caja in self.__arreglo__:
            if ncuil == caja.retornarCuil():
                print(caja.retornarCuil())
                print(caja.retornarNombre())
                print(caja.retornarApellido())
            else:
                print("El numero de cuil no es encuentra")

if __name__ == '__main__':
    salida = contenedor()
    salida.carga()
    cuil = input("Ingrese Numero de cuil: ")
    salida.mostrarNyASaldoCuil(cuil)