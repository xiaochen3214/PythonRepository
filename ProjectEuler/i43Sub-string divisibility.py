# Sub-string divisibility
# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

import time
from termcolor import colored

def isPandigital(string):
    thelen = len(string)
    # print(string,'thelen=', thelen)
    for i in range(1, thelen+1):
        # print('str(i)=', str(i))
        if str(i) not in string:
            return False
    if thelen > 9:
        return False
    return True

def main_process():
    prossibles = []
    for i in range(1,1000// 11 + 1):
        temp = str(11 * i)
        if len(temp) == 2:
            temp = '0' + temp
        # print('before:',temp)
        for j in range(0,10):
            # print('int(temp[1:]):',int(temp[1:]))
            tempj = int(temp[1:]+ str(j) )
            # print('tempj:',tempj)            
            if tempj % 13 == 0:
                temp1 = temp + str(j)
                # print('temp1 % 13:',temp1,'tempj=',tempj)                
                for k in range(0,10):
                    tempk = int(temp1[2:]+ str(k) )
                    if tempk % 17 == 0:
                        temp2 = temp1 + str(k)
                        print('temp2 % 17 :',temp2)


    print(colored('mycount=', 'red'), '#')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)