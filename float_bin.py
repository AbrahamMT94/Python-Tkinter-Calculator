def float_bin(number,precision=4): 
    #split the number
   whole, dec = str(float(number)).split(".") 
    
    #convert whole to binary
   whole = '{:b}'.format(int(whole))
   dec = int (dec) 
   #check ifleft over is 0 and if so retun number 
   if dec==0:
      return whole
   seen_values=[]
   current=dec
   point='.'
   # the loop below keeps adding until precision is met or it loops over
   while current not in seen_values and current!=0 and precision!=0 :
      seen_values.append(dec)
      dec=dec*2
      if dec>=100:
         point+='1'
         dec-=100
         current=dec
      else :
         point+='0'
         current=dec
      precision-=1     

   return whole+point
