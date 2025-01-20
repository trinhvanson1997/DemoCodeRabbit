"""
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagramWay1(self, s: str, t: str) -> bool:
        """
        sort two array of characters and compare arrays
        space: O(n)
        time: O(nlogn)
        """
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
    
    
    def isAnagramWay2(self, s: str, t: str) -> bool:
        """
        use hashmap to store number occurence of each character in two string
        traverse through seen dict, if there is non-zero number -> return false
        
        space: O(26)
        time: O(n)
        """
        seen = dict()
        for charS in s:
            seen[charS] = 1 if charS not in seen else seen[charS]+1
        
        for charT in t:
            seen[charT] = 1 if charT not in seen else seen[charT]-1
        
        for count in seen.values():
            if count != 0:
                return False
        return True
    
    
    def isAnagramWay3(self, s: str, t: str) -> bool:
        """
        Because, there is only English lowercase character in string, so we can store frequency of each character
        in 26-elements array (a -> z)
        
        space: O(26)
        time:  O(n) faster than way 2
        """
        fre = [0] * 26
        for charS in s:
            fre[ord(charS) - ord('a')] += 1
        
        for charT in t:
            if fre[ord(charT) - ord('a')] == 0:     # immediately return result when catch mismatch character -> faster than way 2
                return False
            fre[ord(charT) - ord('a')] -= 1
            
        return True
            

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    
    s = "rat"
    t = "car"
    
    solution = Solution()
    print(solution.isAnagramWay1(s, t))
    print(solution.isAnagramWay2(s, t))
    print(solution.isAnagramWay3(s, t))
