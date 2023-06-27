def validar_opcion_menu(arreglo):
    while True:
        try:
            opc = int(input())
            if opc not in range(1, len(arreglo) + 1):
                print("OPCION NO ENCONTRADA!!!")
            else:
                break
        except:
            print("OPCION INVALIDA!!!")
    return opc


def imprimir_menu(arreglo, nombre_menu):
    print("*" * 35)
    print(f"\t {nombre_menu}")
    print("*" * 35)
    for i in range(len(arreglo)):
        print(f"{i + 1}) {arreglo[i]}")
    print("*" * 35)

    return validar_opcion_menu(arreglo)


def validar_rut():
    while True:
        try:
            rut_persona = int(input())
            break
        except:
            print("RUT INGRESADO INVALIDO!!!")
    return rut_persona


def buscar_persona(lista, criterio, campo=None):
    return [persona for persona in lista if campo in persona and str(persona[campo]) == str(criterio)]


menu_principal = ['Grabar', 'Buscar', 'Imprimir parejas', 'SALIR']
menu_categorias = ['Oro', 'Plata', 'Bronce']


while True:
    participantes = []
    # MENU PRINCIPAL
    opcMenuPrincipal = imprimir_menu(menu_principal, "MENU PADEL")
    # Guardar datos de jugadores
    if opcMenuPrincipal == 1:
        while True:
            print("Ingrese su nombre:")
            nombre_participantes = input()
            participantes.append(nombre_participantes)
            print("*" * 35)
            print("Ingrese su RUT:\t(si termina en K ingrese un '0')")
            rut_participante = validar_rut()
            participantes.append(rut_participante)
            print("Ingrese una de las siguinetes opciones del menu")
            opcMenuCategoria = imprimir_menu(menu_categorias, "CATEGORIAS")
            participantes.append(opcMenuCategoria)
            print("Ingrese su TELEFONO:")
            telefono_participante = int(input())
            participantes.append(telefono_participante)
            print("Ingrese su correo:")
            correo_participante = input()
            participantes.append(correo_participante)

            print(participantes)

    # Buscar participantes segun RUT
    elif opcMenuPrincipal == 2:
        print("Ingrese el RUT del parcitipante que desea buscar:(si termina en K ingrese un '0')")
        rut_participante = validar_rut()
        buscar_participante = buscar_persona(
            participantes, rut_participante, campo="Correo")
        for persona in buscar_participante:
            print("Nombre:", persona["Nombre"])
            print("Categoria", persona["Categoria"])
            print("Fono:", persona["Fono"])
            print("Correo:", persona["Correo"])
            print("-" * 30)

    # Buscar participantes por GRUPO
    elif opcMenuPrincipal == 3:
        print("Ingrese el nombre del grupo que desea buscar:")
        nombre_grupo = input().lower
        buscar_integrantes = buscar_persona(
            participantes, nombre_grupo, campo="Grupo")

        print("\t GRUPO")
        print("-" * 30)
        for persona in buscar_integrantes:
            print("Nombre:", persona["Nombre"])
            print("Categoria", persona["Categoria"])
            print("Fono:", persona["Fono"])
            print("Correo:", persona["Correo"])
            print("-" * 30)
