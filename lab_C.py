print("----------------Program 01----------------")
i= int(1500)
for i in range(i,2700):
    if (i % 7==0 and i%5==0):
        print(i," is divisible by 7 and Multiple of 5. ") 
    else:
        continue 
print("----------------Program 02----------------")
choice=input("Enter 1 for Temprature find in Celsius: 2 for Temprature find in Fahrenheit:")
if(int(choice)==1):
    temp=input("Enter the temperature in Fahrenheit:")
    celsius=((int(temp)-32)/9)*5
    print("The temperature in celsius is :",celsius)
if(int(choice)==2):
    temp=input("Enter the temperature in celsius:")
    Fahrenheit=((int(temp)/5)*9)+32
    print("Enter the temperature in Fahrenheit is :",Fahrenheit)
print("----------------Program 03----------------")
import random
i=True
while (i==True):
    num=int(input("Enter a number between 1 and 9:"))
    num1=random.randint(1,9)
    if(num==num1):
        print("you guessed the number:",num1)
        i=False
    else:
        print("you not guessed the number:",num1)
        print("Try Again!!!!!")
        i=True
        continue 
print("----------------Program 04----------------")
for i in range(5):
    for j in range(i + 1):
            print("*", end=" ")
    print()
for i in range(5 - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
print("----------------Program 05----------------")
word=input("Enter a word:")
print(word[::-1])       
print("----------------Program 06----------------")
series=input("Enter the Number series space seprated:").split()
series=[int(num) for num in series]  
even_count=0
odd_count=0
for num in series:
    if(num%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Number of even numbers:",even_count)
print("Number of odd numbers:",odd_count)
print("----------------Program 07----------------")
#Sample list
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print(f"Item: {item} - Type: {type(item)}")
print("----------------Program 08----------------")
for num in'0123456':
    if num=='3' or num=='6':
        continue
    print(num)
print("----------------Program 09A----------------")
a, b = 0, 1
series = []
while a <= 50:
        series.append(a)
        a, b = b, a + b
print(series[0::])
print("----------------Program 09B----------------")
num=int(1)
for i in range(num,50):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
print("----------------Program 10----------------")
m=int(input("Enter the numbers of Rows:"))
n=int(input("Enter the numbers of Columns:"))
array=[]
for i in range(m):
    row=[]
    for j in range(n):
        value=i*j
        row.append(value)
    array.append(row)
for row in array:
    print(''.join (map(str,row)))
print("----------------Program 11----------------")
print("Enter input lines. To end, just press Enter on a blank line:")
inputs = []
while True:
    line = input()
    if line == "":
        break
    inputs.append(line.lower())
for i in inputs:
    print(i)
print("----------------Program 12----------------")
def binary_divisible_by_5(sequence):
    numbers = sequence.split(',')
    divisible_by_5 = []
    for number in numbers:
        decimal = int(number, 2)
        if decimal % 5 == 0:
            divisible_by_5.append(number)
    print(','.join(divisible_by_5))
input_sequence = '0100,0011,1010,1001,1100,1001'
binary_divisible_by_5(input_sequence)

print("----------------Program 13----------------")
string=input("Enter a string:")
letters=0
digits=0
for i in string:
    if i.isalpha():
      letters=letters+1    
    elif i.isdigit():
        digits=digits+1
print("letters:",letters)
print("Digits:",digits)
if(letters==0 and digits==0):
    print("There is No letters and digits in the string")
print("----------------Program 14----------------")
password = input("Enter the password:")
has_lower = False
has_upper = False
has_digit = False
has_special = False
special_characters = "$#@"
count = len(password)
for char in password:
    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True
if (count == 6 or count <= 16) and has_lower and has_upper and has_digit and has_special:
    print("You entered the correct password according to rules")
else:
    print("Password does not meet the criteria")
