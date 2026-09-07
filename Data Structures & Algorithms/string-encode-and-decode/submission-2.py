class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr=""
        for i in range(0,len(strs)):
            strleni=str(len(strs[i]))
            encodedstr=encodedstr+strleni+"@"+strs[i]
        return encodedstr

    def decode(self, s: str) -> List[str]:
        decodedlist=[]
        i=0
        while i<len(s):
            #Find length
            j=i
            while(s[j]!="@"):
                j+=1
            wordlen=int(s[i:j])
            start=j+1
            end=wordlen+start
            word=s[start:end]
            i=end
            decodedlist.append(word)

        return decodedlist