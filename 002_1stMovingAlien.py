alien = Actor('alien')

# Play around with the aliens .topright parameter, what do you observe?
alien.topright = 30, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

# Yes, this function is still commented out, once having played around with .pos
# comment this in again and see what happens… but how?
#def update():
#    alien.left += 2
#    if alien.left > WIDTH:
#        alien.right = 0
