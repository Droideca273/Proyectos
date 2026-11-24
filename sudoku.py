def esMatrizCuadrada(sudoku):
    assert isinstance(sudoku, list)
    for fila in sudoku:
        if len(fila) != len(sudoku):
            return False
    return True

def sonElementosEnteros(sudoku):
    assert isinstance(sudoku, list)
    for fila in sudoku:
        for columna in fila:
            if type(columna) != int:
                return False
    return True

def columnasValidas(sudoku):
    assert isinstance(sudoku, list)
    for columna in range(len(sudoku)):
        numerosEnColumna = []
        for elemento in range(len(sudoku)):
            numerosEnColumna.append(sudoku[elemento][columna])
        for numero in range(1, len(sudoku) + 1):
            if numero not in numerosEnColumna:
                return False
    return True

def filasValidas(sudoku):
    assert isinstance(sudoku, list)
    for fila in sudoku:
        for indice in range(1, len(sudoku) + 1):
            if indice not in fila:
                return False
    return True

def checkSudoku(sudoku):
    assert isinstance(sudoku, list)
    return (
        esMatrizCuadrada(sudoku)
        and sonElementosEnteros(sudoku)
        and filasValidas(sudoku)
        and columnasValidas(sudoku)
    )

correct = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

incorrect = [[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]

incorrect3 = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 6],
    [4, 5, 2, 1, 3],
    [3, 4, 5, 2, 1],
    [5, 6, 4, 3, 2],
]

incorrect4 = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]

incorrect5 = [[1, 1.5], [1.5, 1]]

sudoku_booleanos = [
    [True, 2, 3],
    [2, 3, 1],
    [3, 1, 2],
]

sudoku_fuera_de_rango = [
    [1, 2, 4],
    [2, 3, 1],
    [3, 1, 2],
]

sudoku_valido_9x9 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

if __name__ == "__main__":
    assert checkSudoku(correct) == True
    assert checkSudoku(incorrect) == False
    assert checkSudoku(incorrect2) == False
    assert checkSudoku(incorrect3) == False
    assert checkSudoku(incorrect4) == False
    assert checkSudoku(incorrect5) == False
    assert checkSudoku(sudoku_booleanos) == False
    assert checkSudoku(sudoku_fuera_de_rango) == False
    assert checkSudoku(sudoku_valido_9x9) == True
    print("Casos test superados")