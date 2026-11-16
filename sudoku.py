def esMatrizCuadrada(sudoku):
    for fila in sudoku:
        if len(fila) != len(sudoku):
            return False
def sonElementosEnteros(sudoku):
    for fila in sudoku:
        for columna in fila:
            if type(columna) != int:
                return False
    return True
def columnasValidas(sudoku):
    for columna in range(len(sudoku)):
        numerosEnColumna = []
        for elemento in range(len(sudoku)):
            numerosEnColumna.append(sudoku[elemento][columna])
        for numero in range(1, len(sudoku) + 1):
            if numero not in numerosEnColumna:
                return False
                
    return True  # Si pasa todas las validaciones, las columnas son correctas
