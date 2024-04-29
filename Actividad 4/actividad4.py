
from gestor_motos import GestorMotos
from gestor_pedidos import GestorPedidos
from clase_menu import Menu
 
if __name__=='__main__':
    GestMotos=GestorMotos()
    GestPedi=GestorPedidos()
    objeto=Menu(GestMotos,GestPedi)
    print("Se desplegara el Menú de acciones")
    objeto.MenuDeOpciones()
    print("Nos vimo")

