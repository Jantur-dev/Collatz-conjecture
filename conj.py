num = int(input('Enter a number : '))
iteration = 0
listNumbers = [num]
"""
if number is odd * 3 + 1
if numbber is even divided by 2
"""
while num !=1:
    iteration += 1
    if num % 2 == 0:
        num = num//2 
    else:
        num = 3*num + 1
    listNumbers.append(num)
print(f'iterations: {iteration}')
print(listNumbers)