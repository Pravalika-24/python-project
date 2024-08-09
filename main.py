import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f'it is between 1 and {x}'))
        if  (guess<random_number):
            print("try again and its too low")
        elif (guess> random_number):
            print("try again and its too high")

    print(f'congrats u guessed correctly {random_number}')   
guess(10)
