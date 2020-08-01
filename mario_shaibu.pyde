#============================================
#MARIO GAME
#Author: Fuseini Shaibu Sunnuma
#Email:shaibusunnuma@gmail.com
#Version 1.1
#============================================

add_library('sound')
import os
path = os.getcwd()

#=========================================================
#               THE GAME CLASS
#===========================================================
class Game:
    def __init__(self):
        self.gains = 0
        self.x=0
        self.w=1280
        self.h=720
        self.g=583
        self.mario = Mario(100,100,35,self.g,100,70,11,'mario.png')
        self.bg=[]
        for i in range(5):
            self.bg.append(loadImage(path+'/images/layer_0'+str(5-i)+'.png'))
        self.platforms=[]
        self.platforms.append(Platform(350,300,200,52))
        self.platforms.append(Platform(600,400,200,52))
        self.platforms.append(Platform(1100,400,200,52))
        self.platforms.append(Platform(1400,300,200,52))
        self.music = SoundFile(this, path + '/sounds/music.mp3')
        self.music.play()
            
    def extras(self):
        star = loadImage(path+'/images/star.png')
        heart = loadImage(path+'/images/mario.png')
        image(heart,10,20,40,40,800,0,900,100)
        image(star,1215,20,20,20,0,0,40,40)
        fill(255)
        textSize(18)
        text(self.mario.life,45,40)
        text(self.gains,1245,37)
        
        

    def display(self):
        count = 5
        for img in self.bg:
            x = (self.x//count) % self.w                                       
            count -= 1
            image(img,1280-x,0)
            image(img,0-x,0)
            
        for p in self.platforms:
            p.display()
            
        self.extras()
            
        self.mario.display()
   
    
#=============================PLATFORM==============================                
class Platform:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.img=loadImage(path+'/images/platform1.png')
        
    def display(self):
        image(self.img,self.x-game.x,self.y,self.w,self.h)
   
        
#================================================================================================
#-----------------------------------------------CREATURE CLASS-----------------------------------
            
class Creature:
    def __init__(self,x,y,r,g,w,h,F,img):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.w=w
        self.h=h
        self.F=F
        self.vy=0
        self.vx=0
        self.f=0
        self.dir=1
        self.keyHandler = {UP:False, LEFT:False, RIGHT:False}
        self.img = loadImage(path+'/images/'+img)
        
    def gravity(self):
        if self.y+self.r < self.g: #if creature is above ground
            self.vy += 0.5
            if self.y+self.r+self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
        else: 
            self.vy = 0
        for p in game.platforms:
            if self.x >= p.x-10 and self.x <= p.x+p.w-15 and self.y+self.r<=p.y+10:
                self.g = p.y+10
                break
            else:
                self.g = game.g
                
    def update(self):
        self.gravity()
        self.x += self.vx
        self.y += self.vy
        
        
        
    def display(self):
        self.update()
        if self.vx != 0:
            self.f = (self.f+0.5)%self.F
        if self.dir==1:
            if self.vx>0:
                image(self.img, self.x-game.x-self.r,self.y-self.r,self.w,self.h, int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
            else:
                image(self.img, self.x-self.r-game.x,self.y-self.r,self.w,self.h, 3*self.w,0,4*self.w,self.h)
        else:
            if self.vx<0:
                image(self.img, self.x-game.x-self.r,self.y-self.r,self.w,self.h, int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
            else:
                image(self.img, self.x-self.r-game.x,self.y-self.r,self.w,self.h, 4*self.w,0,3*self.w,self.h)
                
        
class Mario(Creature):
    def __init__(self,x,y,r,g,w,h,F,img):
        Creature.__init__(self,x,y,r,g,w,h,F,img)
        self.life = 5
        self.jumpsound = SoundFile(this, path+'/sounds/jump.mp3')
        
    def update(self):
        self.gravity()
        if self.keyHandler[UP] and self.y+self.r == self.g:
            self.jumpsound.play()
            self.vy = -15
        if self.keyHandler[LEFT] and self.x-self.r >= game.x:
            self.vx = -5
            self.dir = -1
        elif self.keyHandler[RIGHT]:
            self.vx = 5
            self.dir = 1
        else:
            self.vx = 0
        if self.x > game.w//2:
            game.x += self.vx
        print(game.x)
        self.x += self.vx
        self.y += self.vy
            
class Star(Creature):
    def __init__(self,x,y,r,g,w,h,F,img):
        Creature.__init__(self,x,y,r,g,w,h,F,img)
        self.vx=1
        def update(self):
            return
        
game = Game()







#==============================SYSTEM CONTROLS===============================
def setup():
    size(game.w,game.h)
    stroke(255)
    background(255)
    
def draw():
    background(255)
    game.display()

def keyPressed():
    #print keyCode
    if keyCode == UP:
        game.mario.keyHandler[UP] = True
    elif keyCode == LEFT:
        game.mario.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        game.mario.keyHandler[RIGHT] = True
        
def keyReleased():
    if keyCode == UP:
        game.mario.keyHandler[UP] = False
    elif keyCode == LEFT:
        game.mario.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.mario.keyHandler[RIGHT] = False    
