money = 0
mop = []

inventory = {
    "rusty scissors" : 5,
    "push lawnmower" : 25,
    "battery powered lawnmower" : 100,
    "starving students": 500,  
}

def lvl1():
    choice = input("""
                   A - Chew Grass
                   B - Buy scissors
                   What do you do? > 
                   """)
    if choice.upper() == 'A':
        global money
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
    choice = input(
        """
        A - Cut Grass w Scissors
        B - Buy push lawnmower
        What do you do? >
        """
        )
    if choice.upper() == "A":
        global money
        money += 5
        print(f"{money}$ in the bank!")


def engine():
    while len(mop) == 0:
        lvl1()
    while len(mop) == 1:
        lvl2()
engine()