# Uses python3
import sys

'''def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd'''

def gcd_naive(a, b):
    c=min(a,b)
    d=max(a,b)
    if(c==0):
        return d;
    else:
        return gcd_naive(c,d%c) 
    '''while(c): 
       d, c = c, d % c 
  
   return d'''

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
