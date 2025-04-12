import sys
from collections import defaultdict

class UnionFind:
    """并查集实现"""
    def __init__(self, n):
        self.pa = list(range(n))
    
    def find(self, x):
        """路径压缩查找根节点"""
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def merge(self, x, y):
        """合并两个集合"""
        px, py = self.find(x), self.find(y)
        self.pa[px] = py

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    # 读取 n, m, q
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1

    # 存储朋友关系, 以及接下来会断开关系的边 (需要删除的边)
    sp = set()
    asp = set()

    # 存储查询
    queries = []

    # 存储所有节点的编号
    node = set()

    # 处理输入的朋友关系
    for _ in range(m):
        u, v = int(data[idx]), int(data[idx + 1])
        idx += 2
        node.add(u)
        node.add(v)
        sp.add((u, v))

    # 处理查询
    for _ in range(q):
        op, u, v = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        queries.append((op, u, v))
        node.add(u)
        node.add(v)
        if op == 1 and ((u, v) in sp or (v, u) in sp):
            asp.add((u, v))

    # 离散化节点编号
    ump = {t: i + 1 for i, t in enumerate(sorted(node))}
    idx = len(ump) + 1

    # 初始化并查集
    u1 = UnionFind(idx)
    u2 = UnionFind(idx)

    # 如果不删除应该会有一个怎么样的并查集存在
    for x, y in sp:
        u1.merge(ump[x], ump[y])

    # 为初始的朋友建立关系
    for x, y in sp:
        # 这个需要建立的关系不能在需要删除的集合中
        if (x, y) in asp or (y, x) in asp:
            continue
        u2.merge(ump[x], ump[y])

    # 倒序遍历queries，将删边变成添加边
    ans = []
    for op, x, y in reversed(queries):
        if op == 2:
            if u2.find(ump[x]) == u2.find(ump[y]):
                ans.append(1)
            else:
                ans.append(0)
        else:
            if u1.find(ump[x]) == u1.find(ump[y]):
                u2.merge(ump[x], ump[y])

    # 倒序输出答案
    sys.stdout.write('\n'.join("Yes" if x == 1 else "No" for x in reversed(ans)) + '\n')

if __name__ == "__main__":
    main()  