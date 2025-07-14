from operator import add, sub

# Q1
def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

print(a_plus_abs_b(1,-2))

# Q2
def two_of_three(i, j, k):
    return i**2 + j**2 + k**2 - max(i,j,k)**2

print(two_of_three(1,3,3))

# Q3
def largest_factor(n):
    if n % 2  == 0:
        return n//2
    else:
        list = []
        for i in range(1,n//2):
            if n%i == 0:
                list.append(i)
        return list[-1]

print(largest_factor(13))

# Q4
def hailstone(n):
    step = 0
    while n != 1:
        print(n)
        if n % 2 == 0 :
            n = n//2
            step = step + 1
        else:
            n = n * 3 +1
            step = step + 1
    return step

print(hailstone(111))


