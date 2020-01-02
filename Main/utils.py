class location :
    def __init__(self, letter, x, y, z, n):
        self.letter = letter
        self.x = x
        self.y = y
        self.z = z
        self.n = n
    def get_dict (self):
        location = {'letter' :self.letter,
                    'x':self.x,
                    'y':self.y,
                    'z':self.z,
                    'n':self.n}
        return location