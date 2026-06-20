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


#------------MENU PRINCIPAL----------|






