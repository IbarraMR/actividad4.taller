import random

def maximo_de_tres():
    a = int(input("ingrese el primer numero: "))
    b = int(input("ingrese el segundo numero: "))
    c = int(input("ingrese el tercer numero: "))
    maximo = max(a, b, c)
    print("el maximo es:", maximo)

def maximo_de_diez():
    print("ingrese 10 numeros:")
    numeros = []
    for i in range(10):
        n = int(input(f"numero {i+1}: "))
        numeros.append(n)
    maximo = max(numeros)
    print("el maximo entre los 10 es:", maximo)

def suma_vectores():
    N = int(input("cantidad de elementos en el vector a: "))
    M = int(input("cantidad de elementos en el vector b: "))
    A = [int(input(f"a[{i}]: ")) for i in range(N)]
    B = [int(input(f"b[{i}]: ")) for i in range(M)]
    print("suma de a:", sum(A))
    print("suma de b:", sum(B))
    if N == M:
        C = [A[i] + B[i] for i in range(N)]
        print("vector suma:", C)

def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in palabra if letra in vocales)

def contar_consonantes(palabra):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in palabra if letra.isalpha() and letra not in vocales)

def vocales_consonantes():
    oracion = input("ingrese una o mas oraciones: ")
    palabras = oracion.split()
    total_vocales = sum(contar_vocales(p) for p in palabras)
    total_consonantes = sum(contar_consonantes(p) for p in palabras)
    print("total de vocales:", total_vocales)
    print("total de consonantes:", total_consonantes)

def potencia_digitos_capicua():
    def potencia():
        x = int(input("ingrese un numero: "))
        k = int(input("ingrese la potencia k: "))
        print(f"{x}^{k} =", x ** k)

    def cantidad_digitos():
        x = input("ingrese un numero: ")
        print("cantidad de digitos:", len(x))

    def capicua():
        x = input("ingrese un numero: ")
        if x == x[::-1]:
            print("es capicua")
        else:
            print("no es capicua")

    while True:
        print("1. calcular potencia")
        print("2. contar digitos")
        print("3. ver si es capicua")
        print("0. volver al menu principal")
        op = input("opcion: ")
        if op == "1": potencia()
        elif op == "2": cantidad_digitos()
        elif op == "3": capicua()
        elif op == "0": break
        else: print("opcion invalida")

def suma_producto_matrices():
    def cargar_matriz(m, n):
        return [[int(input(f"m[{i}][{j}]: ")) for j in range(n)] for i in range(m)]

    def mostrar_matriz(m):
        for fila in m:
            print(fila)

    m = int(input("filas: "))
    n = int(input("columnas: "))
    print("cargar matriz a")
    A = cargar_matriz(m, n)
    print("cargar matriz b")
    B = cargar_matriz(m, n)
    op = input("sumar (s) o multiplicar (m) las matrices?: ")
    C = []
    for i in range(m):
        fila = []
        for j in range(n):
            if op == "s":
                fila.append(A[i][j] + B[i][j])
            elif op == "m":
                fila.append(A[i][j] * B[i][j])
        C.append(fila)
    print("resultado:")
    mostrar_matriz(C)

def matriz_factoriales():
    def factorial(n):
        f = 1
        for i in range(1, n+1): f *= i
        return f

    matriz = [
        [7, 11, 20, 11],
        [2, 4, 16, 8],
        [1, 3, 2, 9],
        [7, 3, 2, 20]
    ]
    suma_diag = sum(matriz[i][i] for i in range(len(matriz)))
    print("suma diagonal principal:", suma_diag)
    vector = []
    for fila in matriz:
        for num in fila:
            if factorial(num) >= suma_diag:
                vector.append(num)
    sin_repetidos = list(set(vector))
    ordenado = sorted(sin_repetidos)
    print("vector final ordenado:", ordenado)

