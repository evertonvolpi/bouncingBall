from gfxhat import backlight, lcd
import time

# --------------- D I S P L A Y     O B J E C T --------------- #

def displayObject (obj, startX=0, startY=0):
    column = len(obj)-1
    row = len(obj[0])-1
    y = column
    
    while(y >= 0):
            x = row
            while(x >= 0):
                lcd.set_pixel(x + startX, y + startY, obj[y][x])
                x-=1
            y-=1
            lcd.show()


# --------------- E R A S E     O B J E C T --------------- #

def eraseObject(obj, startX=0, startY=0):
    
    column = len(obj)-1
    row = len(obj[0])-1

    if(startY + len(obj) > 63):
        startY = 64 - len(obj)
        
    if(startX + len(obj[0]) > 127):
        startX = 128 - len(obj[0])

    y = column

    while(y >= 0):
        x = row
        while(x >= 0):
            pixel = obj[y][x]
            if(pixel == 1):
                pixel = 0
                lcd.set_pixel(x + startX, y + startY, pixel)
            x-=1
        y-=1
    lcd.show()


# --------------- M O V E     O B J E C T --------------- #

def moveObject(obj, startX=0, startY=0, vx=0, vy=0):
    column = len(obj)-1
    row = len(obj[0])-1

    y = column
    endX = startX + vx
    endY = startY + vy

    while(startX <= endX and startY <= endY):
        while(y >= 0):
            x = row
            while(x >= 0):
                lcd.set_pixel(x + startX, y + startY, obj[y][x])
                x-=1
            y-=1
        lcd.show()
        time.sleep(2)
        eraseObject(obj,startX,startY)
        y = column
        startX += vx
        startY += vy


# --------------- C H E C K     C O L L I S I O N --------------- #

def checkCollision(obj, startX=0, startY=0, vx=0, vy=0, Sx=128, Sy=64):
    column = len(obj)-1
    row = len(obj[0])-1

    y = column

    while(startX < Sx and startY < Sy):
        while(y >= 0):
            x = row
            while(x >= 0):
                x-=1
            y-=1
        print("X = {} | Y = {} | VX = {} | VY = {}".format(startX,startY,vx,vy))
        startX += vx
        startY += vy
    print("At coordinates X = {} and Y = {} with a speed VX = {} and VY = {}, the object will collide with the screen boundarie in the next movement.".format(startX-vx,startY-vy,vx,vy))


# --------------- B O U N C I N G     O B J E C T --------------- #

