# Productos y sus precios correspondientes
productos = {
    "Pan ciabatta": 2000,
    "Pie de Limon": 3500,
    "Cafe": 2200,
    "Te": 1600,
    "Alfajor": 1000
}

# Solicitar al usuario la cantidad vendida de cada producto
ventas_diarias = {}
total_ventas = 0

print("Ingrese la cantidad vendida de cada producto durante el día:")

for producto, precio in productos.items():
    cantidad = int(input(f"Cantidad de {producto}: "))
    total_producto = cantidad * precio
    ventas_diarias[producto] = total_producto
    total_ventas += total_producto

# Imprimir el informe de ventas en la consola
print("\nInforme de ventas:")
for producto, total_producto in ventas_diarias.items():
    print(f"{producto}: ${total_producto}")

print(f"\nTotal de ventas del día: ${total_ventas}")

# Guardar el informe de ventas en un archivo de texto
with open("informe_ventas.txt", "w") as archivo:
    archivo.write("Informe de ventas:\n")
    for producto, total_producto in ventas_diarias.items():
        archivo.write(f"{producto}: ${total_producto}\n")
    archivo.write(f"\nTotal de ventas del día: ${total_ventas}")
