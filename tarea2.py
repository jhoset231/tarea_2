# PRACTICA NRO 2
#  DEFINA EL SIGUIENTE DICCIONARIO "VENTAS "
ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

# 1. CREA UN MENU ITERACTIVO QUE CUENTE CON LOS SIGUIENTES OPCIONES
def MenU():
    print("El menu de opciones es el siguiente: ")
    print("\n--- Menú de Ventas ---")
    print("1. Mostrar el listado de ventas")
    print("2. Añadir un producto")
    print("3. Calcular la suma total de las ventas")
    print("4. Calcular el promedio de ventas")
    print("5. Mostrar el producto con más unidades vendidas")
    print("6. Mostrar el listado de productos")
    print("7. Salir")
    
    opcion=input("SELECCIONE UNA OPCION: ")
    if opcion=="1":
        Mostrar_lista_Ventas()
    elif opcion=="2":
        New_Producto()
    elif opcion=="3":
        Sumas_Total_venta()
    elif opcion=="4":
        Promedio_Ventas()
    elif opcion=="5":
        Mas_Vendidos()
    elif opcion=="6":
        Productos()
    elif opcion=="7":
        print("Vuelva pronto")
    else:
        print("Opcion no valida") 

# 2. Mostrar el listado de ventas => puedes usar print(f"")
def Mostrar_lista_Ventas():
    for venta in ventas:
        print(f"Fecha: {venta["fecha"]}, Producto: {venta["producto"]}, Cantidad: {venta["cantidad"]}, Precio: {venta["precio"]}, Promocion: {venta["promocion"]}")

# 3. Añadir un producto
def New_Producto():
    fecha=input("Ingresar nueva fecha (dd-mm-aaaa): ")
    producto=input("Ingresar producto (Producto_Letra): ")
    cantidad=input("Ingresar la cantidad: ")
    precio=float(input("Ingresar precio: "))
    promocion=input("¿Esta en promocion?si/no: ").strip().lower()=="si"
    nuevo=[
        {
            "fecha":fecha,
            "producto":producto,
            "cantidad":cantidad,
            "precio":precio,
            "promocion":promocion
        }
    ]
    ventas.append(nuevo)
    print("Producto añadido de manera satisfactoria")
    print("Las ventas son: ",ventas)

# 4. Calcular la suma total de las ventas
def Sumas_Total_venta ():
    suma=0
    for venta in ventas:
        suma+=venta["cantidad"]*venta["precio"]
    print("La suma de las ventas es ",suma)

# 5. Calcular el promedio de ventas
def Promedio_Ventas():
    suma=0
    contador=0
    for venta in ventas:
        suma+=venta["cantidad"]*venta["precio"]
        contador+=1
    if contador>0:
        print("El promedio es: ", suma/contador)
    else:
        print("No hay ventas realizadas")
        
# 6. Mostar el producto mas unidades vendidas
def Mas_Vendidos():
    max_cantidad = 0
    producto_max = ""
    for venta in ventas:
        if venta["cantidad"] > max_cantidad:
            max_cantidad = venta["cantidad"]
            producto_max = venta["producto"]
    print(f"El producto más vendido es: {producto_max} con {max_cantidad} unidades.")     
# 7. Mostrar el listado de productos
def Productos():
    for produ in ventas:
        print(f"Los productos son: {produ["productos"]}")
# Llamada al menú principal
MenU()