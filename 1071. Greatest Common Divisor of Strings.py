class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # check compatibility 
        if( (str1+str2) == (str2+str1) ) :
            #GCD of integers using eucledian distance
            gcd_len = gcd(len(str1) , len(str2))
            #gcd string
            return(str1[:gcd_len])
        else : 
            return ""
        ####
    ####
#####
