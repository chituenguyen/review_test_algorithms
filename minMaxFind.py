from decimal import Decimal

array = [1, 2, 3, 4, 5]


# define function for find min in array for elements than 64 bits
def min_array(arr):
    min_value = Decimal("Infinity")
    for element in arr:
        if element < min_value:
            min_value = element
    return min_value


# define function for find max in array for elements than 64 bits
def max_array(arr):
    max_value = Decimal("-Infinity")
    for element in arr:
        if element > max_value:
            max_value = element
    return max_value


# define function for find even elements in array for elements than 64 bits
def even_find(arr):
    even_elements = ''
    for element in arr:
        if element % 2 == 0:
            even_elements += (str(element) + ' ')

    print("Even elements:", even_elements)


# define function for find odd elements in array for elements than 64 bits
def odd_find(arr):
    odd_elements = ''
    for element in arr:
        if element % 2 == 1:
            odd_elements += (str(element) + ' ')

    print("Odd elements:", odd_elements)


# define function for find min max
def min_max_find(arr):
    sum_array = sum(map(int, arr))  # sum for 64bit
    min_total_4_elements = sum_array - max_array(arr)
    max_total_4_elements = sum_array - min_array(arr)
    print(min_total_4_elements, '', max_total_4_elements)


min_max_find(array)
even_find(array)
odd_find(array)
