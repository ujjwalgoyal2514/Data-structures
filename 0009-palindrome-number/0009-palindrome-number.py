class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        r=0
        n=x
        while n!=0:
            r=r*10+(n%10)
            n//=10
        if r==x:
            return True
        return False