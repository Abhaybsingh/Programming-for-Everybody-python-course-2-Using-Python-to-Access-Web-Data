# Extracting Data With Regular Expressions


# answer 445833

import re
hand  = open('file2.txt')
sum = 0
lst = list()
for line in hand:
    line1 = line.rstrip()
    #print(line)
    lst = re.findall('[0-9]+',line1)
    for j in lst:
        sum = sum + int(j)
print(sum)
