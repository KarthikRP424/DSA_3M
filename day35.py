class Solution(object):
    def isPalindrome(self, s):
        n = 0
        
        for i in s:
            n = n+1

        i = 0
        j = n-1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True
        
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))