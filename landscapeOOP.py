inventory = {
    "teeth" : 1,
    "rusty scissors" : 5,
    "push lawnmower" : 25,
    "battery powered lawnmower" : 100,
    "starving students": 500,  
}

class level:
    bankaccount = 0
    def __init__(self, tool, next_tool):
        self.tool = tool
        self.next_tool = next_tool
    
    
    @classmethod
    def work(cls, self):
        cls.bankaccount += inventory[self.tool]

    
    def game(self):
        choice = input("""
                    A - Cut Grass with {gear}
                    B - Buy {next}
                    What do you do? > 
                    """.format(gear = self.tool, next = self.next_tool) )
        if choice.upper() == "A":
            level.work(self)
            print(f"{level.bankaccount} dollars in bank account!")
        #else if choice.upper() == "B":
            
            
             
    

def engine():
    lvl1 = level("teeth", "rusty scissors")
    while lvl1.tool == "teeth":
        lvl1.game()

engine()