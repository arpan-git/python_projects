import random
def main():
    usernum = int(input("Guess a number\n"))                                          # Taking input from the user
    num = random.randint(1,100)                                                       # Here computer choose a random number 
    while True:
        if usernum == num: 
            print ("You have guessed the number\n")
            break
        else:
            print ("You guessed wrong number \n")
            to_display_hint = display_hint(num, usernum)
            print("Hint : " , to_display_hint)
            usernum = int(input("Guess a number\n"))

def display_hint(num,usernum):       
    c = 0
    hint = hints(num, usernum)                                                     # Executing "hints" function and getting list of hints
    to_display_hint = (hint[random.randint(0,4)])                                  # Displaying a random hint from a list
    displayed_hints = []
    while c == 0:
        if to_display_hint in displayed_hints:
            hint = hints(num, usernum)
            to_display_hint = (hint[random.randint(0,4)])
        else:
            displayed_hints.append(to_display_hint)
            break
    return to_display_hint
            


def hints(num, usernum):                                                                                # Function to make a list of different hints
    hint = []
    gors = GreaterOrSmaller(num, usernum)
    greaternum = greaternumbers(num)
    greaternum_hint = greaternum[random.randint(0, len(greaternum)-1)]
    smallernum = smallernumbers(num)
    smallernum_hint = smallernum[random.randint(0, len(smallernum)-1)]
    divnum = divisible(num)
    divnum_hint = divnum[random.randint(0, len(divnum)-1)]
    mulnum = multiple(num)
    mulnum_hint = mulnum[random.randint(1, len(mulnum)-1)]
    hint.append(gors)
    hint.append(greaternum_hint)
    hint.append(smallernum_hint)
    hint.append(divnum_hint)
    hint.append(mulnum_hint)
    return hint


def GreaterOrSmaller(num, usernum):                                               # Function to check whether the user input number is greater or smaller than the number to be guessed
    if num < usernum:
        gors = "You guessed number greater than actual number "
    else:
        gors = "You guessed number lesser than actual number "
    return gors


def greaternumbers(num):                                                          # Function to return a list of numbers greater than actual number
    initial_num = num+1
    greaternum =[]
    for i in range(initial_num, 100):
        data = "Actual number is smaller than " + str(i)
        greaternum.append(data)
    return greaternum


def smallernumbers(num):                                                          # Function to return a list of numbers smaller than actual number
    final_num = num-1
    smallernum =[]
    for i in range(0, final_num):
        data = "Actual number is greater than " + str(i)
        smallernum.append(data)
    return smallernum 


def divisible(num):                                                               # Function to return a list of numbers which can exactly divide the actual number
    divnum =[]
    final_value = num - 1
    for i in range(1, final_value):
        if num % i == 0:
            data = "Actual number is divisible by " + str(i)
            divnum.append(data)
    return divnum


def multiple(num):                                                                # Function to return a list of multiples of actual number
    mulnum =[]
    for i in range (1, 10):
        mul = num * i
        data = "Multiple of actual number is " + str(mul)
        mulnum.append(data)
    return mulnum

if __name__ == '__main__':
    main()
