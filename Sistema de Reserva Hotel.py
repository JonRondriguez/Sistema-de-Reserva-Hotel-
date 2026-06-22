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
    
def calculo_por_noche(cantidad_noches, valor_noche):
    return cantidad_noches * valor_noche

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

def buscar_reserva(reservas, codigo):
    for reserva in reservas:
        if reserva["codigo"] == codigo:
            return reserva
    return None





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

            if cantidad_noches(input_noches) is not None:
                print("Ingresa un valor mayor a 0 para realizar la reserva.")
                return
            
            input_valor = int(input("Ingresa el valor por noche de la reserva: "))

            if valor_noche(input_valor) is not None:
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
        print(reservas)



    except ValueError as e:
        print(f"Error: {e}")



# Actualizar reserva
def actualizar_reserva():
    print("-------- Actualizar reserva --------")

    codigo = input("Ingresa el código de la reserva a buscar: ").strip()

    reserva = buscar_reserva(codigo)

    if reserva is None:
        print("El codigo ingresado, no se encuentra registrado.")
        return

    elif reserva is not None:
        print("--- Reserva encontrada ---")
        print(f'''
                ----------------------------------------
                "Código"        : {reserva["codigo"]}
                "Nombre"        : {reserva["nombre"]}
                "Cantidad noches: {reserva["noches"]}
                "Valor por noche: {reserva["valor"]}
                "Total reserva  : {reserva["total"]}
                "Categoría"     : {reserva["categoria"]}
                ----------------------------------------\n
              ''')
        
        print("¿Qué deseas modificar?")
        print("1.- Nombre Huésped")
        print("2.- Cantidad Noches")
        print("3.- Valor por noche")

        try:
            opcion = int(input("Ingresa un valor del menú: "))

            if opcion == 1: #Cambiar nocmbre
                nuevo_nombre = input("Ingresa el nuevo nombre del huésped: ")

                if not validacion_nombre(nuevo_nombre):
                    print("El nuevo nombre no puede estar vacío.")
                    return
                
                reserva["nombre"] = nuevo_nombre
            
            elif opcion == 2: #Cambiar Cantidad noches
                nueva_cantidad_noches = int(input("Ingresa la cantidad de días a reservar: "))

                if not cantidad_noches(nueva_cantidad_noches):
                    print("La cantidad de noches, debe ser mayor a 0.")
                    return
                
                reserva["noches"] = nueva_cantidad_noches

            elif opcion == 3: #Cambiar Valor noche
                nuevo_valor = int(input("Ingresa un nuevo valor por noche: "))

                if not valor_noche(nuevo_valor):
                    print("El valor por noche, debe ser mayor a 0")
                    return
                
                reserva["valor"] = nuevo_valor
            
            else:
                raise ValueError("Ingresa una opción válida")

        except ValueError as e:
            print("Error: {e}")

        nuevo_total = calculo_por_noche(nueva_cantidad_noches, nuevo_valor)

        reserva["total"] = nuevo_total

        print("--- Reserva Actualizada ---")
        print(f'''
                ----------------------------------------
                "Código"        : {reserva["codigo"]}
                "Nombre"        : {reserva["nombre"]}
                "Cantidad noches: {reserva["noches"]}
                "Valor por noche: {reserva["valor"]}
                "Total reserva  : {reserva["total"]}
                "Categoría"     : {reserva["categoria"]}
                ----------------------------------------\n
              ''')                 


# Mostrar estadísticas

def mostrar_estadisticas(reservas):

    cantidad_reservas = len(reservas)
    suma_reservas = sum(reservas["total"])
    promedio_reservas = (suma_reservas / cantidad_reservas)

    if len(reservas) == 0:
        print("Aún no hay reservas registradas")

    print("--------------- ESTADISTICAS DEL PROGRAMA -----------------")
    print(f"Cantidad de reservas                : {cantidad_reservas}")
    print(f"Ingresos totales                    : {suma_reservas}")
    print(f"Reserva de mayor valor              : {max(reservas["total"])}")
    print(f"Promedio de ingresos por reserva    : {promedio_reservas}")



#Leer opción

def leer_opcion():
    try:
        op_menu = int(input("Ingresa una opción del menú para continuar: "))

        if op_menu >= 1 or op_menu <=7:
            return op_menu
        else:
            print("Opción fuera de rango.")
            return 0
    
    except:
        print("Opción inválida. Ingresa un valor numérico del menú para continuar")
        return 0




# Programa principal

def main():
    reservas = []

    while True:
        mostrar_menu()

        op_menu = leer_opcion()

        if op_menu == 1:
            registrar_reserva(reservas)
        elif op_menu == 2:
            buscar_reserva(reservas)
        elif op_menu == 3:
            actualizar_reserva(reservas)
        elif op_menu == 4:
            eliminar(reservas)
        elif op_menu == 5:
            mostrar_reservas(reservas)
        elif op_menu == 6:
            mostrar_estadisticas(reservas)
        elif op_menu == 7:
            print("Saliendo del sistema. . .")
            break


main()

