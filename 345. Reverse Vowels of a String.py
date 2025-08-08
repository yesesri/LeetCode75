class Solution:
    def reverseVowels(self, s: str) -> str:
        #using two pointer method to identify and swap vowels.
        s_list    = list(s)
        #space complexity only O(1) so best to create vowel set to check. 
        vowel_set = set ( "aeiouAEIOU")
        #starting position
        left_pointer = 0 
        #since python index start at 0 
        right_pointer = len(s_list) - 1 
        while left_pointer < right_pointer : 
            #move left pointer until it reach an vowel character 
            while  left_pointer < right_pointer  and s_list[left_pointer] not in vowel_set  : 
                left_pointer+=1
            #move right pointer until it reach an vowel character 
            while  left_pointer < right_pointer and s_list[right_pointer] not in vowel_set : 
                right_pointer-=1
            # swap vowels, if right and left do not cross yet.
            if( left_pointer < right_pointer) : 
                s_list[ left_pointer ],s_list[right_pointer ] = s_list[right_pointer ],s_list[ left_pointer ]
                left_pointer+=1
                right_pointer-=1
        #### left and right cross , exit and return the string with swapped vowels. 
        return( "".join(s_list))
            
