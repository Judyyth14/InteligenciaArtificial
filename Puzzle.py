import random
 
# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join([str(numero) if numero != 0 else ' ' for numero in fila]))
    print()

# Función para mover una ficha
def mover_ficha(tablero, movimiento):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == movimiento:
                if i > 0 and tablero[i - 1][j] == 0:
                    tablero[i][j], tablero[i - 1][j] = tablero[i - 1][j], tablero[i][j]
                    return True
                if i < 2 and tablero[i + 1][j] == 0:
                    tablero[i][j], tablero[i + 1][j] = tablero[i + 1][j], tablero[i][j]
                    return True
                if j > 0 and tablero[i][j - 1] == 0:
                    tablero[i][j], tablero[i][j - 1] = tablero[i][j - 1], tablero[i][j]
                    return True
                if j < 2 and tablero[i][j + 1] == 0:
                    tablero[i][j], tablero[i][j + 1] = tablero[i][j + 1], tablero[i][j]
                    return True
    return False

# Inicialización del tablero
tablero = [[0, 3, 2], [6, 4, 7], [1, 5, 8]]
random.shuffle(tablero)

contador_movimientos = 0  # Agregar contador de movimientos

print("¡Vamos a jugar este puzzle!")

while True:
    imprimir_tablero(tablero)
    movimiento = input("Ingresa el número que deseas mover (o 'q' para salir): ")
    
    if movimiento == 'q':
        print("¡Gracias por participar!")
        break
    
    try:
        movimiento = int(movimiento)
        if 0 <= movimiento <= 8:
            if mover_ficha(tablero, movimiento):
                contador_movimientos += 1  # Incrementar el contador de movimientos
                if tablero == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
                    imprimir_tablero(tablero)
                    print("¡Felicidades! Has resuelto el puzzle en", contador_movimientos, "movimientos.")
                    break
            else:
                print("No puedes mover esa ficha.")
        else:
            print("Ingresa un número entre 0 y 8.")
    except ValueError:
        print("Ingresa un número válido o 'q' para salir.")

