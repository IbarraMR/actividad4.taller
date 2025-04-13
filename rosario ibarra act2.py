def ejercicio1():
    numero = int(input("ingresar un numero: "))
    numero_ingresado = numero
    contador = 0
    if numero == 0:
        contador = 1
    else:
        while numero > 0:
            numero = numero // 10
            contador += 1
    print("el numero", numero_ingresado, "tiene", contador, "digitos.")

def ejercicio2():
    numero = (input("ingresar un numero decimal: "))
    coma = numero.find(",")
    enteros = numero[:coma]
    decimales = numero[coma+1:]
    cant_enteros = len(enteros)
    cant_decimales = len(decimales)
    print("el numero ingresado tiene", cant_enteros, "digitos enteros y", cant_decimales, "decimales")

def ejercicio3():
    numeros = int(input("ingresaar numeros, cuando termines ingresar el 0: ")) 
    vector = []
    while numeros > 0:
        vector.append(numeros)
        numeros = int(input("ingresaar numeros, cuando termines ingresar el 0: "))
    for numero in vector:
        divisores = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += 1
        if divisores > 2:
            print(numero)

def ejercicio4():
    numeros = int(input("ingresar numeros, cuando termines ingresar el 0: "))
    vector = []
    while numeros > 0:
        vector.append(numeros)
        numeros = int(input("ingresar nnmeros, cuando termines ingresar el 0: "))
    vector_nuevo = []
    while len(vector) > 0:
        nuevo = vector.pop()
        vector_nuevo.append(nuevo)
    print(vector_nuevo)

def ejercicio5():
    import random
    listaA = []
    listaB = []
    for i in range(20):
        numero = random.randrange(20, 200)
        listaA.append(numero)
    listaB.append("A")
    for numero in listaA:
        texto = str(numero)
        pares = 0
        for i in texto:
            if int(i) % 2 == 0:
                pares += 1
        if pares == 2:
            listaB.append(numero)
    listaB.append("B")
    for numero in listaA:
        texto = str(numero)           
        impares = 0
        for i in texto:
            if int(i) % 2 != 0:
                impares += 1
        if impares >= 2:
            listaB.append(numero)
    print(listaA)
    print(listaB)

def ejercicio6():
    import random
    lista = []
    lista_nueva = []
    for i in range(10):
        numero = random.randrange(20, 200)
        lista.append(numero)
    K = random.randrange(2, 10)
    for i in lista:
        lista_nueva.append(i)
        if i % K == 0:
            lista_nueva.append(K)
    print("Lista original:", lista)
    print("Lista nueva:", lista_nueva)

def ejercicio7():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print("matriz =", matriz)
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        promedio = sum(matriz[i]) / columnas
        print(f"Fila {i + 1}: {promedio:.2f}")
    for j in range(columnas):
        suma_columna = 0
        for i in range(filas):
            suma_columna += matriz[i][j]
        promedio = suma_columna / filas
        print(f"Columna {j + 1}: {promedio:.2f}")

def ejercicio8():
    matriz = [
        [3, 2, 1],
        [4, 5, 6],
        [7, 8, 3]
    ]
    print("Matriz cuadrada =", matriz)
    suma_diagonal = 0
    for i in range(len(matriz)):
        suma_diagonal += matriz[i][i]
    print("Suma de la diagonal principal:", suma_diagonal)

    def factorial(n):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    vector_resultado = []
    for fila in matriz:
        for numero in fila:
            if factorial(numero) >= suma_diagonal:
                vector_resultado.append(numero)

    print("Vector con repetidos:", vector_resultado)
    vector_sin_repetidos = []
    for elemento in vector_resultado:
        if elemento not in vector_sin_repetidos:
            vector_sin_repetidos.append(elemento)
    print("Vector sin repetidos:", vector_sin_repetidos)

def ejercicio9():
    matriz = [
        [3, 8, 4],
        [9, 7, 6],
        [2, 1, 5]
    ]
    print("Matriz=", matriz)
    k = 0
    h = 1
    numero = matriz[k][h]
    mayor_fila = max(matriz[k])
    menor_columna = matriz[0][h]
    for i in range(1, len(matriz)):
        if matriz[i][h] < menor_columna:
            menor_columna = matriz[i][h]

    if numero == mayor_fila and numero == menor_columna:
        print("El numero", numero, "en la posicion [", k, "][", h, "] es un punto silla.")
    else:
        print("El numero", numero, "en la posicion [", k, "][", h, "] NO es un punto silla.")

def ejercicio10():
    matriz = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]
    print("Matriz=", matriz)
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas != columnas:
        print("La matriz no es simetrica porque no es cuadrada.")
    else:
        simetrica = True
        for i in range(filas):
            for j in range(columnas):
                if matriz[i][j] != matriz[j][i]:
                    simetrica = False
        if simetrica:
            print("La matriz si es simerica.")
        else:
            print("La matriz no es simetrica.")

def menu():
    while True:
        print("MENU DE EJERCICIOS")
        print("1. Ejercicio 1 - Contar digitos")
        print("2. Ejercicio 2 - Decimales y enteros")
        print("3. Ejercicio 3 - Mas de 2 divisores")
        print("4. Ejercicio 4 - Invertir vector")
        print("5. Ejercicio 5 - Lista B pares/impares")
        print("6. Ejercicio 6 - Insertar multiplo K")
        print("7. Ejercicio 7 - Promedios matriz")
        print("8. Ejercicio 8 - Factorial y diagonal")
        print("9. Ejercicio 9 - Punto silla")
        print("10. Ejercicio 10 - Matriz simetrica")
        print("0. Salir")

        opcion = input("Elegir una opcion: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            ejercicio10()
        elif opcion == "0":
            print("chau")
            break
        else:
            print("opcion incorrecta")

menu()
