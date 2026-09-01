class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: count how many times each number appears
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # counts now looks like: {1: 3, 2: 1, 3: 2}
        # meaning "1 appeared 3 times, 2 appeared once, 3 appeared twice"

        # Step 2: pick the k numbers with the highest counts
        result = []
        for i in range(k):
            best_num = None
            best_count = -1
            for num in counts:
                if counts[num] > best_count:
                    best_count = counts[num]
                    best_num = num
            result.append(best_num)
            del counts[best_num]   # remove it so we don't pick it again

        return result