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
    validar_total = cantidad_noches * valor_noche

def validar_total(total, categoria):

    if total < 200000:
        categoria = "Economica"

    elif total > 200000 and total < 500000:
        categoria = "Estandar"

    elif total > 500000:
        categoria = "Premium"


#----------------------------MENU PRINCIPAL-------------------------------|
    print("\t\t-----------------------")
    print("\t\t|> MENU DE OPCIONES  <|")
    print("\t\t-----------------------")


    print("\t---------------------------------------------")
    print("\t|     N°                DESCRIPCION         |")
    print("\t---------------------------------------------")
    print(f"\t|    1.-             Registrar reserva     |")
    print("\t---------------------------------------------")
    print(f"\t|    2.-             Buscar reserva        |")
    print("\t---------------------------------------------")
    print(f"\t|    3.-             Actualizar reserva    |")
    print("\t---------------------------------------------")
    print(f"\t|    4.-             Eliminar reserva      |")
    print("\t---------------------------------------------")
    print(f"\t|    5.-             Mostrar reservas      |")
    print("\t---------------------------------------------")
    print(f"\t|    6.-             Mostrar estadísticas  |")
    print("\t---------------------------------------------")
    print(f"\t|    7.-                   Salir           |")
    print("\t---------------------------------------------")
    print("")





 



