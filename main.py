#Ejercicio de manejo de elementos en funcion dict()

agenda_telefonica = dict()

def imprimir_operacion(nombre_operacion):
    print()
    print("-------- Agenda telefónica --------")
    print(nombre_operacion)
    print("-----------------------------------")
    print()


def agregar_contacto():
    contacto = input("Nombre del nuevo contacto: ")
    numero = input("Número del nuevo contacto: ")
    agenda_telefonica[contacto] = numero

    imprimir_operacion(contacto + " agregado con el número " + numero + ".")


def remover_contacto():
    contacto = input("Nombre del contacto que deseas borrar: ")
    try:
        del agenda_telefonica[contacto]
    except KeyError:
        imprimir_operacion(contacto + " no existe.")
    else:
        imprimir_operacion(contacto + " borrado.")


def actualizar_contacto():
    contacto = input("Nombre del contacto que desea actualizar: ")
    numero = input("Nuevo número de " + contacto + ": ")

    agenda_telefonica[contacto] = numero
    imprimir_operacion(contacto + " actualizado a: " + numero)


def ver_contacto():
    contacto = input("Nombre del contacto: ")
    try:
        imprimir_operacion("{} - {}".format(contacto, agenda_telefonica[contacto]))
    except KeyError:
        imprimir_operacion(contacto + " no existe.")


def ver_todo():
    nombre_operacion = None

    if len(agenda_telefonica) == 0:
        nombre_operacion("No hay ningún contacto.")
    else:
        for contacto in agenda_telefonica:
            if nombre_operacion == None:
                nombre_operacion = "{} - {}".format(contacto, agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n{} - {}".format(contacto, agenda_telefonica[contacto])

    imprimir_operacion(nombre_operacion)

print("**** Bienvenido a la Agenda Telefónica de Enrique ****")

while True:
    print("1 - Agregar un contacto")
    print("2 - Remover un contacto")
    print("3 - Actualizar un contacto")
    print("4 - Ver un contacto")
    print("5 - Ver todos los contactos")
    print("6 - Salir")
    print()
    try:
        operacion = int(input(": "))
    except ValueError:
        print()
        print ("Selecciona un número del 1 al 6.")
        print()
    else:
        if operacion == 1:
            agregar_contacto()
        elif operacion == 2:
            remover_contacto()
        elif operacion == 3:
            actualizar_contacto()
        elif operacion == 4:
            ver_contacto()
        elif operacion == 5:
            ver_todo()
        elif operacion == 6:
            break
        else:
            print ("Operación desconocida")

print()
print("Gracias por usar nuestra Agenda Telefónica")
print("¡Vuelva Pronto!")
