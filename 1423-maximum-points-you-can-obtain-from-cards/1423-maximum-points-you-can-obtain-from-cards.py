class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s=maxi=0
        for i in range(k):
            s+=cardPoints[i]
        maxi=s
        r=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            s-=cardPoints[i]
            s+=cardPoints[r]
            r-=1
            maxi=max(maxi,s)
        return maxi