class farmaciud:
    __filas__=5 #sucursales
    __columnas__=7 #dias
    __matriz__=[]
    def __init__(self):
        for i in range (self.__filas__):
            self.__matriz__.append([0]*self.__columnas__)
    def carga(self,i,j,monto):
        self.__matriz__[i-1][j-1]+=monto
        print(self.__matriz__) #se pintea la matriz para visualizar
    def facturacion (self,i):
        monto=0
        for j in range (self.__columnas__):
            monto+=self.__matriz__[i-1][j]
        print("MONTO DE LA SUCURSAL {} es: {}".format(i, monto))
    def mayormonto(self, i):
        aux=0
        indice=0
        for j in range(self.__filas__):
            if aux<self.__matriz__[j][i-1]:
                aux=self.__matriz__[j][i-1]
                indice=j
        print("Sucursal que mas vendio en el dia {} fue: sucursal {} con monto ${}".format(i, indice+1, aux))
    def menormonto (self):
        _arr_=[]
        for i in range (self.__filas__):
            _arr_.append(0)
        for i in range(self.__filas__):#filas son sucursales
            for j in range (self.__columnas__):
                _arr_[i]+=self.__matriz__[i][j]
        monto=0
        indice=0
        print(_arr_)
        for i in range (self.__filas__):
            if monto<_arr_[i-1]:
                monto=_arr_[i-1]
                indice=i
        print("La sucursal con menor monto en todo la semana fue la sucursal {} con monto: ${}".format(indice+1,_arr_[indice]))
    def montototal (self):
        monto=0
        for i in range (self.__filas__):
            for j in range(self.__columnas__):
                monto+=self.__matriz__[i][j]
        print("el monto total de la semana fue de: ${}" .format(monto))