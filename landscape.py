money = 0
mop = []

inventory = {
    "rusty scissors" : 5,
    "push lawnmower" : 25,
    "battery powered lawnmower" : 100,
    "starving students": 500,  
}

def lvl1():
    global money
    choice = input("""
                   A - Chew Grass
                   B - Buy scissors
                   What do you do? > 
                   """)
    if choice.upper() == 'A':
        money += 1
        print(f"{money}$ in the bank!")
    if choice.upper() == "B":
        if money < 5:
            print('U BROKE')
        else:
            money -= 5
            print("PURCHASED SCISSORS")
            mop.append(1)

def lvl2():
    global money
    choice = input(
        """
        A - Cut Grass w Scissors
        B - Buy push lawnmower
        What do you do? >
        """
        )
    if choice.upper() == "A":
        money += 5
        print(f"{money}$ in the bank!")
    if choice.upper() == "B":
        if money < 25:
            print("Come back when u have 25 quid")
        else:
            money -= 25
            print('PURCHASED A PUSH LAWNMOWER')
            mop.append(1)

def lvl3():
    global money
    choice = input(
        """
        A - Cut Grass w push lawnmower
        B - Buy electic lawnmower
        What do you do? >
        """
        )
    if choice.upper() == "A":
        money += 50
        print(f"{money}$ in the bank!")
    if choice.upper() == "B":
        if money < 25:
            print("Come back when u have 250 quid")
        else:
            money -= 250
            print('PURCHASED A Battery LAWNMOWER')
            mop.append(1)

def lvl4():
    global money
    choice = input(
        """
        A - Cut Grass w battery lawnmower
        B - Hire starving students
        What do you do? >
        """
        )
    if choice.upper() == "A":
        money += 100
        print(f"{money}$ in the bank!")
    if choice.upper() == "B":
        if money < 500:
            print("Come back when u have 500 quid")
        else:
            money -= 500
            print('PURCHASED A TON OF STARVING STUDENTS')
            mop.append(1)

def final():
    global money
    while money < 1000:
        choice = input(
            """
            A - Tell students to work
            """
            )
        if choice.upper() == 'A':
            money += 250
            print(f"{money}$ in the bank!")
    gameover = input("""
                    Game Over! Play again? (y/n) >
                     """)
    if gameover.upper() == 'Y':
        money = 0
        mop.clear()
        engine()
    if gameover.upper() == 'N':
        exit()
        
    
def engine():
    while len(mop) == 0:
        lvl1()
    while len(mop) == 1:
        lvl2()
    while len(mop) == 2:
        lvl3()
    while len(mop) == 3:
        lvl4()
    while len(mop) == 4:
        final()
engine()