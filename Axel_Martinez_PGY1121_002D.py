import os 
os.system("cls")

productos = []


def registrar_producto():
    try:
        codigo = input("Ingrese el código numérico de 6 dígitos: ")
        while len(codigo) != 6 or not codigo.isdigit():
            print("El código debe tener exactamente 6 dígitos numéricos.")
            codigo = input("Ingrese el código numérico de 6 dígitos: ")

        nombre = input("Ingrese el nombre del producto: ")
        while len(nombre) < 2 or len(nombre) > 50:
            print("El nombre debe tener entre 2 y 50 caracteres.")
            nombre = input("Ingrese el nombre del producto: ")

        categoria = input("Ingrese la categoría del producto: ")

        precio = float(input("Ingrese el precio del producto: "))
        while precio <= 0:
            print("El precio debe ser mayor que cero.")
            precio = float(input("Ingrese el precio del producto: "))

        stock = int(input("Ingrese la cantidad disponible en stock: "))
        while stock < 0:
            print("La cantidad disponible debe ser un número entero positivo.")
            stock = int(input("Ingrese la cantidad disponible en stock: "))


        productos.append({"codigo": codigo, "nombre": nombre, "categoria": categoria, "precio": precio, "stock": stock})
        print("Producto registrado con éxito.")
    except ValueError:
        print("Error: Se ha ingresado un valor no válido.")


def buscar_producto():
    try:
        categoria = input("Ingrese la categoría del producto a buscar: ")
        found = False

        print("Productos encontrados en la categoría '{}':".format(categoria))
        for producto in productos:
            if producto["categoria"] == categoria:
                print("Código: {}".format(producto["codigo"]))
                print("Nombre: {}".format(producto["nombre"]))
                print("Precio: {}".format(producto["precio"]))
                print("Stock: {}".format(producto["stock"]))
                print("-----------------------------------")
                found = True

        if not found:
            print("No se encontraron productos en la categoría '{}'.\n".format(categoria))
    except:
        print("Error: Se produjo un error al buscar productos.")


def listar_productos():
    try:
        print("Lista de productos:")
        print("{:<10} {:<20} {:<15} {:<10} {:<10}".format("Código", "Nombre", "Categoría", "Precio", "Stock"))
        print("-----------------------------------------------")
        for producto in productos:
            print("{:<10} {:<20} {:<15} {:<10} {:<10}".format(producto["codigo"], producto["nombre"], producto["categoria"], producto["precio"], producto["stock"]))
    except:
        print("Error: Se produjo un error al listar los productos.")


def main():
    try:
        print("Bienvenido a SuperStore")
        print("Sistema de gestión de venta de productos")
        print("-----------------------------------------")

        while True:
            print("\nMenú:")
            print("1. Registrar producto")
            print("2. Buscar producto por categoría")
            print("3. Listar productos")
            print("4. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                registrar_producto()
            elif opcion == "2":
                buscar_producto()
            elif opcion == "3":
                listar_productos()
            elif opcion == "4":
                print("¡Gracias por usar el programa!")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
    except:
        print("Error: Se produjo un error en la ejecución del programa.")


main()