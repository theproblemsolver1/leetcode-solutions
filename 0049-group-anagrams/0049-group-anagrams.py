class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}

        for word in strs:

            freq={}

            for ch in word:

                if ch in freq:
                    freq[ch]+=1
                else:
                    freq[ch]=1

              


            key=tuple(sorted(freq.items()))


            if key not in res:
                res[key]=[]
            res[key].append(word)


        return list(res.values())
        