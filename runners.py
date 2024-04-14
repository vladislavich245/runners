from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"), (700,500))
sprite1 = transform.scale(
    image.load('sprite1.png'),
    (100,100))

sprite2 = transform.scale(
    image.load('sprite2.png'),
    (100,100))
x1 = 100
y1 = 330
x2 = 400
y2 = 300
clock = time
speed = 5

game = True
while game:
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 >5:
        x2 -= speed
    if keys_pressed[K_RIGHT] and x1 <395:
        x2 += speed
    if keys_pressed[K_UP] and x1 >5:
        y2 -= speed
    if keys_pressed[K_DOWN] and x1 <395:
        y2 += speed
    if keys_pressed[K_a] and x1 >5:
        x1 -= speed
    if keys_pressed[K_d] and x1 <395:
        x1 += speed
    if keys_pressed[K_w] and x1 >5:
        y1 -= speed
    if keys_pressed[K_s] and x1 <395:
        y1 += speed

    window.blit(background,(0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
