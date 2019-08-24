from math import sin,cos

WIDTH = 160
HEIGHT = 80

class Ship:
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.rot = 0

        self.speed = 4
        self.rot_speed = 0.5

    def fd(self):
        self.x += cos(self.rot) * self.speed
        self.y += sin(self.rot) * self.speed
        self.x, self.y = self.wrap(self.x, self.y)

    def rt(self):
        self.rot += self.rot_speed

    def lt(self):
        self.rot -= self.rot_speed

    def draw(self, d):
        self.draw_relative(d, 0,0,-4,4)
        self.draw_relative(d, -4,4,10,0)
        self.draw_relative(d, 10,0,-4,-4)
        self.draw_relative(d, -4,-4,0,0)

    def draw_relative(self, d, x1, y1, x2, y2):
        xa = self.x + x1*cos(self.rot) - y1*sin(self.rot)
        ya = self.y + x1*sin(self.rot) + y1*cos(self.rot)
        xb = self.x + x2*cos(self.rot) - y2*sin(self.rot)
        yb = self.y + x2*sin(self.rot) + y2*cos(self.rot)
        self.draw_line(d,xa,ya,xb,yb)


class ShipTorus(Ship):
    def __init__(self):
        super().__init__()

    def wrap(self, x, y):
        x %= WIDTH
        y %= HEIGHT
        return x,y

    def draw_line(self, d, x1, y1, x2, y2):
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        while x1 < 0 and x2 < 0:
            x1 += WIDTH
            x2 += WIDTH
        while x1 > WIDTH and x2 > WIDTH:
            x1 -= WIDTH
            x2 -= WIDTH
        while y1 < 0 and y2 < 0:
            y1 += HEIGHT
            y2 += HEIGHT
        while y1 > HEIGHT and y2 > HEIGHT:
            y1 -= HEIGHT
            y2 -= HEIGHT

        if x1 > WIDTH or x2 > WIDTH:
            y_split = y1 + (y2 - y1) * (WIDTH - x1) / (x2 - x1)
            if x1 > WIDTH:
                self.draw_line(d, x2, y2, WIDTH, y_split)
                self.draw_line(d, x1-WIDTH, y1, 0, y_split)
                return
            else:
                self.draw_line(d, x1, y1, WIDTH, y_split)
                self.draw_line(d, x2-WIDTH, y2, 0, y_split)
                return
        if x1 < 0 or x2 < 0:
            y_split = y1 + (y2 - y1) * -x1 / (x2 - x1)
            if x1 < 0:
                self.draw_line(d, x2, y2, 0, y_split)
                self.draw_line(d, x1+WIDTH, y1, WIDTH, y_split)
                return
            else:
                self.draw_line(d, x1, y1, 0, y_split)
                self.draw_line(d, x2+WIDTH, y2, WIDTH, y_split)
                return

        if y1 > HEIGHT or y2 > HEIGHT:
            x_split = x1 + (x2 - x1) * (HEIGHT - y1) / (y2 - y1)
            if y1 > HEIGHT:
                self.draw_line(d, x2, y2, x_split, HEIGHT)
                self.draw_line(d, x1, y1-HEIGHT, x_split, 0)
                return
            else:
                self.draw_line(d, x1, y1, x_split, HEIGHT)
                self.draw_line(d, x2, y2-HEIGHT, x_split,0)
                return
        if y1 < 0 or y2 < 0:
            x_split = x1 + (x2 - x1) * -y1 / (y2 - y1)
            if y1 < 0:
                self.draw_line(d, x2, y2, x_split, 0)
                self.draw_line(d, x1, y1+HEIGHT, x_split, HEIGHT)
                return
            else:
                self.draw_line(d, x1, y1, x_split, 0)
                self.draw_line(d, x2, y2+HEIGHT, x_split, HEIGHT)
                return

        d.line(x1, y1, x2, y2)

class ShipKlein(Ship):
    def __init__(self):
        super().__init__()

    def wrap(self, x, y):
        while x > WIDTH:
            x -= WIDTH
            y = HEIGHT-y
            rot *= -1
        y %= HEIGHT
        return x,y

    def draw_line(self, d, x1, y1, x2, y2):
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        while x1 < 0 and x2 < 0:
            x1 += WIDTH
            x2 += WIDTH
        while x1 > WIDTH and x2 > WIDTH:
            x1 -= WIDTH
            x2 -= WIDTH
        while y1 < 0 and y2 < 0:
            y1 += HEIGHT
            y2 += HEIGHT
        while y1 > HEIGHT and y2 > HEIGHT:
            y1 -= HEIGHT
            y2 -= HEIGHT

        if x1 > WIDTH or x2 > WIDTH:
            y_split = y1 + (y2 - y1) * (WIDTH - x1) / (x2 - x1)
            if x1 > WIDTH:
                self.draw_line(d, x2, y2, WIDTH, y_split)
                self.draw_line(d, x1-WIDTH, y1, 0, y_split)
                return
            else:
                self.draw_line(d, x1, y1, WIDTH, y_split)
                self.draw_line(d, x2-WIDTH, y2, 0, y_split)
                return
        if x1 < 0 or x2 < 0:
            y_split = y1 + (y2 - y1) * -x1 / (x2 - x1)
            if x1 < 0:
                self.draw_line(d, x2, y2, 0, y_split)
                self.draw_line(d, x1+WIDTH, y1, WIDTH, y_split)
                return
            else:
                self.draw_line(d, x1, y1, 0, y_split)
                self.draw_line(d, x2+WIDTH, y2, WIDTH, y_split)
                return

        if y1 > HEIGHT or y2 > HEIGHT:
            x_split = x1 + (x2 - x1) * (HEIGHT - y1) / (y2 - y1)
            if y1 > HEIGHT:
                self.draw_line(d, x2, y2, x_split, HEIGHT)
                self.draw_line(d, x1, y1-HEIGHT, x_split, 0)
                return
            else:
                self.draw_line(d, x1, y1, x_split, HEIGHT)
                self.draw_line(d, x2, y2-HEIGHT, x_split,0)
                return
        if y1 < 0 or y2 < 0:
            x_split = x1 + (x2 - x1) * -y1 / (y2 - y1)
            if y1 < 0:
                self.draw_line(d, x2, y2, x_split, 0)
                self.draw_line(d, x1, y1+HEIGHT, x_split, HEIGHT)
                return
            else:
                self.draw_line(d, x1, y1, x_split, 0)
                self.draw_line(d, x2, y2+HEIGHT, x_split, HEIGHT)
                return

        d.line(x1, y1, x2, y2)

import display
import buttons
import utime
d = display.open()

selected = 0
surfaces = ["Torus","Klein bottle"]
ships = [ShipTorus,ShipKlein]

while True:
    text = ""
    for i,s in enumerate(surfaces):
        if i == selected:
            text += ">"
        else:
            text += " "
        text += (s+" "*10)[:10]
    d.clear()
    d.print(text)
    d.update()
    utime.sleep(0.1)
    if buttons.read(buttons.TOP_RIGHT):
        break
    if buttons.read(buttons.BOTTOM_RIGHT):
        selected += 1
    if buttons.read(buttons.BOTTOM_LEFT):
        selected -= 1
    selected %= len(surfaces)

s = ships[selected]()

while True:
    d.clear()
    s.draw(d)
    d.update()
    utime.sleep(0.1)
    if buttons.read(buttons.BOTTOM_RIGHT):
        s.rt()
    if buttons.read(buttons.BOTTOM_LEFT):
        s.lt()
    s.fd()
d.close()

