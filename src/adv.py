from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room["outside"].items.append(Item("Sword", "Sharp"))
room["outside"].items.append(Item("Crystal ball", "Does it work?"))
room["foyer"].items.append(Item("TV", "Big one"))
room["overlook"].items.append(Item("Gameboy", "lol"))
room["narrow"].items.append(Item("Yellow stone", "Yeah!"))
room["treasure"].items.append(Item("Gold coins", "Plenty"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Jonas", room['outside'])

direction = "initial"

while (direction != "q"):
    print(f"Your current room is {player1.room.name}")
    print(f"{player1.room.description}")

    if (len(player1.room.items) == 0):
        print("There are no items in this room... :(")
    else:
        print(f"The items in this room are: {player1.room.items}")
    
    if (len(player1.items) == 0):
        print("You currently have no items... :(")
    else:
        print(f"Your items are: {player1.items}")

    direction = input("What do you want to do?: ")
    directionList = direction.split()

    if len(directionList) == 1:

        if (direction == "q"):
            exit
        
        elif (direction == "n"):
            if (player1.room.n_to is not None):
                player1.room = player1.room.n_to
            else:
                print("*** You cannot move in that direction!")
        
        elif (direction == "s"):
            if (player1.room.s_to is not None):
                player1.room = player1.room.s_to
            else:
                print("*** You cannot move in that direction!")
        
        elif (direction == "w"):
            if (player1.room.w_to is not None):
                player1.room = player1.room.w_to
            else:
                print("*** You cannot move in that direction!")
        
        elif (direction == "e"):
            if (player1.room.e_to is not None):
                player1.room = player1.room.e_to
            else:
                print("*** You cannot move in that direction!")

    elif len(directionList) == 2:

        if directionList[0] == "get" or directionList[0] == "take":
            if len(player1.room.items) == 0:
                print("***** This room has no items!")
            
            else:
                for i in player1.room.items:
                    
                    count = 0

                    if i.name == directionList[1]:
                        player1.items.append(directionList[1])
                        player1.room.items.pop(count)
                    
                    count += 1
    
            print("*** That item is not in this room!")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
