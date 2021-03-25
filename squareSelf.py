'''
John and Linda are playing a numbers game. John asked Linda to find the number whose square ends
with the number itself. The numnber should also be a positive integer. Write a program to implement the
above logic.

Input Format:
    Input contains an integer 'N' denoting the number.

Output Format:
    If the numebr whose square ends with the number itself, print "Correct Number", otherwise print
    "Incorrect Number". If the user enters negative integer, the result should display "Wrong input".

Constraints:
    1 <= N <= 10 ^ 8
'''

N = int(input())

def automorphic(N: int):
    sqrN = N * N
    while N > 0:
        if N % 10 != sqrN % 10:
            return False
        N //= 10
        sqrN //= 10
    return True

if N < 0:
    print('Wrong Input')
else:
    # print('Correct Number' if automorphic(N) else 'Incorrect Number')
    i = 1
    while i <= N:
        if automorphic(i):
            print(i, end=' ')
        i += 1