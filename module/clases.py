""" 
CBA
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 05/07/2024

"""
"""aqui se encuentran las clases producto y lista de productos"""

import json 
import os
from datetime import datetime
import shutil
from module import excepciones as ex


class Producto():
    def __init__(self,codigoProducto='',nombreProducto='',inventorioProducto=0,precioProducto=0.00,):
        self.__codigoProducto = str(codigoProducto)
        self.__nombreProducto = str( nombreProducto)
        self.__inventorioProducto = int(inventorioProducto)
        self.__precioProducto = float(precioProducto)
        
    #getters and setters
    
    def get_codigoProducto(self):
        return self.__codigoProducto
    
    
    def set_codigoProducto(self,value):
        self.__codigoProducto = str(value)
        
        
    def get_nombreProducto(self):
        return self.__nombreProducto
    
    
    def set_nombreProducto(self,value):
        self.__nombreProducto = str(value)
        
        
    def get_inventorioProducto(self):
        return self.__inventorioProducto
    
    
    def set_inventorioProducto(self,value):
        self.__inventorioProducto = int(value)
        
        
    def get_precioProducto(self):
        return self.__precioProducto
    
    
    def set_precioProducto(self,value):
        self.__precioProducto = float(value)


    #METODO
    def diccionario(self):
        return {
            'codigoProducto': self.get_codigoProducto(),
            'nombreProducto': self.get_nombreProducto(),
            'inventarioProducto': self.get_inventorioProducto(),
            'precioProducto': self.get_precioProducto()
        }    


