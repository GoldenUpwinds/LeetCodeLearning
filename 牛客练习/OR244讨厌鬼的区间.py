import sys

def find_max(l1,r1,l2,r2):
    if l2 <= r1 <= r2 or l1 <= r2 <=r1:
        return min(r1,r2)
    else:
        return -1

def main():
    max_num = -1
    l1,r1,l2,r2,l3,r3 = map(int,input().split())

    max_num = max(max_num,2*find_max(l1,r1,l2,r2))
    max_num = max(max_num,2*find_max(l1,r1,l3,r3))
    max_num = max(max_num,2*find_max(l2,r2,l3,r3))

    print(max_num)

if __name__ == "__main__":
    main()
