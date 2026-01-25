class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        st=[]
        stc=[]
        
        for c in s:
            if c=="#":
                st.pop()
            else:
                st.append(c)
        SUM1= "".join(st)
        
        
        for a in t:
            if a=="#":
                stc.pop()
            else:
                stc.append(a)
        SUM2="".join(stc)
    
        if  SUM1==SUM2:
            return True
        else:
            return False
    
