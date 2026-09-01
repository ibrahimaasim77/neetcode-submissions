class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
        s = clean 
        
        left = 0
        right = (len(s) - 1)
        length = len(s) // 2
        for i in range (length):
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False  
          
        return True
