
class Room():
    number_of_rooms
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}

        self.character = None
        self.locked = False
        


    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description
    
    def set_name(self, room_name):
        self.name = room_name
    
    def lock(self):
        self.locked = True

    def unlocked(self):
        self.locked = False

    def set_character(self, character_name):
        self.character = character_name

    def get_name(self):
        return self.name

    def get_details(self):
         for direction in self.linked_rooms:
              room = self.linked_rooms
              print( "The " + room.get_name() + " is " + direction)

    def describe(self):
        print( self.description )
        for direction in self.linked_rooms:
            print(f'{self.linked_rooms[direction].name}  is to the {direction}')
    
    def link_room(self, room_to_link, direction):

        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        if direction in self.linked_rooms:
            if not self.linked_rooms[direction].locked:
                return self.linked_rooms[direction]
            else:
                print("Locked.")
            return self
    
        else:
            print("You can't go that way.")

        


if __name__ == "__main__":
    #This condtional will only allow the code written here to run if we run room.py
    pennelopes_room = Room("Pennelopes Room") # This is an instance of a room called "Kitchen"
    bedroom_hallway = Room("Bedroom hallway")
    lounge_room = Room("Lounge Room")

    pennelopes_room.set_description("The bed you left lay's still warmed and unmade against the back wall. The walls unseeable behind in bookselfs covered in books and memorobilla.")
    bedroom_hallway.set_description("A hallways lined with mismatching doors, one stands out as a laundry disposaple locked up with caution tape. A stair case at the end of the hall leads towards a light downstairs")
    lounge_room.set_description("A long room, bookselves lining one side with a tv standing infront blasting reruns, one boy sits on the beanchair watching.")


    print(pennelopes_room.name) # this line calls the name attribute
    print("_____________")
   # print(kitchen.get_description()) # this line calls the get_descriiption methouhd

    pennelopes_room.link_room(bedroom_hallway, 'south') #this is add "south": dining_hall to dictionary linked_rooms
    print(pennelopes_room, )

"""
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = None
        self.link_rooms = {}
        self.locked = False

def lock(self):
    self.locked = True

def unlock (self):
    self.locked = False

def move(self, direction):
    if direction in self.linked_rooms:
        if self.linked_room['direction'].locked:
            print("You can't go there. Door is locked")
            return self
    else:
        return self.linked_rooms['direction']
"""