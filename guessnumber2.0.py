import random

def guess(x):
    print("THINK OF A NUMBER IN YOUR HEAD AND START PLAYING BELOW!! \n")
    low = 1
    high = x
    feedback = " "
    while feedback != "C":
        guess = random.randint(low,high)
        print(guess)
        feedback = input("Too High (H), Too Low (L), Correct(C)").upper()

        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
        else:
            feedback == "C"
            print(f"you guessed my number: {guess}")

guess(1000)



