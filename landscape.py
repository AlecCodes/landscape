money = 0
mop = ''

inventory = {
    "rusty scissors" : 5,
    "push lawnmower" : 25,
    "battery powered lawnmower" : 100,
    "starving students": 500,  
}

def lvl1():
    choice = input("""
                   A - Chew Grass
                   B - Go to STore
                   What do you do? > 
                   """)
    if choice.upper() == 'A':
        global money
        money += 1
        print(f"{money}$ in the bank!")



def engine():
    while mop == '':
        lvl1()
        
engine()