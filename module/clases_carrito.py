""" 
CBA
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 05/07/2024

"""
"""aqui se encuentran las clases relacionadas al carrito"""
import json
import os
from module import excepciones as ex

#clase para los productos que se vayan a comprar
class ProductoCarrito():
    def __init__(self,codigoProducto='',nombreProducto='',inventorioProducto=0,precioProducto=0.00, subTotalProducto=0.00,):
        self.__codigoProducto = str(codigoProducto)
        self.__nombreProducto = str( nombreProducto)
        self.__inventorioProducto = int(inventorioProducto)
        self.__precioProducto = float(precioProducto)
        self.__subTotalProducto = float(subTotalProducto)

    #getter y setter
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

    
    def set_subTotalProducto(self):
        self.__subTotalProducto= self.get_inventorioProducto()* self.get_precioProducto()



    def get_subTotalProducto(self):
        return self.__subTotalProducto
    
    #metodos de la clase ProductoCarrito
    
    def digitarDato(self,mensaje):
        print("falta desarrollar")


    
    #verifica que el codigo si exista
    def datoCodigoProducto(self, codigo):
        for producto in self.get_listaProducto():
            if producto.get_codigoProducto() == codigo:
                return True
        return False

    
    

    
#clase carritoCompra tendran los datos del cliente y los productos que va a comprar
class CarritoCompra():
    def __init__(self, documentoCliente='', nombreCliente='', direccionCliente='', productosCarrito=None) :
        self.__documentoCliente = str(documentoCliente)
        self.__nombreCliente = str(nombreCliente)
        self.__direccionCliente = str(direccionCliente)
        # Inicializar productosCarrito como una lista vacía si no se proporciona ninguna
        if productosCarrito is None:
            productosCarrito = []
        self.__productosCarrito = productosCarrito

    # Getters y setters para los atributos del cliente
    def get_documentoCliente(self):
        return self.__documentoCliente

    def set_documentoCliente(self, value):
        self.__documentoCliente = str(value)

    def get_nombreCliente(self):
        return self.__nombreCliente

    def set_nombreCliente(self, value):
        self.__nombreCliente = str(value)

    def get_direccionCliente(self):
        return self.__direccionCliente

    def set_direccionCliente(self, value):
        self.__direccionCliente = str(value)

    # Getters y setters para productosCarrito
    def get_productosCarrito(self):
        return self.__productosCarrito

    def agregarProductoCarrito(self, producto):
        self.__productosCarrito.append(producto)


    #metodos de la clase (cliente)
    def digitarDato(self):
        print("en proceso")

    #socilita el documento del cliente
    def documentoCliente(self):
        documento= ex.verificacionNumerosSTR("digite su Documento: ")
        self.set_documentoCliente(documento)

    #socilita el nombre del cliente
    def nombreCliente(self):
        nombre= ex.input_con_error("digite su Nombre: ")
        self.set_nombreCliente(nombre)

    #socilita la dirrecion del cliente
    def dirrecionCliente(self):
        dirrecion= ex.input_con_error("digite su Dirrecion: ")
        self.set_direccionCliente(dirrecion) 

