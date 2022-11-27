import pygame,os
import random
 
os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

fps=120
timer=pygame.time.Clock()


currentPaint=[]
activeSize=20
activeColor='white'
info=pygame.display.Info()
WIDTH=info.current_w-10
HEIGHT=info.current_h-50
screen = pygame.display.set_mode([WIDTH,HEIGHT])

pygame.display.set_caption("The Paint Application!")
activeShape="circle"
activeRectHeight=20
activeRectWidth=20
painting=[]

def draw_menu():
    
    pygame.draw.rect(screen,'gray',[0,0,WIDTH,70])
    pygame.draw.line(screen,'black',(0,70),(WIDTH,70),3)

    xl_brush=pygame.draw.rect(screen,(0,0,128),[10,10,50,50])

    font=pygame.font.Font('freesansbold.ttf',32)
    text=font.render('P',True,(0,255,0),(0,0,128))
    textRect=text.get_rect()
    textRect.center=(30,35)

    screen.blit(text,textRect)

    circle_brush=pygame.draw.rect(screen,'black',[70,10,50,50])
    pygame.draw.circle(screen,'white',(95,35),20)
    rectangle_brush=pygame.draw.rect(screen,'black',[130,10,50,50])
    pygame.draw.rect(screen,'white',[135,15,40,40])
    triangle_brush=pygame.draw.rect(screen,'black',[190,10,50,50])
    pygame.draw.polygon(screen, (0, 255, 255), ((213,16),(195,55),(235,55)))
    acFont=pygame.font.Font('freesansbold.ttf',32)
    actext=font.render('CLEAR',True,(0,255,0),(0,0,128))
    actextRect=actext.get_rect()
    actextRect.center=(310,30)
    screen.blit(actext,actextRect)

    brush_list=[xl_brush,circle_brush,rectangle_brush,triangle_brush,actextRect]


    red=pygame.draw.rect(screen,(255,0,0),[WIDTH-35,10,25,25])
    green=pygame.draw.rect(screen,(0,255,0),[WIDTH-35,35,25,25])
    blue=pygame.draw.rect(screen,(0,0,255),[WIDTH-60,10,25,25])
    orange=pygame.draw.rect(screen,(252,121,0),[WIDTH-60,35,25,25])
    yellow=pygame.draw.rect(screen,(255,255,0),[WIDTH-85,10,25,25])
    pink=pygame.draw.rect(screen,(255,0,122),[WIDTH-85,35,25,25])
    brown=pygame.draw.rect(screen,(122,0,0),[WIDTH-110,10,25,25])
    white=pygame.draw.rect(screen,(255,255,255),[WIDTH-110,35,25,25])
    black=pygame.draw.rect(screen,(0,0,0),[WIDTH-135,10,25,25])
    turquoise=pygame.draw.rect(screen,(64,224,224),[WIDTH-135,35,25,25])

    
    rgb_list=[(255,0,0),(0,255,0),(0,0,255),(252,121,0),(255,255,0),(255,0,122),(122,0,0),(255,255,255),(0,0,0)]
    color_rect=[red,green,blue,orange,yellow,pink,brown,white,black]
    return brush_list,color_rect,rgb_list

def drawPainting(paints):
    bl,cr,rg=draw_menu()
    for i in range(len(paints)):
        if paints[i][3]=="pencil":
           pygame.draw.circle(screen,paints[i][0],paints[i][1],10)
        elif paints[i][3]=="circle":
           pygame.draw.circle(screen,random.choice(rg),paints[i][1],paints[i][2])
        elif paints[i][3]=="rectangle":
           x=paints[i][1][0]
           y=paints[i][1][1]
           top=y-paints[i][4]
           left=x-paints[i][5]
           height=paints[i][4]
           width=paints[i][5]
           pygame.draw.rect(screen,paints[i][0],[left,top,height ,width])
        elif paints[i][3]=="triangle":
            x=paints[i][1][0]
            y=paints[i][1][1]
            pygame.draw.polygon(screen, paints[i][0], ((x,y-paints[i][4]),(x-paints[i][5],y+paints[i][4]),(x+paints[i][5],y+paints[i][4])))   

run =True

while run:
    timer.tick(fps)
    screen.fill('white')

    mouse=pygame.mouse.get_pos()
    leftClick=pygame.mouse.get_pressed()[0]

    if leftClick and mouse[1]>70:
        currentPaint=painting
        painting.append((activeColor,mouse,activeSize,activeShape,activeRectHeight,activeRectWidth))    
    drawPainting(painting)

    


    if mouse[1]>70:
        if activeShape=="pencil":
           pygame.draw.circle(screen,activeColor,mouse,10)
        elif activeShape=="circle":
           pygame.draw.circle(screen,activeColor,mouse,activeSize)
        elif activeShape=="rectangle":
           x=mouse[0]
           y=mouse[1]
           top=y-activeRectHeight
           left=x-activeRectWidth
           height=activeRectHeight
           width=activeRectWidth
           pygame.draw.rect(screen,activeColor,[left,top,height ,width])
        elif activeShape=="triangle":
            x=mouse[0]
            y=mouse[1]
            pygame.draw.polygon(screen,activeColor, ((x,y-activeRectHeight),(x-activeRectWidth,y+activeRectHeight),(x+activeRectWidth,y+activeRectHeight))) 
 
    brushes,colors,rgbs=draw_menu()

    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
               print("Up Key Pressed!")
               painting=currentPaint
            if event.key == pygame.K_KP1:
                activeSize=20
                activeRectHeight=20
                activeRectWidth=20
            elif event.key == pygame.K_KP2:
                activeSize=40
                activeRectHeight=30
                activeRectWidth=30
            elif event.key == pygame.K_KP3:
                activeSize=60
                activeRectHeight=40
                activeRectWidth=40
            elif event.key == pygame.K_KP4:
                activeSize=80
                activeRectHeight=50
                activeRectWidth=50
            elif event.key == pygame.K_KP5:
                activeSize=100
                activeRectHeight=60
                activeRectWidth=60

        if event.type  == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    if i==0:
                       activeShape="pencil"
                       print(activeShape)
                    elif i==1:
                        activeShape="circle"
                        print(activeShape)
                    elif i==2:
                        activeShape="rectangle"
                        print(activeShape)
                    elif i==3:
                        activeShape="triangle"
                        print(activeShape)
                    elif i==4:
                        painting=[]

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    activeColor = rgbs[i]        

    pygame.display.flip()
pygame.quit()