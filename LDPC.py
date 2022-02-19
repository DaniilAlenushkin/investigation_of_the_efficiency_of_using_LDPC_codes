from function_for_LDPC import *

generator_matrix = [[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]

check_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]]

if __name__ == '__main__':

    for j in range(100000):
        while True:
            signal = [randint(0, 1) for i in range(len(generator_matrix))]
            if max(signal) != 0:
                break
        code_signal = multiplication_vector_on_matrix(signal[:], generator_matrix[:])
        syndrome = multiplication_vector_on_matrix(code_signal[:],
                                                   transposition(check_matrix))
        counter_syndrome = 0
        for k in syndrome:
            counter_syndrome += k
        if counter_syndrome != 0:
            print(syndrome)

    check_matrix_one_position = []
    for i in check_matrix:
        check_matrix_one_position_line = []
        for j in range(len(i)):
            if i[j] == 1:
                check_matrix_one_position_line.append(j)
            if j + 1 == len(i):
                check_matrix_one_position.append(check_matrix_one_position_line)
    for i in check_matrix_one_position:
        print(i)
    for i in check_matrix:
        for j in check_matrix:
            if i == j:
                continue
            counter = 0
            for z in range(len(i)):
                if i[z] == j[z] and i[z] == 1:
                    counter += 1
            if counter > 1:
                print(
                    f'{check_matrix.index(i) + 1} строка похожа на '
                    f'{check_matrix.index(j) + 1} {counter} символами')
