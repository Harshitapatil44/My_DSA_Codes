from array import *
import numpy as np

val = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])

# for x in val:
#   print(x, end=" , ")

# --->  i - for integer,
# ---> f - for float,
# ---> d - for double,
# ---> u - for unicode character,
# ---> b - for signed char,
# ---> B - for unsigned char,
# ---> h - for signed short,
# ---> H - for unsigned short,
# ---> l - for signed long,
# ---> L - for unsigned long,
# ---> q - for signed long long
# ---> Q - for unsigned long long

# to reverse the array :
# val.reverse()


# val.insert(1, 50)  # ---> to insert a value at a specific index
# val.append(100)  # ---> to add a value at the end of the array
# val[2] = 200  # ---> to overwrite the value at a specific index

# copyArray = array(val.typecode, (x * 3 for x in val))

# copyArray.pop()  # ---> to remove the last element of the array
# copyArray.pop(3)  # ---> to remove the element at a specific index
# copyArray.remove(9)  # ---> to remove the first occurrence of a specific value

# abc = val[2:5]  # ---> to slice the array from index 2 to 4 (5 is exclusive)

# abc = val[2:-3]

# abc = val[::-1]  # ---> to reverse the array using slicing

# for i in range(0, len(abc)):
#     print(abc[i], end=" ")

# arr = array("i", [])

# n = int(input("Enter the number: "))

# for i in range(0, n):
#     arr.append(int(input("Enter the value: ")))

# i = arr.index(30)  # ---> to find the index of the first occurrence of a specific value

# for x in arr:
#     print(x, end=" ")

# print("\nIndex Found: ", i)

# numpy array :

arr = np.array([1, 2, 3, 4])

arr = np.linspace(
    10, 20, 5
)  # --> to create an array of evenly spaced values between a specified range

arr = np.arange(
    10, 20, 2
)  # --> to create an array of values within a specified range with a specified step size

for x in arr:
    print(x, end=" ")
