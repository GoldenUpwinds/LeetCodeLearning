import sys
import math

def main():
    a,b = map(int,input().split())
    x = float(1)/float(b*math.log(a))
    y = math.log(x,a) - b*x
    print(f"{y:.10f}")

if __name__ == "__main__":
    main()