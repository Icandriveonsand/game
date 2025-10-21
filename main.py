from room import Room
from character import Enemy, Friend
from RPGinfo import RPGInfo
from item import Item

grommet_cup = RPGInfo("Grommet Cup")
grommet_cup.welcome()
RPGInfo.info()

RPGInfo.author = "Raspberry Pi Fontation"

pennelopes_room = Room("Pennelopes Room") 
pennelopes_room.set_description("The bed you left lay's still warmed and unmade against the back wall. The walls unseeable behind in bookselfs covered in books and memorobilla.")
bedroom_hallway = Room("Bedroom hallway")
bedroom_hallway.set_description("A hallways lined with mismatching doors, one stands out as a laundry disposaple locked up with caution tape. A stair case at the end of the hall leads towards a light downstairs")
lounge_room = Room("Lounge Room")
lounge_room.set_description("A long room, bookselves lining one side with a tv standing infront blasting reruns, one boy sits on the beanchair watching.")
kitchen = Room("Kitchen")
kitchen.set_description("In it stands a teenage boy rummaging through the mismatched cupboards, across the counter spread a mess of food and dishes.")
wilburs_room = Room("Wilbur's Room")
wilburs_room.set_description("A cramped room, the floor unseeable underneath the heeps of clothes that lead towards a unframed matteress, old band posters dangle unsticking from the slanted ceiling.")
tea_room = Room("The Tea Room")
tea_room.set_description("A wide dome shaped room, all inside consists of a small table and chairs adorned with a tea set, one wall lined with giant glass windows out of which you can see a florishing garden, by the windows lays some gardening tools.")
foyer = Room("The foyer")
foyer.set_description("A small space at the bottom on the spiralled stairs, the golden rays from the front door just hit your feet, tv noises blaring from the constantly on tv, a singlarly lit hallway looms behind")
laundry_hallway = Room("Laundry Hallway")
laundry_hallway.set_description("A single spitting bulb lights the hall leading to the heavy wooden laundry door.")
laundry_disposale = Room("Laundry disposale")
laundry_disposale.set_description("")
laundry = Room("The Laundry")
laundry.set_description("")
entrance = Room("The Hallway to the Exit")
entrance.set_description("A seemingly short hallway, at the end, a wooden door with one singlar stain glass pain, shining golden rays of light down the walk, the door mat infront reads keep trying.")
pantry = Room("Pantry")
pantry.set_description("")

laundry_disposale.lock()
print("The are " + str(Room.number_of_rooms) + " rooms to explore.")

pennelopes_room.link_room(bedroom_hallway, "exit")
bedroom_hallway.link_room(pennelopes_room, "enter")
bedroom_hallway.link_room(laundry_disposale, "west")
laundry_disposale.link_room(bedroom_hallway, "east")
bedroom_hallway.link_room(foyer, "down")
foyer.link_room(bedroom_hallway, "up")
foyer.link_room(lounge_room, "west")
foyer.link_room(entrance, "south")
foyer.link_room(laundry_hallway, "south")
foyer.link_room(tea_room, "east")
lounge_room.link_room(foyer, "east")
lounge_room.link_room(kitchen, "north")
lounge_room.link_room(wilburs_room, "west")
entrance.link_room(foyer, "north")
entrance.link_room(entrance, "south")
kitchen.link_room(lounge_room, "south")
kitchen.link_rooms(pantry, "east")
wilburs_room.link_room(lounge_room, "west")
tea_room.link_room(foyer, "west")
laundry_hallway.link_room(foyer, "north")
laundry_disposale.link_room(laundry, "enter")

charlie = Friend("Charlie", "A younger boy, 12 maybe 13, the resemblance to Wilbur gives him away as his better half, sitting watching brain numbing reruns.")
charlie.set_conversation = "'What?'"
charlie.set_conversation = "The boy stares of at the screen barely giving you a glance as you stand awaiting a converstation never to happen"
lounge_room.set_character(charlie)

