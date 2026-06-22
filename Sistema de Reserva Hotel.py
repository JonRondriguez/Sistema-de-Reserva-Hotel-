
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


def mostrar_reservas():

    print("\n=== MOSTRAR RESERVAS ===")

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return
    
    for mostrar in range(len(reservas)):

        print(f"[Posición {mostrar}]")

        mostrar_reservas(reservas[mostrar])


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
