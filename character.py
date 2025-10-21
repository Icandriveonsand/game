class Character():
    def fight(self, combat_item):
        return True 
    
    #Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = []
        self.holding_text = None
        self.held = None
        self.talked_to = 0


    #Describe this character
    def describe(self):
        print ( self.name + " is here!")
        print ( self.description )
        
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation.append(conversation)

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation[self.talked_to])
            if self.talked_to != len(self.conversation)-1:
                self.talked_to += 1
        elif  self.talked_to < 0 and self.held:
            print("[" + self.name + " says]: " + self.held_text)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    
    
    
class Enemy(Character):
    def ___init___(self, char_name, char_descrpition):
        super().__init__(char_name, char_descrpition)
        self.weakness = None
        self.fight_text = f"You fend off {self.name} with the {self.weakness}"
        self.failed_fight_text = f"{self.name} crushes you, puny adventurer"

    def fight(self, combat_item):
        if combat_item == self.weakness: 
            print(self.fight_text)
            return True
        else:
            print(self.failed_fight_text)
            return False 

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
        self.want = None

backpack = []

if __name__ == "__main__": 
    laundry_spider =  Enemy("Laundry Spider", "It resembles a spider made from the mutated skin of a human, It's body is concelled under layers of old washing. ")
    laundry_spider.describe()
    laundry_spider.held = "Pennelopes jacket"
    print("What will you fight with?")
    fight_with = input(">> ")
    laundry_spider.fight(fight_with) 

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You distract " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " grabs you, stuffing you in a washing machine. You're dead.")
            return False
    laundry_spider.set_weakness("Wilbur's shirt")


    wilbur = Friend("Wilbur", "A teenage boy, looks to be about 17, a lanky tall build with a thoughtless happy grin, clearly still in the clothes he slept in.")
    wilbur.set_conversation("'Yo yo! You're up!'")
    wilbur.set_conversation("'I was starting to think you'd never leave that bed ha' A forced laugh to cover the awkwardness in his truth")
    wilbur.set_conversation("He continues to rumage around the drawes, 'I swear I left that bread some where aroudn here'")

    wilbur.describe()
    wilbur.talk

    charlie = Friend("Charlie", "A younger boy, 12 maybe 13, the resemblance to Wilbur gives him away as his better half, sitting watching brain numbing reruns.")

    caution_tape =  Enemy("Caution tap", "Classic yellow caution tape blocks the laundry shoot")
    caution_tape.describe()

    print("What will you fight with?")
    fight_with = input(">> ")
    caution_tape.fight(fight_with) 

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You cut the " + self.name + " with the " + combat_item + "the tape falls to the floor and you may enter." )
            return True
        else:
            print("It remains still blocking your path.")
    caution_tape.set_weakness("Garden shears")

    rat = Enemy("A BIG FREAKING RAT", "IT'S HUGE, a rotund RAT, stands on its hind legs as if awaiting your arrival and oh look at that THE BREAD. KILL HIM")
    rat.set_conversation("'Squeek Squeek Bitch.' The rat makes your blood boil.")
    rat.held = "Loaf of Bread"
    rat.want = "Cheese"
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You frisbee throw the " + combat_item + " at the " + self.name + " with perfect aim, the rat catches the cheese dropping the bread and running off." )
            backpack.remove(Enemy.want)
            backpack.add(Enemy.held)
            Enemy.held = None
            return True
        else:
            print("ITS TOO STRONG!")
    rat.set_weakness("Cheese")


