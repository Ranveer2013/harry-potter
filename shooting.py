import pgzero,random

WIDHT,HEIGHT = 800,500
harry=Actor("harry potter.png")
harry.pos=400,200

def draw():
    screen.blit("bg.jpg",(0,0))
    harry.draw()



pgzrun.go()

