#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.
#the sum should end in 850

import re
hand = open ('regex_sum_1491330.txt')
sum = 0
for line in hand:
    line =line.rstrip()
    #print (line)
    numbers = re.findall ('[0-9]+', line)
    #if len(numbers)>0: print(numbers)
    for number in numbers:
        sum = sum + int(number)
print('the sum is', sum)

#the sum is 453850
