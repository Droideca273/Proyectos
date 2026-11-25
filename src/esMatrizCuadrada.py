def esMatrizCuadrada(sudoku):
    assert isinstance(sudoku, list)
    for fila in sudoku:
        if len(fila) != len(sudoku):
            return False
    return True

### CASOS TEST ###

if __name__ == "__main__":

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        else:
            print(attr, " => ", esMatrizCuadrada(casosTest.__dict__[attr]))