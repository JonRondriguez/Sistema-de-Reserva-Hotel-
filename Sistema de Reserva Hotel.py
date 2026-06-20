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

def cantidad_noches(cant_noches):
    if cant_noches <= 0:
        return None
    
def calculo_por_noche(calculo):
    validar_total = cantidad_noches * valor_noche

def validar_total(total):

    if total < 200000:
        return "Economica"

    elif total > 200000 and total < 500000:
        return "Estandar"

    elif total > 500000:
        return "Premium"

def existe_codigo(reservas, codigo):
    for reserva in reservas:
        if reserva["codigo"] == codigo:
            return reserva
    return None



#------------MENU PRINCIPAL----------|

# Registrar reserva

def registrar_reserva(reservas):
    
    try:
        codigo = input("Ingresa el código de la reserva: ").upper()

        #Validar código
        if  not validacion_codigo(codigo):
            print("Error: El código no puede estar vacío")
            return

        #¿Código ya existe?
        if existe_codigo(reservas, codigo) is not None:
            print("El código de la reserva ingresado, ya existe.")
            return

        nombre = input("Ingresa el nombre del huésped: ")

        if not validacion_nombre(nombre):
            print("El nombre del huésped no puede estar vacío.")
            return
        
        try:
            input_noches = int(input("Ingresa la cantidad de noches a alojar: "))

            if cantidad_noches(input_noches) is None:
                print("Ingresa un valor mayor a 0 para realizar la reserva.")
                return
            
            input_valor = int(input("Ingresa el valor por noche de la reserva: "))

            if valor_noche(input_noches) is None:
                print("Ingresa un monto mayor a 0 para reservar.")
                return
            
        except:
            print("Error: Debes ingresar un valor numérico entero para reservar.")
            return
        
        total = calculo_por_noche(input_noches, input_valor)

        categoria = validar_total(total)

        reservas = [{"codigo": codigo,
                     "nombre": nombre,
                     "noches": input_noches,
                     "valor": input_valor,
                     "total": total,
                     "categoria": categoria}]


    except ValueError as e:
        print(f"Error: {e}")