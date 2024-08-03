from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog
from prompt_toolkit.styles import Style
import os
from module import clases as cl

def mostrar_menu():
    style = Style.from_dict({
        "dialog": "bg:#ffffff #000000",        # Fondo blanco, texto negro
        "button": "bg:#ffffff #000000",        # Botones con fondo blanco, texto negro
        "button-focused": "bg:#00aaaa #ffffff",# Fondo azul claro, texto blanco cuando está enfocado
    })

    result =radiolist_dialog(
        title="Bienvenido al menú",
        text="Seleccione una opción:",
        values=[
            ("Cargar los Productos", "cargar_productos"),
            ("Opción 2", "opcion_2"),
            ("Opción 3", "opcion_3"),
            ("Agregar Nuevos Productos", "Agregar Nuevos Productos"),
            ("Borrar Productos", "Borrar Productos"),
            ("Opción 6", "opcion_6"),
            ("salir", "salir"),
        ],
        ok_text="Ok",
        cancel_text="Cancel",
        style=style,
    ).run()

    print(f"Resultado de la selección del menú: {result}")
    return result

def main():
    listaProducto = cl.ProductosVentas()

    while True:
        opcion = mostrar_menu()
        print(f"opcion: {opcion}")

        if opcion is None:
            print("\nCancelado por el usuario.\n")
            break
        if opcion == "Cargar los Productos":
            listaProducto.cargarArchivoProductos()
            m= message_dialog(title="Cargar los Productos", text=listaProducto.imprimirTabla()).run() 
            
            os.system('pause')
        elif opcion == "opcion_2":
            print("\nMensaje de apoyo moral para la Opción 2: Confía en tu capacidad para lograr lo que te propongas.")
            os.system('pause')
        elif opcion == "opcion_3":
            print("\nMensaje de apoyo moral para la Opción 3: Eres capaz de enfrentar cualquier desafío que se presente.")
            os.system('pause')
        elif opcion == "Agregar Nuevos Productos":
            listaProducto.cargarManualProductos()
            os.system('pause')
        elif opcion == "Borrar Productos":
            print("Ejecutando Opción 5")
            listaProducto.borrarProducto()
            os.system('pause')
        elif opcion == "opcion_6":
            print("Ejecutando Opción 6")
            os.system('pause')
        elif opcion == "salir":
            listaProducto.grabarArchivoProductosSalarios()   
            os.system('pause')
            break
        else:
            print("\nOpción no válida\n")
            os.system('pause')

if __name__ == "__main__":
    main()