#Clase donde se guardaran los productos
class ProductosVentas():
    #metodo constructor
    def __init__(self, listaProducto=None):
        if listaProducto is None:
            listaProducto = []
        self.__listaProducto = listaProducto

        
    #getters y setters
    def set_listaProductos(self,producto):
        self.__listaProducto.append(producto)
        
    
    def get_listaProducto(self):
        return self.__listaProducto
    

    #metodos de la clase productos venta
    def digitarDato(self, mensaje):
        print("falta desarrollar")

    
    #crea la lista, cargando datos del archivo json
    def cargarDelJson(self):
        with open('ArchivoDeUso/bd.json', 'r') as json_file:
            data = json.load(json_file)
            for objeto in data:
                producto = Producto()
                producto.set_codigoProducto(objeto['codigoProducto'])
                producto.set_nombreProducto(objeto['nombreProducto'])
                producto.set_inventorioProducto(objeto['inventarioProducto'])
                producto.set_precioProducto(objeto['precioProducto'])
                self.set_listaProductos(producto)
            if not self.get_listaProducto():
                producto=Producto('0','',0,0)
                self.set_listaProductos(producto)
                print("no se encontraron datos en el archivo actual, Se creo un producto para poder Trabajar(Recuerde Borrarlo luego)")
                os.system('pause')
                
    #realiza la copia de respaldo
    def copiaRespaldo(self):
        #variable que encierra la fecha de hoy
        fecha_hoy= datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        #variable de la base de datos
        carpeta= 'BaseDatos'
        #el nombre de la copia de respaldo
        nombre_archivo_respaldo = f'BD-{fecha_hoy}.json' 
        #aqui se ubica el archivo
        ruta_archivo = os.path.join(carpeta, nombre_archivo_respaldo)
        
        #se guarda la copia de respaldo 
        self.ordenar_por_codigo()
        with open(ruta_archivo, 'w') as archivo_respaldo:
            productos_diccionario = [producto.diccionario() for producto in self.get_listaProducto()]
            json.dump(productos_diccionario, archivo_respaldo, indent=4)
            
    
    #carga datos de una copia de respaldo        
    def repararDatos(self):
        #ubicamos la carpeta de base de datos
        carpeta= 'BaseDatos'
        #se crea una lista con los archivos de la carpeta que terminen en .json
        archivos_respaldo = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.json')]
        
        #Si no hay archivos de respaldo, se muestra un mensaje y termina
        if not archivos_respaldo:
            print('No hay copias de respaldo disponibles.')
        else:
            # Mostrar los archivos de respaldo disponibles enumerados
            print('Copias de respaldo disponibles:')
            #idx es el indice de la lista de los archivos
            for idx, archivo in enumerate(archivos_respaldo):
                print(f'{idx + 1}. {archivo}')#se imprime la lista de los archivos de respaldo
        #input de seleccion de archivo     
        seleccion = ex.solicitar_dato_int('Seleccione el número de la copia de respaldo que desea abrir: ')
        if 1 <= seleccion <= len(archivos_respaldo):#aseguro que la seleccion sea seleccionable
            archivo_seleccionado = archivos_respaldo[seleccion - 1]#guarda en variables el archivo seleccionado
            #se guarda la ruta del archivo
            ruta_archivo_seleccionado = os.path.join(carpeta, archivo_seleccionado)
            
            
            # se crea la copia del archivo
            fecha_actual = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
            nombre_copia = f'{os.path.splitext(archivo_seleccionado)[0]}-fueCopiada-{fecha_actual}.json'
            ruta_copia = os.path.join(carpeta, nombre_copia)

            

            try:
                with open(ruta_archivo_seleccionado, 'r') as archivo:
                    data = json.load(archivo)
                if data == {} or data ==[]:
                    print('el archivo se encontro vacio')
                    os.remove(ruta_archivo_seleccionado)
                    print(f'archivo vacio eliminado: {ruta_archivo_seleccionado}')
                else:
                #print(json.dumps(data, indent=4)) }
                     #renombrar el archivo seleccionado
                    # Crear una copia del archivo seleccionado
                    shutil.copy2(ruta_archivo_seleccionado, ruta_copia)
                    print(f'Copia de respaldo creada: {ruta_copia}')
                    nuevo_nombre = "bd.json"
                    ruta_nuevo_archivo = os.path.join("ArchivoDeUso", nuevo_nombre)
                        
                        #para que evitar el error al no poder crear un archivo ya existente
                    if os.path.exists(ruta_nuevo_archivo):
                        os.remove(ruta_nuevo_archivo)
                        
                        #se renombra el archivo
                        os.rename(ruta_archivo_seleccionado, ruta_nuevo_archivo)
                        print(f'Archivo renombrado a: {nuevo_nombre}')
                    else:
                        print('Selección no válida.') 
            except json.JSONDecodeError:
                print('el archivo se encontro vacio')
                os.remove(ruta_archivo_seleccionado)
                print(f'archivo vacio eliminado: {ruta_archivo_seleccionado}')
                

            
           
            
            
               
    


    # metodo que imprime la tabla de los productos cargados de json
    def imprimirTabla(self):
        #os.system("cls")
        tabla = """
+-----------------------PRODUCTOS CARGADOS DESDE ARCHIVO------------------------+
| Codigo   Descripción                       Inventario         Precio de Venta |
+-------------------------------------------------------------------------------+
"""
        for producto in self.get_listaProducto():
            tabla += '| {0:<10} {1:<35} {2:<14} {3:15.2f} |\n'.format(
                producto.get_codigoProducto(),
                producto.get_nombreProducto(),
                producto.get_inventorioProducto(),
                producto.get_precioProducto()
            )
        final = "+-------------------------------------------------------------------------------+"
        tabla = tabla + final
        print(tabla )


    # metodo que es llamado en el menu: carga los archivos del json y los imprimie en pantalla
    #en caso de que se hayan ya cargado una vez los archivos solo imprimira en pantalla
    def cargarArchivoProductos(self):
        if not self.get_listaProducto(): 
            self.cargarDelJson()
            self.imprimirTabla()
        else:
            #print("Ya se han cargado los productos desde el archivo.")
            self.imprimirTabla()


       
    #metodo que se llama en el menu para agregar nuevos productos al menu
    def cargarManualProductos(self):
        os.system("cls")
        if not self.get_listaProducto(): # aseguramos que se hayan cargado ya los datos
            print("Primero carga los productos, antes de agregar un nuevo producto")
            return
        self.imprimirTabla()#imprimimos en pantalla los datos existentes
        while True:
            ciclo= ex.input_con_error("Desea agregar un nuevo producto? (S/N): ").upper()
            if ciclo =="S":
                producto=Producto() #se crea un nuevo objeto producto
                #se asignan los atributos al objeto
                producto.set_codigoProducto(ex.verificacionNumerosSTR("Digite el codigo del producto: "))
                if self.verificarCodigoProducto(producto.get_codigoProducto()) == True:
                  continue
                producto.set_nombreProducto(ex.input_con_error("Digite el nombre: "))
                if self.verificarNombreProducto(producto.get_nombreProducto()) == True:
                  continue
                producto.set_inventorioProducto(ex.solicitar_dato_int("Digite la cantidad del producto: "))
                producto.set_precioProducto(ex.solicitar_dato_float("Digite el Precio del producto: "))
                #Se muestra en pantalla los datos a agregas antes de agregarlos
                print(" Codigo: {0}\n Nombre: {1}\n Inventario: {2}\n Precio: {3}".format(producto.get_codigoProducto(),producto.get_nombreProducto(), producto.get_inventorioProducto(), producto.get_precioProducto()))
                confirmacion = ex.input_con_error("Esta seguro de agregar el nuevo producto:(S/N) ").upper()
                if confirmacion == "S":
                    self.set_listaProductos(producto)# se agregan al menu
                    self.imprimirTabla() 
                    print("El producto ha sido agregado correctamente")
                elif confirmacion == "N":
                    print("Producto descartado")
                else:
                    print("opcion invalida")
                    
            elif ciclo == "N":
                print("Regresando al Menu...")
                break
                    
                
            else:
                print("Digite una opcion valida...")
                continue
    

    #metodo que se llama al menu para eliminar un productos del menu
    def borrarProducto(self):
        os.system("cls")
        if not self.get_listaProducto():# se asegura que los datos hayan sido cargados
            print("No hay productos para borrar.")
            return
        
        self.imprimirTabla() #se muestran en pantalla los datos existentes
        while True:
            ciclo= ex.input_con_error("Desea eliminar un Producto: (S/N)").upper()
            if ciclo== "S":
               self.verificarBorrarProductos()
            elif ciclo =="N":
                print("Regresando al Menu...")
                break
            else:
                print("opcion no valida")


    #elimina un producto segun su indice 
    def eliminar_producto(self, indice):
       del self.__listaProducto[indice]# se debe utilizar "del" para eliminar segun el indice

    
    #metodo que asegura que el producto exista y posteriormente borra el producto
    def verificarBorrarProductos(self,):
        pregunta=ex.verificacionNumerosSTR("Escriba el codigo del Producto que vas a eliminar: ")
        producto_encontrado= None
            #enumate se usa para obtener el indice en la variable i 
        for i, producto in enumerate(self.get_listaProducto()):
                if producto.get_codigoProducto() == pregunta:
                    producto_encontrado = i
                    break
                    
        if producto_encontrado is not None:
            self.eliminar_producto(producto_encontrado)# aqui se elimina el producto
            self.imprimirTabla()
            print(f"Producto con código {pregunta} ha sido eliminado.")
        else:
            print(f"No se encontró ningún producto con el código {pregunta}.")
    
    def nuevosProductos(self):
        print("nose")


    #metodo que verifica que no se repitan los codigos de los productos cuando se crean
    def verificarCodigoProducto(self, codigo):
        for producto in self.get_listaProducto():
            
            if producto.get_codigoProducto() == codigo:
                print("El codigo del Producto ya existe")
                return True


    #metodo que verifica que no se repitan los nombres de los productos cuando se crean
    def verificarNombreProducto(self,nombre):
        for producto in self.get_listaProducto():
            if producto.get_nombreProducto() == nombre:
                print("El nombre del Producto ya existe")
                return True


    #metodo que guarda los cambios realizados en el menu de productos a la base de datos
    def grabarArchivoProductos(self):
        self.ordenar_por_codigo()
        with open('ArchivoDeUso/bd.json', "w") as json_file:
            productos_diccionario = [producto.diccionario() for producto in self.get_listaProducto()]
            json.dump(productos_diccionario,json_file,indent=4 )
        
        
    
    
        

    def existenciaProductos():
        print("nose")
                    
    #metodo que ordena por codigo los productos para guardan en el json 
    #solo se llama en grabarArchivoProductos 
    def ordenar_por_codigo(self):
        self.__listaProducto.sort(key=lambda producto: producto.get_codigoProducto())


    #limpia toda la lista (Accion Peligrosa)
    def limpiarproductos(self):
        self.__listaProducto.clear()



        
        
        
    