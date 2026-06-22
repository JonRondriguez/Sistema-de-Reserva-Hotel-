import os
import time

reservas = []
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
    return -1
def mostrar_una_reserva(reser):
    print(f"  Código        : {reser['codigo']}")
    print(f"  Nombre        : {reser['nombre']}")
    print(f"  Noches        : {reser['noches']}")
    print(f"  Valor/noche   : ${reser['valor_noche']}")
    print(f"  Total         : ${reser['total']}")
    print(f"  Categoría     : {reser['categoria']}")

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

# Actualizar reserva
def actualizar_reserva():
    print("-------- Actualizar reserva --------")

def mostrar_reservas():

    print("\n=== MOSTRAR RESERVAS ===")

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return
    
    for mostrar in range(len(reservas)):

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
        print(f"[Posición {mostrar}]")

        mostrar_reservas(reservas[mostrar])

main()

def mostrar_menu():
    
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
