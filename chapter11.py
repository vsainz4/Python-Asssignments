#There are 90 values with a sum=445833

import re
hand = open ('regex_sum_42.txt')
sum = 0
for line in hand:
    line =line.rstrip()
    #print (line)
    numbers = re.findall ('[0-9]+', line)
    #if len(numbers)>0: print(numbers)
    for number in numbers:
        sum = sum + int(number)
print('the sum is', sum)
