def filasValidas(sudoku):
    for fila in sudoku:
        for indice in range(1, len(sudoku)+1):
            if indice not in fila:
                return False
    return True