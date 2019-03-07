def float_bin(number): 
    #split the number
    whole, dec = str(number).split(".") 
    
    #convert all vals to integers
    whole = int(whole) 
    dec = int (dec) 
   # turn to string and format 
    whole = '{:b}.'.format(whole)
    dec = '{:b}'.format(dec)
    dec = dec[::-1]
    result = whole + dec
    return result

