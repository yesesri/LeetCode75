class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       #initialize  number of plants plotted 
        n_plant_plotted = 0
        # store length of flowerbed array.
        n_plots  = len(flowerbed)
        #index to iterate flowerbed array 
        i = 0 
        #loop through flower bed to checl for space to plot plant
        while ( i < n_plots ): 
            #check if current spot is empty 
            if(flowerbed[i] == 0 ) : 
                #check if left and right plots are empty as they cannopt be adjacent. 
                is_left_empty  = ( i == 0  or flowerbed[i-1] == 0 )
                is_right_empty = (i== (n_plots - 1) or flowerbed[i+1] == 0 )
                if( is_left_empty and is_right_empty )  : 
                    i+=2
                    n_plant_plotted+=1
                    # early exit since plotting for all the plants are checked. 
                    if( n_plant_plotted  >= n )  : return ( True )
                else : 
                    # move to next plot since roght and left are not empty
                    i+=1
            # cuurent spot in not empty so skip two as left should be empty. 
            else : 
                i+=2
            ### end of if check 
        ### end of while loop 
        #return false 
        return ( n_plant_plotted  >= n )
    #### end of function

               
            
                

                

