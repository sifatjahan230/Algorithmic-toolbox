# Uses python3
import sys

'''def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10'''

def get_fibonacci_last_digit_naive(n):
    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b) % 10
        print(b)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    get_fibonacci_last_digit_naive(n)
