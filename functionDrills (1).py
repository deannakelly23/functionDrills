'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def sub_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 - num2
    return sumOfTwoNumbers
x = sub_two_numbers(4, 5)
print (x)
#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def four_numbers(num1, num2, num3, num4):
    sumOfFourNumbers = num1 / num2 * num3 + num4 
    return sumOfFourNumbers 
x = four_numbers(6,2,77,10000)
print (x)
    
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def check_numbers(num1, num2):
    if(num1 == num2):
        return True
    else:
        return False 
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def bigger_number (num1, num2):
    if (num1 > num2):
        return num1 
    elif (num1 == num2):
        return num1 
    else:
        return num2
#5) Define a function that takes in two words and returns a string that contains both words combined.
def two_words(word1, word2):
    sumOfTwoWords = word1 + word2 
    return sumOfTwoWords
x = two_words("Good", "Bye")
print (x)
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def three_numbers(num1, num2, num3):
    if(num1 == (num2 or num3)):
        return True
    else:
        return False 
#7) Define a function that prints your name.
def my_name(let1, let2, let3, let4, let5, let6):
    sumOfMyName = let1 + let2 +let3 +let4 +let5 +let6
    return sumOfMyName
x = my_name("d", "e", "a", "n", "n", "a")
print (x) 
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def favorite_color (string1):
    if(string1 == "blue"):
        return print ("thats my favorite color")
    elif(string1=="yellow"):
        return print ("That's not my favorite color! Try again")
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def to_zero(num1):
    while num1>-1:
        print(num1)
        num1 = num1 - 1 


#10) Define a function that prints your moms name
def mothers_name(name1, name2, name3):
    sumOfMothersName = name1 + name2 + name3
    return sumOfMothersName
x = mothers_name("annetta", "kay", "hoppe")
print (x)

