import pytest
import main
import imp


imp.reload(main)


# значения вводятся в " " по причине возвращение функцией input() исключительно строк
@pytest.mark.parametrize("n, m", [("2", "Ф"),
                                  ("A", "3")])
def test_size_isnumeric(n, m):
    import main
    with pytest.raises(main.SizeError):
        result = main.size_mtr(n, m)


@pytest.mark.parametrize("args", [
    ['1', 'F', '3', '4', '5'],
    ['1', "2+1", '3', '4', '5', '6', '7'],
    ['1', '2', '3', "A"]
])
def test_matrix_isnumeric(args):
    import main
    # Создать инстанс класса и прокинуть в него зачения? --- можно но реализовано через дополнительній чек
    with pytest.raises(main.EntrError):
        result = main.check_for_error(args)


def test_choise():
    import main
    with pytest.raises(main.ChoiseError):
        result = main.choise_operation(main.Matrix(1, 1, ["1"]), "-1")


def test_multiply():
    import main
    testmtr = main.Matrix(1, 1, [1])
    with pytest.raises(main.MultiplyError):
        result = testmtr.multiply("A")


def test_positive_opr():
    import main
    testmtr = main.Matrix(2, 2, [1, 0, 0, 1])
    result = testmtr.determinant(testmtr.matrix)
    assert result == 1

# test_positive_buff test_positive_buff test_positive_buff ????
