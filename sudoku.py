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