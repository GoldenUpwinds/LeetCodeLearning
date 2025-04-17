from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_dict = {}
        for i, char in enumerate(s):
            if char in hash_dict:
                hash_dict[char][1] = i
            else:
                hash_dict[char] = [i, i]
        output = []
        pointer = None
        for key in list(hash_dict):
            if key not in hash_dict:
                continue
            if not pointer:
                pointer = hash_dict[key]
                del hash_dict[key]
            elif pointer[1] < hash_dict[key][0]:
                output.append(pointer[1]-pointer[0]+1)
                pointer = hash_dict[key]
                del hash_dict[key]
            else:
                pointer[1] = max(hash_dict[key][1],pointer[1])
                del hash_dict[key]
        if pointer:
            output.append(pointer[1]-pointer[0]+1)
        return output

Solve = Solution()
s = "ababcbacadefegdehijhklij"
print(Solve.partitionLabels(s))