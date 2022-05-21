# Write a program to print first 50 natural numbers using recursion.

def first_fifty_natural_numbers(n):
    if n > 0:
        if n == 1:
            print(n)
        else:
            print(f"{n},")
        first_fifty_natural_numbers(n - 1)


first_fifty_natural_numbers(50)


# Write a program to print the array elements using recursion.
def array_elements(nums, i=0):  # here i is a default parameter
    if i < len(nums):
        print(nums[i])
        array_elements(nums, i + 1)


array_elements([2, 5, 6, 7])


# Write a program to count the digits of a given number using recursion.

def number_of_digit(num, i=0):
    if num > 0:
        i = i + 1
        number_of_digit(num // 10, i)
    else:
        return i


print(number_of_digit(12))


# Write a program to get the largest element of an array using recursion.
def largerst_num(nums):
    pass





print(largerst_num([1, 2, 3, 4]))
