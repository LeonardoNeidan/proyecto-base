from clases.operaciones import Operaciones

def main():
    op = Operaciones()
    op.leerNumeros()

    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Módulo")

    opcion = input("Ingrese el número de la operación: ")

    if opcion == "1":
        op.sumar()
    elif opcion == "2":
        op.restar()
    elif opcion == "3":
        op.multiplicar()
    elif opcion == "4":
        op.dividir()
    elif opcion == "5":
        op.modulo()
    else:
        print("Opción inválida")

    op.mostrarResultado()
    
if __name__ == "__main__":
    main()
