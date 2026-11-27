
def is_square_matrix(sudoku):
    assert isinstance(sudoku, list)
    for fila in sudoku:
        if len(fila) != len(sudoku):
            return False
    return True


### CASOS TEST ###

if __name__ == "__main__":
    import sys
    
    sys.path.append("../")
    
    import casosTest.casos_test_sudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        else:
            print(attr, " => ", is_square_matrix(casosTest.__dict__[attr]))
