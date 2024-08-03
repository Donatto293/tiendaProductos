"funciones del menu"
""" 
CBA
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 05/07/2024

"""
import signal
import sys
import os
from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog
from prompt_toolkit.styles import Style
from module import clases as cl
from module import clases_carrito as carrito
from module import excepciones as ex


#esta funcion muestra el menu usando radiolist_dialog para las opciones
#retorna los valores de las opciones
def mostrar_menu():
    #el estilo del menu
    style = Style.from_dict({
        "dialog": "bg:#ffffff #000000",        # Fondo blanco, texto negro
        "button": "bg:#ffffff #000000",        # Botones con fondo blanco, texto negro
        "button-focused": "bg:#00aaaa #ffffff",# Fondo azul claro, texto blanco cuando está enfocado
    })
    #las opciones del menu
    result =radiolist_dialog(
        title="Bienvenido al menú",
        text="Seleccione una opción:",
        values=[
            ("Cargar los Productos", "Cargar los Productos"),
            ("Copia De Respaldo", "Copia De Respaldo"),
            ("Reparar Datos", "Reparar Datos"),
            ("Agregar Nuevos Productos", "Agregar Nuevos Productos"),
            ("Borrar Productos", "Borrar Productos"),
            ("Comprar Producto", "Comprar Producto"),
            ("Quitar Productos del Carrito", "Quitar Productos del Carrito"),
            ("Imprimir Factura", "Imprimir Factura"),

            ("salir", "salir"),
        ],
        ok_text="Ok",
        cancel_text="Cancel",
        style=style,
    ).run()

    #print(f"Resultado de la selección del menú: {result}")
    return result



#funcion de prueba para controlar Ctrl+ c
#def signal_handler(sig, frame):
    print("\nInterrupción con Ctrl+C deshabilitada. Utilice la opción 'salir' del menú para cerrar el programa.")
    

def main():

    # Configurar el manejador de señal para Ctrl+C(prueba)
    #signal.signal(signal.SIGINT, signal_handler)

    #instanciamos las clases
    listaProducto = cl.ProductosVentas()
    carritoCompra = carrito.CarritoCompra()

    #ciclo while para mantener el menu abierto hasta que el usuario salga
    while True:
        try:
            opcion = mostrar_menu()#llamamos la menu 
            print(f"opcion: {opcion}")

            if opcion is None:#opcion cancelar
                print("\nCancelado por el usuario.\n")
                break
            if opcion == "Cargar los Productos": #para cargar los datos de la base de datos json
                os.system('cls')
                listaProducto.cargarArchivoProductos()
                os.system('pause')
            elif opcion == "Copia De Respaldo": #guarda una copia en la base de datos
                os.system("cls")
                listaProducto.copiaRespaldo()
                listaProducto.imprimirTabla()
                print("\nCopia de respaldo Creada.")
                os.system('pause')
            elif opcion == "Reparar Datos": #esta opcion carga los datos de una copia guardada
                os.system("cls")
                listaProducto.repararDatos()
                os.system('pause')
            elif opcion == "Agregar Nuevos Productos": #para agregar nuevos productos al menu 
                listaProducto.cargarManualProductos()
                os.system('pause')
            elif opcion == "Borrar Productos": #borrar productos del menu
                listaProducto.borrarProducto()
                os.system('pause')
            elif opcion == "Comprar Producto": #para comprar productos de menuw
                os.system("cls")
                
                while True:
                    os.system("cls")
                    listaProducto.imprimirTabla()
                    entrada = ex.input_con_error("Digite el codigo del Producto que vas a comprar(N para salir): ").upper()
                    if entrada =="N":
                        print("regresando al menu...") 
                        break
                    if not carritoCompra.verificarCodigoProducto(entrada,listaProducto): #verificacion si el codigo existe en el menu
                        continue
                    inventario= ex.solicitar_dato_int("Digite la cantidad del Producto que vas a comprar: ")
                    if carritoCompra.datoCantidadProducto(entrada,inventario, listaProducto): #verificacion del inventario en caso de que solicite mas que el inventario existente
                        carritoCompra.nuevoProducto(entrada ,inventario,listaProducto)
                        os.system("pause")
                        continue     
                os.system('pause')
            elif opcion== "Quitar Productos del Carrito": #para eliminar productos del carrito de compras
                os.system("cls")
                carritoCompra.datosCompra()
                carritoCompra.borrarProducto(listaProducto)
                os.system('pause')
            elif opcion == "Imprimir Factura": #realiza la compra y imprime la factura
                os.system("cls")
                carritoCompra.facturaCompra(listaProducto)
                os.system('pause') 
            elif opcion == "salir": #para salir y guardar los cambios realiados
                os.system("cls")
                listaProducto.grabarArchivoProductos() 
                print("cerrando la tienda")  
                os.system('pause')
                break
            else:
                print("\nOpción no válida\n")
                os.system('pause')
        except KeyboardInterrupt: # try except para inabilitar el Ctrl+c
            print("\nInterrupción con Ctrl+C deshabilitada. Utilice la opción 'salir' del menú para cerrar el programa.")
            continue
