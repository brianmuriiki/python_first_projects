#calculate matrix
#array calculations
import numpy as np

#functions to be called on matrix calculations
def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

#calculate matrix
#array calculations

#functions to be called on matrix calculations
def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def transpose_matrix(matrix):
    return np.transpose(matrix)

def determinant_matrix(matrix):
    return np.linalg.det(matrix)

def inverse_matrix(matrix):
    return np.linalg.inv(matrix)

def divide_matrices(matrix1, matrix2):
    return np.divide(matrix1, matrix2)

#array calculations
def add_arrays(array1, array2):
    return np.add(array1, array2)

def subtract_arrays(array1, array2):
    return np.subtract(array1, array2)

def multiply_arrays(array1, array2):
    return np.multiply(array1, array2)

def divide_arrays(array1, array2):
    return np.divide(array1, array2)

def power_arrays(array1, array2):
    return np.power(array1, array2)

def sqrt_array(array):
    return np.sqrt(array)

def log_array(array):
    return np.log(array)

def sin_array(array):
    return np.sin(array)

def cos_array(array):
    return np.cos(array)

def tan_array(array):
    return np.tan(array)

def inverse_sin_array(array):
    return np.arcsin(array)

def inverse_cos_array(array):
    return np.arccos(array)
     
def inverse_tan_array(array):
    return np.arctan(array)

###################start of main program####################

if __name__ == "__main__":
    print("==================Advanced Calculator===================")
    print("1. Matrix Calculations")
    print("2. Array Calculations")
    try:
        choice = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("Invalid choice. Please enter 1 or 2.")
        exit(1)

    if choice == 1:
        print("Matrix Calculations")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Transpose Matrix")
        print("5. Determinant of Matrix")
        print("6. Inverse of Matrix")
        print("7. Divide Matrices")
        try:
            matrix_choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid choice for matrix calculations.")
            exit(1)

        # Get matrix 1 from user input
        try:
            rows1 = int(input("Enter the number of rows for matrix 1: "))
            cols1 = int(input("Enter the number of columns for matrix 1: "))
        except ValueError:
            print("Invalid dimensions.")
            exit(1)

        matrix1 = []
        print("Enter the elements of matrix 1 (row by row, space-separated):")
        for i in range(rows1):
            row = list(map(float, input().split()))
            matrix1.append(row)
        matrix1 = np.array(matrix1)

        # Get matrix 2 if needed
        if matrix_choice in [1, 2, 3, 7]:
            try:
                rows2 = int(input("Enter the number of rows for matrix 2: "))
                cols2 = int(input("Enter the number of columns for matrix 2: "))
            except ValueError:
                print("Invalid dimensions.")
                exit(1)

            matrix2 = []
            print("Enter the elements of matrix 2 (row by row, space-separated):")
            for i in range(rows2):
                row = list(map(float, input().split()))
                matrix2.append(row)
            matrix2 = np.array(matrix2)
        else:
            matrix2 = None

        ########calculations for matrix operations########
        if matrix_choice == 1:
            result = add_matrices(matrix1, matrix2)
            print("Result of addition:")
            print(result)
        elif matrix_choice == 2:
            result = subtract_matrices(matrix1, matrix2)
            print("Result of subtraction:")
            print(result)
        elif matrix_choice == 3:
            result = multiply_matrices(matrix1, matrix2)
            print("Result of multiplication:")
            print(result)
        elif matrix_choice == 4:
            result = transpose_matrix(matrix1)
            print("Result of transpose:")
            print(result)
        elif matrix_choice == 5:
            result = determinant_matrix(matrix1)
            print("Result of determinant:")
            print(result)
        elif matrix_choice == 6:
            result = inverse_matrix(matrix1)
            print("Result of inverse:")
            print(result)
        elif matrix_choice == 7:
            result = divide_matrices(matrix1, matrix2)
            print("Result of division:")
            print(result)
        else:
            print("Invalid choice for matrix calculations.")

    elif choice == 2:
        print("Array Calculations")
        print("1. Add Arrays")
        print("2. Subtract Arrays")
        print("3. Multiply Arrays")
        print("4. Divide Arrays")
        print("5. Power of Arrays")
        print("6. Square Root of Array")
        print("7. Logarithm of Array")
        print("8. Sine of Array")
        print("9. Cosine of Array")
        print("10. Tangent of Array")
        print("11. Inverse Sine of Array")
        print("12. Inverse Cosine of Array")
        print("13. Inverse Tangent of Array")
        try:
            array_choice = int(input("Enter your choice (1-13): "))
        except ValueError:
            print("Invalid choice for array calculations.")
            exit(1)

        # Get arrays from user input
        if array_choice in [1, 2, 3, 4, 5]:
            try:
                size = int(input("Enter the size of the arrays: "))
            except ValueError:
                print("Invalid size.")
                exit(1)
            array1 = list(map(float, input("Enter the elements of array 1 (space-separated): ").split()))
            array2 = list(map(float, input("Enter the elements of array 2 (space-separated): ").split()))
            array1 = np.array(array1)
            array2 = np.array(array2)
        else:
            try:
                size = int(input("Enter the size of the array: "))
            except ValueError:
                print("Invalid size.")
                exit(1)
            array1 = list(map(float, input("Enter the elements of the array (space-separated): ").split()))
            array1 = np.array(array1)

        ########calculations for array operations########
        if array_choice == 1:
            result = add_arrays(array1, array2)
            print("Result of addition:")
            print(result)
        elif array_choice == 2:
            result = subtract_arrays(array1, array2)
            print("Result of subtraction:")
            print(result)
        elif array_choice == 3:
            result = multiply_arrays(array1, array2)
            print("Result of multiplication:")
            print(result)
        elif array_choice == 4:
            result = divide_arrays(array1, array2)
            print("Result of division:")
            print(result)
        elif array_choice == 5:
            result = power_arrays(array1, array2)
            print("Result of power:")
            print(result)
        elif array_choice == 6:
            result = sqrt_array(array1)
            print("Result of square root:")
            print(result)
        elif array_choice == 7:
            result = log_array(array1)
            print("Result of logarithm:")
            print(result)
        elif array_choice == 8:
            result = sin_array(array1)
            print("Result of sine:")
            print(result)
        elif array_choice == 9:
            result = cos_array(array1)
            print("Result of cosine:")
            print(result)
        elif array_choice == 10:
            result = tan_array(array1)
            print("Result of tangent:")
            print(result)
        elif array_choice == 11:
            result = inverse_sin_array(array1)
            print("Result of inverse sine:")
            print(result)
        elif array_choice == 12:
            result = inverse_cos_array(array1)
            print("Result of inverse cosine:")
            print(result)
        elif array_choice == 13:
            result = inverse_tan_array(array1)
            print("Result of inverse tangent:")
            print(result)
        else:
            print("Invalid choice for array calculations.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

print("END OF THE PROGRAM.")