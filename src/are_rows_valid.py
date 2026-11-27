
def are_rows_valid(sudoku):

    assert isinstance(sudoku, list)

    for fila in sudoku:

        for indice in range(1, len(sudoku) + 1):

            if indice not in fila:

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
            print(attr, " => ", are_rows_valid(casosTest.__dict__[attr]))
