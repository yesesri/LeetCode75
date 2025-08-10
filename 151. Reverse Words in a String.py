class Solution:
    def reverseWords(self, s: str) -> str:
        #split the string
        s_list = s.split()
        #reverse() - reverses the list in place ( return value is none, so first reverse then join )
        s_list.reverse()
        return " ".join(s_list) 
