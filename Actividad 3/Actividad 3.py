from claseFarmaciud import farmaciud
if __name__ == '__main__':
    a=farmaciud()
    while True:
        print(' 1: carga')
        print(" 2: facturacion sucursal")
        print(" 3: ver que sucursal facturo mas en el dia")
        print(" 4: ver que sucursal facturo mas en la semana")
        print(" 5: calcular monto total de las sucursales en toda la semana")
        print(" 0: terminar operaciones")
        opcion=int(input("ingrese opcion: "))
        if opcion==1:
            print("eligio opcion 1: ingrese datos")
            i=int(input("ingrese sucursal, del 1 al 5: " ))
            j=int(input("ingrese dia, del 1 al 7: "))
            monto=float(input("ingrese monto: "))
            a.carga(i,j,monto)
        if opcion==2:
            print("eligio opcion 2: ingrese datos")
            i=int(input("ingrese sucursal, del 1 al 5: " ))
            a.facturacion(i)
        if opcion==3:
            print("eligio la opcion 3: ingrese datos")
            i=int(input("ingrese dia: "))
            a.mayormonto(i)
        if opcion==4:
            print("eligio la opcion 4: ingrese datos")
            a.menormonto()
        if opcion==5:
            print("eligio la opcion 5")
            a.montototal()
        if opcion==0:
            print("hazzzta la prosimaaa ;)")
            break