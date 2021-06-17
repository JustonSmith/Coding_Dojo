# 
# 
# 
#   - OOP
#     -classes
#     -attributes & methods
#     -constructor
#     -instances
#     -self
#     -chaining
#     -inheritance

class Pacman(object):
    def __init__(self):
        self.pacman = "Pacman"
        self.location = [0,0]

    def move(self, direction):
        self.location[0] + 1
        return self


new_game_one = Pacman() # instance of Pacman class
new_game_one.move("North")
print (new_game_one.location)

new_game_two = Pacman()
print (new_game_two.location)

new_game_two.move("south").move("east")



