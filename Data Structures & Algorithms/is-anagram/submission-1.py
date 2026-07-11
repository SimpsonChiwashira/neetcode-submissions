class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        hashmap = dict()
        for char in s:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1
        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
        for val in hashmap.values():
            if val != 0:
                return False
        return True