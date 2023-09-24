"""
#Assinment: Here given a number range o to 100, 
Please print it to the screen:
1. Show how many Odd number in above this range
2. show all odd number sumation result

"""


totalOddNumber_sumOfrange=0

oddNumberList=[]

for number in range(101):
    
    #To find odd number we use modulus is not equal to zero method.

    if number % 2 !=0:
        oddNumberList.append(number)
        totalOddNumber_sumOfrange+=number

print('Total Odd number list in given range:',oddNumberList)
print('\n')
print('Total Sumation of Odd Number in given range:',totalOddNumber_sumOfrange)


