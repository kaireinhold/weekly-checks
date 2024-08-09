import random

def roll_d2():
    global rolld2
    global d2
    d2 = [1, 2]
    rolld2 = random.choice(d2)
    if rolld2 == 1:
        print("D2: Critical Fail!")
    else:
        print("D2: Critical Success!")
roll_d2()

def roll_d4():
    global rolld4
    global d4
    d4 = [1, 2, 3, 4]
    rolld4 = random.choice(d4)
    if rolld4 > 0:
        print("D4: You rolled a " + str(rolld4) + "!")
roll_d4()

def roll_d6():
    global rolld6
    global d6
    d6 = [1, 2, 3, 4, 5, 6]
    rolld6 = random.choice(d6)
    if rolld6 > 0:
        print("D6: You rolled a " + str(rolld6) + "!")
roll_d6()

def roll_d8():
    global rolld8
    global d8
    d8 = [1, 2, 3, 4, 5, 6, 7, 8]
    rolld8 = random.choice(d8)
    if rolld8 == 8:
        print("D8: You rolled an " + str(rolld8) + "!")
    else:
        print("D8: You rolled a " + str(rolld8) + "!")
roll_d8()

def roll_d10():
    global rolld10
    global d10
    d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rolld10 = random.choice(d10)
    if rolld10 == 8:
        print("D10: You rolled an " + str(rolld10) + "!")
    else:
        print("D10: You rolled a " + str(rolld10) + "!")
roll_d10()

def roll_d12():
    global roll12
    global d12
    d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rolld12 = random.choice(d12)
    if rolld12 == 8:
        print("D12: You rolled an " + str(rolld12) + "!")
    elif rolld12 == 11:
        print("D12: You rolled an " + str(rolld12) + "!")
    else:
        print("D12: You rolled a " + str(rolld12) + "!")
roll_d12()

def roll_d20():
    global rolld20
    global d20
    d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    rolld20 = random.choice(d20)
    if rolld20 == 1:
        print("D20: Critical Fail!")
    elif rolld20 == 20:
        print("D20: Critical Success!")
    elif rolld20 == 11:
        print("D20: You rolled an " + str(rolld20) + "!")
    elif rolld20 == 18:
        print("D20: You rolled an " + str(rolld20) + "!")
    elif rolld20 == 8:
        print("D20: You rolled an " + str(rolld20) + "!")
    else:
        print("D20: You rolled a " + str(rolld20) + "!")
roll_d20()

def roll_d100():
    global rolld100
    global d100
    d100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    rolld100 = random.choice(d100)
    if rolld100 == 8:
        print("D100: You rolled an " + str(rolld100) + "!")
    elif rolld100 == 11:
        print("D100: You rolled an " + str(rolld100) + "!")
    elif rolld100 == 18:
        print("D100: You rolled an " + str(rolld100) + "!")
    elif rolld100 >= 80 and rolld100 <= 89:
        print("D100: You rolled an " + str(rolld100) + "!")
    else:
        print("D100: You rolled a " + str(rolld100) + "!")
roll_d100()
