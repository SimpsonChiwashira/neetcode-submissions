class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = set()
        for i in range(len(nums)):
            if nums[i] in freq_map:
                return True
            freq_map.add(nums[i])
        return False
