class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        n = sorted(list(set(nums)))
        max_count = 1
        running_count = 1

        for i in range(len(n) - 1):
            if n[i+1] - n[i] == 1:
                running_count += 1
            else:
                running_count = 1
            max_count = max(max_count, running_count)
        return max_count