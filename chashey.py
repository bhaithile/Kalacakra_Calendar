# I want to repeat the certain number of the range and continue till the range end

a = 7
for num in range(1, 13):
   print(num)
   if a in [7,29]: # this is the case 
       print(num +1)
   else:
        continue 

# expected result:
# 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12

# in here 7 is repeated because the a value matches 
