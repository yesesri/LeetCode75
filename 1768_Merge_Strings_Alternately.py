class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string    = str()
        min_l = min(len(word1),len(word2))  
        for i in range(0, min_l ) : 
            merged_string+=word1[i]
            merged_string+=word2[i]
        ####
        if(len(word1)!=len(word2)) : 
            if ( len(word1) > len(word2) ) :  merged_string+=word1[min_l :]
            else :  merged_string+=word2[min_l :]
        ###
        return(merged_string)
    ###
