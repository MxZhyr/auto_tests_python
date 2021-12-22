import copy
import numbers


class SizeError(Exception):
    """Input Size Error (kinda)"""


class EntrError(Exception):
    """Input Matrix Args error"""


class ChoiseError(Exception):
    """Input Matrix Args error"""


class MultiplyError(Exception):
    """Input Matrix Args error"""


ch = True


class Matrix:

    def __init__(self, n, m, args):
        self.columns = m
        self.rows = n
        self.matrix = self.get_matrix(n, m, args)

    def get_matrix(self, n, m, args):
        itter = 0
        matrix = [[0 for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = args[itter]
                itter += 1
        return matrix

    def add(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = [[self.matrix[i][j] + mtx.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            # args = []
            for row in result:
                for number in row:
                    # args.append(number)
                    print(number, end=" ")
                print()
            # return Matrix(self.rows, self.columns, args)
        else:
            print("ERROR")

    def multiply(self, number):
        if number.isnumeric():
            result = [[self.matrix[i][j] * float(number) for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            # args = []
            for row in result:
                for number in row:
                    # args.append(number)
                    print(number, end=" ")
                print()
            # return Matrix(self.rows, self.columns, args)
        else:
            raise MultiplyError(f"'{number}' Ошибка: при выборе необходимо вводить строго рациональные числа\n")

    def transpose(self):
        transposed = [[self.matrix[i][j] for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        self.matrix = transposed

    def transpose_side(self):
        transposed = [[self.matrix[i][j] for i in range(-1, -len(self.matrix) - 1, -1)] for j in
                      range(-1, -len(self.matrix[0]) - 1, -1)]
        self.matrix = transposed

    def transpose_vertical(self):
        for row in self.matrix:
            row.reverse()

    def transpose_horizontal(self):
        self.matrix.reverse()

    def printer(self):
        for row in self.matrix:
            for number in row:
                print(int(number), end=" ")
            print()

    def multiply_matrices(self, mtx):
        if self.columns != mtx.rows:
            print("The operation cannot be performed.")
        else:
            result = [[sum([self.matrix[i][k] * mtx.matrix[j][k] for k in range(len(mtx.matrix[0]))]) for j in
                       range(len(mtx.matrix))] for i in range(len(self.matrix))]

            for row in result:
                for number in row:
                    print(round(number, 2), end=" ")
                print()

    @staticmethod
    def determinant(mtx):
        if len(mtx) == 1:
            return mtx[0][0]
        elif len(mtx) == 2:
            det = mtx[0][0] * mtx[1][1] - mtx[1][0] * mtx[0][1]
            return det
        else:
            recur = 0
            for i, e in enumerate(mtx):
                rex = mtx[0][i] * Matrix.determinant(
                    [[el for ind, el in enumerate(matx) if ind != i] for matx in mtx[1:]])
                if i % 2 == 0:
                    recur += rex
                else:
                    recur -= rex
            return recur


def size_mtr(n, m):
    flag = True
    while flag:
        if n.isnumeric():
            if m.isnumeric():
                print("Введите матрицу: ")
                matrix_a = entr_mtr(int(n), int(m))

                flag = False
                return matrix_a
            else:
                raise SizeError(f"'{m}' Ошибка: при выборе необходимо вводить строго цифры от 1 до 9\n")
        else:
            raise SizeError(f"'{n}' Ошибка: при выборе необходимо вводить строго цифры от 1 до 9\n")


def check_for_error(arg):
    k = 0
    while k < len(arg):
        if arg[k].isnumeric():  # isinstance(inp, numbers.Number):
            arg[k] = float(arg[k])
            k += 1
        else:
            raise EntrError(f"'{arg[k]}' Ошибка: при заполнении необходимо вводить строго рациональные числа \n")
    return arg


def entr_mtr(n, m):
    k = 0
    arg = []
    while k < (n * m):
        inp = input()
        arg.append(inp)
        k += 1

    matrix_a = Matrix(n, m, check_for_error(arg))
    return matrix_a


buf_mtr = Matrix(1, 1, [0])

def save_matr(mtx):
    global buf_mtr
    buf_mtr = mtx

def print_matr():
    global buf_mtr
    buf_mtr.printer()


def choise_operation(matrix_a, choice):
    if choice == "1":  # ++
        const = input("Enter constant: ")
        print("The result is:")
        matrix_a.multiply(const)
        return matrix_a

    elif choice == "2":  # ++

        print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
        tran_choice = input("Your choice: ")
        if tran_choice == "1":
            matrix_a.transpose()
        elif tran_choice == "2":
            matrix_a.transpose_side()
        elif tran_choice == "3":
            matrix_a.transpose_vertical()
        elif tran_choice == "4":
            matrix_a.transpose_horizontal()

        matrix_a.printer()
        return matrix_a

    elif choice == "3":  # ++

        print("The result is:")
        print(matrix_a.determinant(matrix_a.matrix))
        return matrix_a

    elif choice == "4":  # ++
        print("Введите резмерность матрицы, строки: ")
        n = input()
        print("Столбцы: ")
        m = input()
        matrix_b = size_mtr(n, m)
        matrix_b.transpose()
        # print(matrix_b.matrix)
        print("The result is:")
        matrix_a.multiply_matrices(matrix_b)
        return matrix_a


    elif choice == "5":  # ++

        print("Введите резмерность матрицы, строки: ")
        n = input()
        print("Столбцы: ")
        m = input()
        matrix_b = size_mtr(n, m)
        print("Enter second matrix: ")

        print("The result is:")
        matrix_a.add(matrix_b)
        return matrix_a


    elif choice == "6":  # ++

        print("Введите резмерность матрицы, строки: ")
        n = input()
        print("Столбцы: ")
        m = input()
        matrix_b = size_mtr(n, m)

        print("The result is:")
        matrix_a.add(matrix_b.multiply(-1))
        return matrix_a

    elif choice == "7":
        save_matr(matrix_a)
        print("Saved!:")
        return matrix_a

    elif choice == "8":
        print_matr()
        return matrix_a

    elif choice == "9":
        print("Введите резмерность матрицы, строки: ")
        n = input()
        print("Столбцы: ")
        m = input()
        matrix_a = size_mtr(n, m)
        return matrix_a

    elif choice == "0":
        global ch
        ch = False
        return False

    else:
        raise ChoiseError(f"'{choice}' Ошибка: при заполнении необходимо вводить строго рациональные числа \n")


def menu():
    print("Введите резмерность матрицы, строки: ")
    n = input()
    print("Столбцы: ")
    m = input()
    matrix_a = size_mtr(n, m)

    while ch:
        print("1. Умножить матрицу на число\n2. Транспонировать матрицу \n3. Найти определитель матрицы \n\
      4. Умножить на новую матрицу \n5. Сложить с новой матрицей\n6. Вычесть новую матрицу\n7. Сохранить текущую матрицу в буфер \n\
      8. Вывести содержимое буфера \n9. Ввести матрицу еще раз  \n0. Выход")
        choice = input()
        matrix_a = choise_operation(matrix_a, choice)


menu()