def bouncingBall(obj, startX=0, startY=0, vx=0, vy=0, Sx=128, Sy=64):
    lenX = len(obj[0])
    lenY = len(obj)
    direction = "starting"

    while(True):
        if(startX + lenX < Sx and startY + lenY < Sy and direction == "starting"):
            
            startX, startY = moveObjectSE(obj, startX, startY, vx, vy)

            if(startX + lenX >= Sx and startY + lenY < Sy): startY = startY - vy
            if(startY + lenY >= Sy and startX + lenX < Sx): startX = startX - vx
            if(startX + lenX >= Sx and startY + lenY >= Sy): startX = startX - vx
            direction = "rightDown"

        if(startX + lenX < Sx and startY + lenY < Sy and direction == "leftDown"):
            startX = startX + vx
            
            startX, startY = moveObjectSE(obj, startX, startY, vx, vy)
            
            if(startX + lenX >= Sx and startY + lenY < Sy): startY = startY - vy
            if(startY + lenY >= Sy and startX + lenX < Sx): startX = startX - vx
            if(startX + lenX >= Sx and startY + lenY >= Sy): startX = startX - vx
            direction = "rightDown"
        
        if(startX + lenX < Sx and startY <= 0 and direction == "rightUp"):
            startY = startY + vy
            
            startX, startY = moveObjectSE(obj, startX, startY, vx, vy)

            if(startX + lenX >= Sx and startY + lenY < Sy): startY = startY - vy
            if(startY + lenY >= Sy and startX + lenX < Sx): startX = startX - vx
            if(startX + lenX >= Sx and startY + lenY >= Sy): startX = startX - vx
            direction = "rightDown"  
        
        if(startX + lenX < Sx and startY + lenY >= Sy and direction == "rightDown"):
            startY = startY - vy
            
            startX, startY = moveObjectNE(obj, startX, startY, vx, vy)

            if(startY < 0): startX = startX - vx
            if(startX + lenX >= Sx): startY = startY + vy
            direction = "rightUp"

        if(startX < 0 and startY > 0 and direction == "leftUp"):
            startX = startX + vx
            
            startX, startY = moveObjectNE(obj, startX, startY, vx, vy)

            if(startY < 0): startX = startX - vx
            if(startX + lenX >= Sx): startY = startY + vy
            direction = "rightUp"

        if(startX + lenX >= Sx and startY + lenY < Sy and direction == "rightDown"):
            startX = startX - vx
            
            startX, startY = moveObjectSW(obj, startX, startY, vx, vy)

            if(startX < 0 and startY + lenY < Sy): startY = startY - vy
            if(startY + lenY >= Sy and startX >= 0): startX = startX + vx
            if(startX < 0 and startY + lenY >= Sy): startX = startX + vx
            direction = "leftDown"

        if(startX > 0 and startY <= 0 and direction == "leftUp"):
            startY = startY + vy
            
            startX, startY = moveObjectSW(obj, startX, startY, vx, vy)

            if(startX < 0 and startY + lenY < Sy): startY = startY - vy
            if(startY + lenY >= Sy and startX >= 0): startX = startX + vx
            if(startX < 0 and startY + lenY >= Sy): startX = startX + vx
            direction = "leftDown"

        if(startX > 0 and startY + lenY >= Sy and direction == "leftDown"):
            startY = startY - vy
            
            startX, startY = moveObjectNW(obj, startX, startY, vx, vy)

            if(startX < 0): startY = startY + vy
            if(startY < 0): startX = startX + vx
            direction = "leftUp"

        if(startX + lenX >= Sx and startY > 0 and direction == "rightUp"):
            startX = startX - vx

            startX, startY = moveObjectNW(obj, startX, startY, vx, vy)
                
            if(startY < 0): startX = startX + vx
            if(startX < 0): startY = startY + vy
            direction = "leftUp"

# --- Inner Collision Detector ---

def collisionDetector (obj, startX, startY, vx, vy, Sx=128, Sy=64):
    lenX = len(obj[0])
    lenY = len(obj)
    if(startX + lenX < Sx and startY + lenY < Sy and startX >=0 and startY >=0):
        return(True)

# --- Inner Display Object ---

def displayObjectInner (obj, startX=0, startY=0):
    column = len(obj)-1
    row = len(obj[0])-1
    y = column
    
    while(y >= 0):
            x = row
            while(x >= 0):
                lcd.set_pixel(x + startX, y + startY, obj[y][x])
                x-=1
            y-=1

# --- Inner Move Object / Directions ---

# SouthEast
def moveObjectSE (obj, startX=0, startY=0, vx=0, vy=0):
    while(collisionDetector(obj, startX, startY, vx, vy) == True):
        displayObjectInner (obj, startX, startY)
        lcd.show()
        time.sleep(0.05)
        eraseObject(obj,startX,startY)
        startX += vx
        startY += vy
    return(startX, startY)

# SouthWest
def moveObjectSW (obj, startX=0, startY=0, vx=0, vy=0):
    while(collisionDetector(obj, startX, startY, vx, vy) == True):
        displayObjectInner (obj, startX, startY)
        lcd.show()
        time.sleep(0.05)
        eraseObject(obj,startX,startY)
        startX -= vx
        startY += vy
    return(startX, startY)

# NorthEast
def moveObjectNE (obj, startX=0, startY=0, vx=0, vy=0):
    while(collisionDetector(obj, startX, startY, vx, vy) == True):
        displayObjectInner (obj, startX, startY)
        lcd.show()
        time.sleep(0.05)
        eraseObject(obj,startX,startY)
        startX += vx
        startY -= vy
    return(startX, startY)

# NorthWest
def moveObjectNW (obj, startX=0, startY=0, vx=0, vy=0):
    while(collisionDetector(obj, startX, startY, vx, vy) == True):
        displayObjectInner (obj, startX, startY)
        lcd.show()
        time.sleep(0.05)
        eraseObject(obj,startX,startY)
        startX -= vx
        startY -= vy
    return(startX, startY)