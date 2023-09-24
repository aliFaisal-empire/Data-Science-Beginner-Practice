#matrix list

A= [['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']]

oddNumber= 0

Column=[]

for totalNumber in range(101):

    if totalNumber % 2 !=0:
        oddNumber+= totalNumber
        Column.append(totalNumber)


print('Column=',Column)

print('For loop on A list all items or element count last showed result is:'
      '\n Column ==>',Column)


# # Initialize a variable to store the sum
# sum_of_odd_numbers = 0
#
# # Loop through numbers from 0 to 100
# for number in range(101):
#     # Check if the number is odd
#     if number % 2 != 0:
#         # If it's odd, add it to the sum
#         sum_of_odd_numbers += number
#
# # Print the sum of odd numbers
# print("The sum of odd numbers from 0 to 100 is:", sum_of_odd_numbers)
#