#METODOS (CARRITO DE COMPRAS)

    #metodo movido a esta clase
    #Verifica que el codigo del producto exista para realizar la compra
    def verificarCodigoProducto(self, codigo, lista):
        for producto in lista.get_listaProducto():
            if producto.get_codigoProducto() == codigo:
                return True
        print("No se encuentra el Codigo del Producto")


    #metodo trasladado a esta clase
    #verifica que la compra no sobrepase las cantidad existente el en inventario
    def datoCantidadProducto(self, codigo, cantidad, lista):
        #buscamos el codigo en la lista
        for producto in lista.get_listaProducto():
            if producto.get_codigoProducto() == codigo:
                #verificamos que la cantidad del pedido no supere el inventario existente
                if not producto.get_inventorioProducto() >= cantidad: 
                    print("Su pedido supera nuestro inventario")
                    os.system('pause')
                else :
                    return True
                    

    
    #movi este metodo a esta clase
    #imprime los datos del carrito que lleven al momento 
    def datosCompra(self):
        tabla = """
+----------------------------------CARRITO DE COMPRA-------------------------------------------------+
| Codigo   Descripción                       Cantidad           Valor Unitario              Subtotal |
+----------------------------------------------------------------------------------------------------+
"""
        for producto in self.get_productosCarrito():
            tabla += '| {0:<10} {1:<35} {2:<10} {3:12.2f}{4:28.2f} |\n'.format(
                producto.get_codigoProducto(),
                producto.get_nombreProducto(),
                producto.get_inventorioProducto(),
                producto.get_precioProducto(),
                producto.get_subTotalProducto()
            )
        total = self.calcularValorCompra()
        final =f"+----------------------------------------------------------------------------------------------------+\n|Total = {total}                                                       |\n+----------------------------------------------------------------------------------------------------+"
       # f"|Total = {total}                                                       |\n"
        # "+------------------------------------------------------------------------+"  
        tabla += final 
        print(tabla)


    #movi este metodo a esta clase
    #metodo que realiza la suma total del costo de todos los productos
    def calcularValorCompra(self):
        total= 0
        for producto in self.get_productosCarrito():
            total = total + producto.get_subTotalProducto()
        return total
    

    #como parametro se espera la lista que contiene los productos
    #la "entrada" en el input del codigo 
    #el inventario es la cantidad
    #crea y agrega el el producto al carrito de productos
    def nuevoProducto(self,entrada,inventario, listaProductos):
        if not listaProductos.get_listaProducto():
            print("NO SE HAN CARGADO LOS PRODUCTOS")
            return
        for objeto in listaProductos.get_listaProducto():
            if objeto.get_codigoProducto() == entrada:
                producto = ProductoCarrito()
                producto.set_codigoProducto(objeto.get_codigoProducto())
                producto.set_nombreProducto(objeto.get_nombreProducto())
                producto.set_inventorioProducto(inventario)
                producto.set_precioProducto(objeto.get_precioProducto())
                producto.set_subTotalProducto()
                self.agregarProductoCarrito(producto)
                self.datosCompra()
                print("se ha agregado el producto al Carrito")
                
                for i in listaProductos.get_listaProducto():
                    if i.get_codigoProducto() == producto.get_codigoProducto():
                        nuevo_inventario = i.get_inventorioProducto() - producto.get_inventorioProducto()
                        i.set_inventorioProducto(nuevo_inventario)
        

        


    #como parametro la lista de productos
    #realiza la compra y genera la factura
    def facturaCompra(self, listaProductos):
        if not self.get_productosCarrito(): #se asegura que exista algo para comprar
            print("NO HAY PRODUCTOS EN EL CARRITO")
            return
        self.datosCompra()
        confirmacion = ex.input_con_error("¿Está Seguro de Realizar la compra? (S/N): ").upper()
        if confirmacion != "S":
            print("Compra cancelada.")
            return
        #solicita los datos del cliente
        self.documentoCliente()
        self.nombreCliente()
        self.dirrecionCliente()
        #imprime la factura
        print("\n+----------------------- FACTURA DE COMPRA -----------------------+")
        print(f"Documento del Cliente: {self.get_documentoCliente()}")
        print(f"Nombre del Cliente: {self.get_nombreCliente()}")
        print(f"Dirección del Cliente: {self.get_direccionCliente()}")
        print("+----------------------------------------------------------------+\n")

        self.datosCompra()
        #final= self.calcularValorCompra()
        #print(f"Total es :{final}")
        # Actualizar inventario de productos en la lista principal quitando la cantidad que se va a comprar
        
        #en pruebas
        """for producto_carrito in self.get_productosCarrito():
            for producto in listaProductos.get_listaProducto():
                if producto.get_codigoProducto() == producto_carrito.get_codigoProducto():
                    nuevo_inventario = producto.get_inventorioProducto() - producto_carrito.get_inventorioProducto()
                    producto.set_inventorioProducto(nuevo_inventario) """
        

        # Guardar cambios en el archivo JSON
        self.limpiarproductos()
        listaProductos.grabarArchivoProductos()
        print("El inventario ha sido actualizado y la factura ha sido generada.")

    #metodo que elimina del carrito de comprar segun el indice
    def eliminar_Producto(self,indice):
        del self.__productosCarrito[indice]

    #verifica que el producto escrito exista en el carrito para borrar
    def verificarBorrarProducto(self,listaProductos):
        pregunta= ex.verificacionNumerosSTR("digite el codigo del carritto que vas a eliminar: ")
        producto_encontrado= None
        #enumerate para sacar el indice del producto y guardarlo en la variable i 
        for i, productoC in enumerate(self.get_productosCarrito()):
                if productoC.get_codigoProducto()== pregunta:
                    producto_encontrado= i
                    for x in listaProductos.get_listaProducto():
                        if x.get_codigoProducto() == productoC.get_codigoProducto():
                            nuevo_inventario = x.get_inventorioProducto() + productoC.get_inventorioProducto()
                            x.set_inventorioProducto(nuevo_inventario)
                    break
        if producto_encontrado is not None: # se borra el producto 
            self.eliminar_Producto(producto_encontrado)
            self.datosCompra()
            
        



    #metodo que se llama al menu para borrar un producto del carrito
    def borrarProducto(self,lista):
        if not self.get_productosCarrito():
            print("NO HAY PRODUCTOS PARA BORRAR")
            return
        while True:
            ciclo= ex.input_con_error("Desea eliminar un Producto: (S/N)").upper()
            if ciclo== "S":
               self.verificarBorrarProducto(lista)
               print("el Producto ha sido borrado")
            elif ciclo =="N":
                print("Regresando al Menu...")
                break
            else:
                print("opcion no valida")
                

    def limpiarproductos(self):
        self.__productosCarrito.clear()
        