laundry_spider =  Enemy("Laundry Spider", "It resembles a spider made from the mutated skin of a human, It's body is concelled under layers of old washing. ")
laundry.set_character(laundry_spider)

arvam = Friend("Arvam", "The houses closest thing to a parent, a man late thirties, Arvam stands tall dreessed from head to toe in a long coat, at the bottom of which his feet are adorned with pink rabbit slippers.")
arvam.set_conversation("'Pennelope! I'm so glad to see you up, in honest I was starting to- Jacket? Oh yes, that I threw it into the laundry, dont worry youll have it back soon enough! Why? Well you do know how it smelt right..'")
arvam.set_conversation("'What do you mean get it back? You will, it just needs to be cleaned first and I- No I wont go get it for you, it will hardly be a day hold your horses.'")
arvam.set_conversation("'Now that you're up would you care to chat over some tea maybe?' You stand silent 'I'll take that as a no..'")
tea_room.set_character(arvam)


wilbur = Friend("Wilbur", "A teenage boy, looks to be about 17, a lanky tall build with a thoughtless happy grin, clearly still in the clothes he slept in.")
wilbur.held = "Wilbur's Room Key"
wilbur.held_text =  "God I'm starved dude."
wilbur.want = "Loaf of Bread"
wilbur.set_conversation("'Yo yo! You're up!'")
wilbur.set_conversation("'I was starting to think you'd never leave that bed ha' A forced laugh to cover the awkwardness in his truth 'Anyway! I'm just making myself lunch, let's talk later'")
wilbur.set_conversation("He continues to rumage around the drawes, 'I swear I left that bread some where around here' he says in a low grumble to himself")
kitchen.set_character(wilbur)

rat = Enemy("A BIG FREAKING RAT", "IT'S HUGE, a rotund RAT, stands on its hind legs as if awaiting your arrival and oh look at that THE BREAD. KILL HIM")
rat.set_conversation("'Squeek Squeek Bitch.' The rat makes your blood boil.")
rat.held = bread
pantry.set_character(rat)

caution_tape =  Enemy("Caution tap", "Classic yellow caution tape blocks the laundry shoot")
shears = Item("Garden Shears", "Red handled gardening shears, the metal slightly rusted by years of use")
wilburs_shirt = Item("Wilbur's Shirt", "A yellow tinted baggy shirt, stained with mysterious sauces, it smells of a dying carcass")
bread = Item("Loaf of Bread", "A loaf of good ol white bread" )
wilburs_key = Item("Wilbur's Room Key"," A small yellow key, slightly bent, in messy sharpie reads Wilburs Room, upon closer look you can see its covering an engraving reading R1")
cheese = Item("Cheese", "Think that small cheese snack pack that comes with crackers.. except someone ate all the crackers..")
kitchen.set_item(cheese)
pennelopes_jacket = Item("Pennelopes Jacket", "")
laundry_spider.held = pennelopes_jacket


current_room = pennelopes_room
backpack = []

while True:
    if bedroom_hallway.character != caution_tape:
        laundry_disposale.unlock()
    
    "This is the infinate game loop"
    print('\n') # this prints 
    current_room.describe()


    command = input('> ')

    if command == 'give':
        if inhabitant.want in backpack:
            backpack.remove(inhabitant.want)
            backpack.remove(inhabitant.held)
            inhabitant.held = None
    
    current_room = current_room.move(command)

    dead = False
    while dead == False:
        print("\n")         
        current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    if command in ["north", "south", "east", "west", "down", "up", "enter", "exit"]:
        current_room = current_room.move(command)
    
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
       
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in (item.name for item in backpack):
                if inhabitant.fight(fight_with) == True:
                    print("You won, you feel taken aback by your capabilities")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You won, you feel stronger than this morning")
                        dead = True
                else:
                    print("You lost")
                    print("That's your end.. maybe try waking up again")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")  

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in pockets")
            backpack.append(item)
            current_room.set_item(None)



    RPGInfo.credits()