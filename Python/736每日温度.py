from typing import List
import sys
import ast


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                last_temperature = stack.pop()
                output[last_temperature[1]] = i - last_temperature[1]
            stack.append((temperature, i))
        return output


def main():
    temperatures = ast.literal_eval(sys.stdin.read().strip())
    Solve = Solution()
    print(Solve.dailyTemperatures(temperatures))


if __name__ == "__main__":
    main()