def gestion_electrodomesticos():
    matriz = []
    def cargar():
        n = int(input("cuantos electrodomesticos vas a cargar: "))
        for i in range(n):
            nombre = input("nombre: ")
            proveedor = input("proveedor: ")
            precio = input("precio: ")
            while not precio.isdigit():
                precio = input("(debe ser numero) precio: ")
            stock = input("stock: ")
            while not stock.isdigit():
                stock = input("(debe ser numero) stock: ")
            matriz.append([nombre, proveedor, precio, stock])

    def mostrar_proveedor():
        prov = input("proveedor a buscar: ")
        for item in matriz:
            if item[1].lower() == prov.lower():
                print(item)

    def menor_precio():
        menor = min(matriz, key=lambda x: int(x[2]))
        print("producto con menor precio:", menor)

    def stock_positivo():
        for item in matriz:
            if int(item[3]) > 0:
                print(item)

    while True:
        print("--- gestion electrodomesticos ---")
        print("1. cargar datos")
        print("2. mostrar por proveedor")
        print("3. mostrar con menor precio")
        print("4. mostrar con stock positivo")
        print("0. volver")
        op = input("opcion: ")
        if op == "1": cargar()
        elif op == "2": mostrar_proveedor()
        elif op == "3": menor_precio()
        elif op == "4": stock_positivo()
        elif op == "0": break
        else: print("opcion invalida")

def lista_pacientes():
    lista = []
    def nuevo():
        nombre = input("nombre del paciente: ")
        lista.append(nombre)
    def atender():
        if lista:
            print("atendido:", lista.pop(0))
        else:
            print("no hay pacientes")
    def urgencia():
        nombre = input("nombre del paciente urgente: ")
        lista.insert(0, nombre)
    def cuantos_faltan():
        nombre = input("nombre a buscar: ")
        if nombre in lista:
            print("faltan", lista.index(nombre), "pacientes antes que", nombre)
        else:
            print("el paciente no esta en la lista")
    while True:
        print("--- lista de pacientes ---")
        print("1. ingresar paciente")
        print("2. atender siguiente")
        print("3. urgencia")
        print("4. cuantos faltan")
        print("0. volver")
        op = input("opcion: ")
        if op == "1": nuevo()
        elif op == "2": atender()
        elif op == "3": urgencia()
        elif op == "4": cuantos_faltan()
        elif op == "0": break
        else: print("opcion invalida")

def tragamonedas():
    simbolos = ["o", "x", "7"]
    columnas = [[random.choice(simbolos) for _ in range(9)] for _ in range(3)]
    while True:
        print("--- maquina tragamonedas ---")
        print("columnas:")
        for col in columnas:
            print(col)
        input("presiona enter para jugar...")
        indices = [random.randint(0, 8) for _ in range(3)]
        resultado = [columnas[i][indices[i]] for i in range(3)]
        print("resultado:", resultado)
        if resultado == ["x"] * 3:
            print("gano 10 fichas")
        elif resultado == ["o"] * 3:
            print("gano 100 fichas")
        elif resultado == ["7"] * 3:
            print("gano 1000 fichas")
        else:
            print("no gano")
        if input("jugar otra vez? (s/n): ").lower() != "s":
            break

# menu principal
def menu():
    while True:
        print("--- menu principal ---")
        print("1. maximo entre tres numeros")
        print("2. maximo entre diez numeros")
        print("3. operaciones con vectores")
        print("4. contar vocales y consonantes")
        print("5. potencia / digitos / capicua")
        print("6. suma o producto de matrices")
        print("7. matriz factorial y ordenamiento")
        print("8. gestion de electrodomesticos")
        print("9. lista de pacientes")
        print("10. maquina tragamonedas")
        print("0. salir")
        opcion = input("elegi una opcion: ")
        if opcion == "1": maximo_de_tres()
        elif opcion == "2": maximo_de_diez()
        elif opcion == "3": suma_vectores()
        elif opcion == "4": vocales_consonantes()
        elif opcion == "5": potencia_digitos_capicua()
        elif opcion == "6": suma_producto_matrices()
        elif opcion == "7": matriz_factoriales()
        elif opcion == "8": gestion_electrodomesticos()
        elif opcion == "9": lista_pacientes()
        elif opcion == "10": tragamonedas()
        elif opcion == "0":
            print("nos vemos")
            break
        else:
            print("opcion invalida")

menu()
