class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

      # # Find the maximum number of candies
        maxCandy = max(candies)
        result = []
       # Iterate through each kid's candy count
        for n_candy in candies :  
          # Check if the kid's new total is greater than or equal to the maximum
            if(  (n_candy+extraCandies) < maxCandy  ) : result.append( False )
            else : result.append(True ) 
            ####
        ####
        return(result)
    
