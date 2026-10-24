import pgzrun

WIDTH, HEIGHT=400,400 
TITLE="Circles"

def draw():
    ra=200
    r = 16
    g = 0
    b = 255

    for i in range(25):
        screen.draw.filled_circle((200,200), ra, (r,g,b))
        ra-=7
        r += 5
        g += 8
        b -=10
        



pgzrun.go()