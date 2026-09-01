class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        length = len(numbers)
        for i in range (length):
            for j in range (length):
                if numbers[j] == numbers[i]:
                    continue
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
