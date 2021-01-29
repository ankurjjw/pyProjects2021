import random

print('Please enter you name')
name = input()
print('Hi ' + name + ' , guess the number that I am thinking between 1 and 10.')
print('You have 5 chances to guess the Number.')
secretNumber = random.randint(1, 10)
print(secretNumber)
guessFlag = False
for i in range(5):
    print('Enter the number')
    try:
        guessNum = int(input())
        if guessNum == secretNumber:
            print('Your guess was correct. Congratulations')
            guessFlag = True
            break
        else:
            print('secretnumber ' + str(secretNumber) + ' guessNum ' + str(guessNum))
            print('Wrong guess!')
            continue
    except:
        print('Enter a proper number')

if guessFlag == False:
    print('You exhausted your chances. Correct number was ' + str(secretNumber))
