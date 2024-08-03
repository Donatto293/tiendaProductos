""" 
CBA
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 05/07/2024

"""
"""manejo de excepciones"""
import os

#control del ctrl + c
#(aun no se como funciona a la perfeccion)
def catch_keyboard_interrupt(func):
    def wrapper(*args, **kwargs):# *args para cualquier cantidad de parametros y **kwargs para argumentos con nombre
        while True:
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                print("\nInterrupción con Ctrl+C deshabilitada.")
                continue
            except EOFError:#tuve que ponerle que no se detuviera con esta excepcion porque igual prevenia el ctrl + c se detenia el codigo
                print("\nInterrupción de entrada detectada.")
                continue
    return wrapper


#verificacion de input con control del ctrl +c
@catch_keyboard_interrupt
def input_con_error(prompt):
    return input(prompt)
    

    
#verificacion de solo caracteres alfabeticos
@catch_keyboard_interrupt #decoracion para controlar ctrl+ c
def verificacionTexto(mensaje):
    while True:
            texto=input(mensaje)
            if texto.replace(" ","").isalpha():
                return texto
            else:
                print("digite solo caracteres  alfabeticos")
    


#verifica la entrada de numeros int pero los convierte el STR 
@catch_keyboard_interrupt           
def verificacionNumerosSTR(mensaje):
    while True:
        try:
            texto=int(input(mensaje))
            texto=str(texto)
            if texto.isdigit():
                texto=str(texto)
                return texto
        except ValueError:
                print("digite solo caracteres  numericos")
    

#asegura la entrada de numeros floats 
@catch_keyboard_interrupt              
def solicitar_dato_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError: 
            print("Error: El valor ingresado no es un número válido. Inténtelo de nuevo.")


#asegura la entrada de numeros int 
@catch_keyboard_interrupt
def solicitar_dato_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError: 
            print("Error: El valor ingresado no es un número válido. Inténtelo de nuevo.")
            