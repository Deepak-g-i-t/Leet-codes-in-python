class solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]
        
    """  method 2
    
    def isPalindrome(self, x: int) -> bool:
            s=str(x)
            l=0
            r=len(s)-1
            while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
            return True
            
    """
    