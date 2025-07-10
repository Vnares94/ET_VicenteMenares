# Declaración de variables
op = ''
encontrados = []
marca_encontrada = ''
stock_total = 0
p_min = 0
p_max = 0
chequeo_precios = True
modelo = ''
nuevo_precio = 0
sw_actualizacion = True
lista_marca_producto = []


# Diccionarios

# 
productos = {  
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],

}

# 
stock = {
    '8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1], 'fgdxFHD': [424990, 1],
}


# Funciones
def  mostrar_menu():    
    print('\n*** MENU PRINCIPAL ***')
    print('1. Stock marca.')
    print('2. Búsqueda por precio.')
    print('3. Actualizar precio.')
    print('4. Salir.')


def stock_marca(marca_ingresada): 
    encontrados.clear()
    stock_total = 0
    for producto in productos:
        if marca_ingresada == productos[producto][0].lower():
            encontrados.append(producto)
            marca_encontrada = productos[producto][0]
    if len(encontrados) == 0:
        print(f"No se han encontrado productos con la búsqueda '{marca_ingresada}'")
    else:
        print(f"Con la búsqueda '{marca_ingresada}' se han encontrado los siguientes productos:")
        for i, producto in enumerate(encontrados):
            print(f"{i+1}.- Nombre del producto: {producto}. Stock disponible: {stock[producto][1]}")
            stock_total += stock[producto][1]
        
        print(f"El stock total de la marca {marca_encontrada} es: {stock_total} productos.")

def busqueda_precio(p_min, p_max): # Función para buscar productos dentro de un rango de precios
    encontrados.clear()
    lista_marca_producto.clear()
    for producto in stock:
        if stock[producto][0] >= p_min and stock[producto][0] <= p_max:
            encontrados.append(producto)
    if len(encontrados) == 0:
        print(f"No se han encontrado productos en el rango de precio ${p_min} - ${p_max}")
    else:
        print(f"En el rango de precio ${p_min} - ${p_max} se han encontrado los siguientes productos:")

    for modelo in encontrados:
        lista_marca_producto.append(f"{productos[modelo][0]}--{modelo}")
    lista_marca_producto.sort()
    print(lista_marca_producto)


def actualizar_precio(modelo, p):
    for producto in stock:
        if modelo == producto:
            stock[producto][0] = p
            return True
    return False


# Ejecución del código
while True:
    try:
        mostrar_menu()
        op = input("Ingrese una opción: ")

        if op == '1': 
            marca_ingresada = input("Ingrese la marca sobre la cual desea revisar el stock: ").strip()
            marca_ingresada = marca_ingresada.lower()
            stock_marca(marca_ingresada)

        elif op == '2': 
            chequeo_precios = True
            while chequeo_precios:
                try:
                    while True:
                        p_min = int(input("Ingrese el precio mínimo que desea buscar: "))
                        if p_min <= 0:
                            print("¡Debe ingresar valores enteros!")
                        else:
                            break
                    while True:
                        p_max = int(input("Ingrese el precio máximo que desea buscar: "))
                        if p_max <= 0:
                            print("¡Debe ingresar valores enteros!")
                        elif p_max <= p_min:
                            print("El precio máximo debe ser superior al precio mínimo!")
                        else:
                            chequeo_precios = False
                            break
                except ValueError:
                    print("¡Debe ingresar números enteros!")
            busqueda_precio(p_min, p_max)

        elif op == '3': 
            sw_actualizacion = True
            while sw_actualizacion:
                modelo = input("Ingrese el modelo: ").strip()
                while True:
                    try:
                        nuevo_precio = int(input("Ingrese el precio nuevo: "))
                        if nuevo_precio <= 0:
                            print("¡Debe ingresar valores enteros!")
                        else:
                            break
                    except ValueError:
                        print("¡Debe ingresar números enteros!")
                if actualizar_precio(modelo, nuevo_precio):
                    print(f"¡El precio del modelo {modelo} se ha actualizado!")
                else:
                    print(f"¡El modelo no existe!")

                while True:
                    op = input("¿Desea actualizar el precio de otro notebook? Ingrese Sí o No: ").lower()
                    if op in ["si", "s", "sí"]:
                        break
                    elif op in ["no", "n"]:
                        sw_actualizacion = False
                        break
                    else:
                        print("Ingrese una opción válida: Sí o no.")

        elif op == '4': # Salir
            print("Programa finalizado.")
            break

        else: 
            print("¡¡Debe seleccionar una opción válida!!")


    except Exception as e:
        print(f"Error imprevisto: {e}")