# This is the solution for problem 32 from projecteuler
# Link of the problem: https://projecteuler.net/problem=32

from itertools import permutations

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = list(permutations(digits))

def join_tup(tup):
    result = tup[0]
    for digit in tup[1:]:
        result = result * 10 + digit
    return result

sum = 0
found_products = []

def check_pandigital(perm, num1_size, num2_size):
    num1 = join_tup(perm[:num1_size])
    num2 = join_tup(perm[num1_size:num1_size+num2_size])
    product = num1 * num2
    num3 = join_tup(p[num1_size+num2_size:])
    product_unfound = not product in found_products
    if product == num3 and product_unfound:
        global sum
        sum += product
        found_products.append(product)

for p in perms:
    # Check first case: 1-digit number * 4-digit number = 4-digit number
    check_pandigital(p, num1_size=1, num2_size=4)
    # Check second case: 2-digit number * 3-digit number = 4-digit number
    check_pandigital(p, num1_size=2, num2_size=3)

print(f'Sum of products that form a pandigital with their multiplicants: {sum}')