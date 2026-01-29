class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d={}
        d2={}
        
        
        for tt in t:
            if tt in d:
                d[tt]+=1
            else:
                d[tt]=1
        
        
         
         
        for ss in s:
            if ss in d2:
                d2[ss]+=1
            else:
                d2[ss]=1
        
        
         
         
         
        if d==d2: # here ww are comparing the dictionary 
             return True
        else:
             return False
        