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
### CASOS TEST ###

if __name__ == "__main__":

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        else:
            print(attr, " => ", columnasValidas(casosTest.__dict__[attr]))