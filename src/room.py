# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description): 
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'
    
    def n_to(self):
        return self.n_to
    
    def s_to(self):
        return self.s_to

    def e_to(self):
        return self.e_to

    def w_to(self):
        return self.w_to