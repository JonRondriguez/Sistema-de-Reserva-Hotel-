import os
import time


#------------VALIDACIONES---------------|

def validacion_codigo(codigo):
    return codigo.strip() != ""

def validacion_nombre(nombre):
    return nombre.strip() != ""

def valor_noche(valor_noche):
    if valor_noche <= 0:
        return None

def cantidad_noches(cat_noches):
    if cat_noches <= 0:
        return None
    
def calculo_por_noche(calculo):
    total = cantidad_noches * valor_noche

def validar_total(total, categoria):

    if total < 200000:
        return "Economica"

    elif total > 200000 and total < 500000:
        return "Estandar"

    elif total > 500000:
        return "Premium"

def buscar_reserva(reservas, codigo):    
    for reserva in reservas:
        if reserva["codigo"] == codigo:
            return reserva
        return None


#------------------BUSCAR RESERVA-----------------------|

def buscar_reserva(reservas, codigo):
    print("\n===== BUSQUEDA DE RESERVA =====")

    try:
        codigo = input("Ingrese codigo de reserva: ")

        #Validar código
        if not validacion_codigo:
            print("Error: Debe ingresar el codigo para verificar su reserva")
            return
    except ValueError:
        print("Error: , ")


def eliminar_reserva(eliminar):
    print("\n==== ELIMINAR RESERVA ===")

    try:
        codigo = input("Ingrese código a eliminar: ").strip()
        buscar = buscar_reserva(codigo)

        if buscar == -1:
            print("No se encontró ninguna reserva con ese código.")
            return
            reserva.pop(buscar) 
        print(f" Reserva '{codigo}' eliminada.")
        
    except ValueError:
        print("Error: Debe ingresar un codigo valido")


 



