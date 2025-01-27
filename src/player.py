# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room): 
        self.name = name
        self.room = room
        self.items = []
    
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f'Player({repr(self.name)}, {repr(self.room)})'
