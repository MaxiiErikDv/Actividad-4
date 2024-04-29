from CajadeAhorros import Caja_de_ahorros
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