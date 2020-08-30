# python3
import os

def max_pairwise_product(n,a):
    #k=max(a);
    a.sort() 
    max_product=a[n-1]*a[n-2]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    n = len(input_numbers)
    print(max_pairwise_product(n,input_numbers))
