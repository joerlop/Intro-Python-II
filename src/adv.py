from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Jonas", room['outside'])

print(player1.room.n_to)

for i in range(3):
    if (i == 0):
        print(f"Your current room is {player1.room.name}")

    elif (i == 1):
        print(f"{player1.room.description}")

    else:
        direction = input("Where do you want to go?: ")

        if (direction == "q"):
            exit
        elif (direction == "n"):
            if (hasattr(player1.room, "n_to")):
                player1.room = player1.room.n_to
                print(f"Your current room is {player1.room}")
            else:
                print("You cannot move in that direction!")
        elif (direction == "s"):
            if (hasattr(player1.room, "s_to")):
                player1.room = player1.room.s_to
                print(f"Your current room is {player1.room}")
            else:
                print("You cannot move in that direction!")
        elif (direction == "w"):
            if (hasattr(player1.room, "w_to")):
                player1.room = player1.room.w_to
                print(f"Your current room is {player1.room}")
            else:
                print("You cannot move in that direction!")
        elif (direction == "e"):
            if (hasattr(player1.room, "e_to")):
                player1.room = player1.room.e_to
                print(f"Your current room is {player1.room}")
            else:
                print("You cannot move in that direction!")

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
