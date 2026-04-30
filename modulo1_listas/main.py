# Definir inventario con tres productos [nombre, cantidad, precio]
inventario = [
    ["manzana", 50, 1.5],
    ["pan", 30, 2.0],
    ["leche", 20, 3.2]
]

# Definir actualizar_precio(producto, nuevo_precio)
def actualizar_precio(producto, nuevo_precio):
    for item in inventario:
        if item[0] == producto:
            item[2] = nuevo_precio

# Definir registrar_venta(producto, cantidad)
def registrar_venta(producto, cantidad):
    for item in inventario:
        if item[0] == producto:
            if item[1] >= cantidad:
                item[1] = item[1] - cantidad
            else:
                print("No hay suficiente stock de", producto)

# Definir anadir_producto(producto, cantidad, precio)
def anadir_producto(producto, cantidad, precio):
    for item in inventario:
        if item[0] == producto:
            item[1] = item[1] + cantidad
            return
    inventario.append([producto, cantidad, precio])

# Definir mostrar_inventario()
def mostrar_inventario():
    print("Inventario actual:")
    for item in inventario:
        print("Producto:", item[0], "| Cantidad:", item[1], "| Precio:", item[2])

# Llamar a actualizar_precio con el segundo producto
actualizar_precio("pan", 2.5)

# Llamar a registrar_venta con el primer producto
registrar_venta("manzana", 10)

# Llamar a anadir_producto con un producto nuevo
anadir_producto("huevos", 40, 0.5)

# Llamar a mostrar_inventario
mostrar_inventario()