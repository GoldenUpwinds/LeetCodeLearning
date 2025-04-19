import sys

def findFactor(num)->int:
    for i in range(2,num+1):
        if num % i == 0:
            return i

def main():
    N = int(input())
    output = 0
    while N != 1:
        factor = findFactor(int(N))
        output += factor
        N /= factor
    print(output)

if __name__ == "__main__":
    main()
