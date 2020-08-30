# Uses python3
import sys

'''def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b'''
def gcd_naive(a, b):
    c=min(a,b)
    d=max(a,b)
    if(c==0):
        return d;
    else:
        return gcd_naive(c,d%c)
    
def lcm_naive(a, b):
    return int((a*b)/gcd_naive(a, b));
    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

