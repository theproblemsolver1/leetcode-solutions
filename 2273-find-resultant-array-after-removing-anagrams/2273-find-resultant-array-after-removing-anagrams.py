class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        res=[]
        prev=None
        
        for word in words:
            freq={}
            for ch in word:
                 if ch in freq:
                     freq[ch]+=1
                 else:
                     freq[ch]=1 


        
            if freq!=prev:
                res.append(word)
                prev=freq


        return res
        