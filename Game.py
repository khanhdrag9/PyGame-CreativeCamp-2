import pygame, sys
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BG_COLOR = (255, 255, 255)
FPS = 30

MOVE_SPEED = 5
JUMP = 20
JUMP_HIGH = JUMP * 10

GRAVITY = 7
GROUND = SCREEN_HEIGHT
START_POS = (0, GROUND)


def releaseGame():
    pygame.quit()
    sys.exit()

def loadAnimation(curIndex, sprite, images, isLoadAni = True, orientation = "Right"):
    if isLoadAni == True:
        if(curIndex >= len(images) - 1):
            curIndex = 0
        else:
            curIndex += 1

    sprite = images[curIndex]

    if orientation == "Left":
        sprite = pygame.transform.flip(sprite, True, False)
        
    return (curIndex, sprite)

def getVelocityMove(cmd):
    vec = (0,0)
    if cmd == "goLeft":
        vec = (-1 * MOVE_SPEED, 0)
        return vec
    if cmd == "goRight":
        vec = (MOVE_SPEED, 0)
        return vec
    if cmd == "jump":
        #code jump here....
        
        return vec

def game():
    pygame.init()
    mainClock = pygame.time.Clock() #used to set FPS for game

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mario by Khanh")
    pygame.mouse.set_visible(False)

     #create animation
    animation = pygame.sprite.Sprite 
    animation.images =[
        pygame.image.load('images/walk1.png'),
        pygame.image.load('images/walk2.png'),
        pygame.image.load('images/walk3.png'),
        pygame.image.load('images/walk4.png'),
        pygame.image.load('images/walk5.png'),
        pygame.image.load('images/walk6.png'),
        pygame.image.load('images/walk7.png'),
        pygame.image.load('images/walk8.png'),
        pygame.image.load('images/walk9.png'),
        pygame.image.load('images/walk10.png')
    ]

    curIndex = -1
    playerImage = animation.images[0]
    loadAnimation(curIndex, playerImage, animation.images)
    playerRect = playerImage.get_rect()
    
    #Game Loop
    while True:
        
        playerRect.bottomleft = START_POS
        moveLeft = moveRight = jump = isJumping = False
        orientation = 'Right'
        jumpTarget = 0
        isMove = False

        while True: #loop playing game
            isMove = False
            #event keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    releaseGame()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveLeft = True
                        moveRight = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = True
                        moveLeft = False
                    if event.key == K_SPACE and isJumping == False:
                        y = getVelocityMove("jump")[1]
                        if y > 0:
                            jump = True
                            jumpTarget = playerRect.bottom - y
                
                if event.type == pygame.KEYUP:
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = False

                # Move the player around.
            if moveLeft:
                isMove = True
                orientation = "Left"
                if playerRect.left > 0:
                    playerRect.move_ip(getVelocityMove("goLeft"))

                isLoadAni = True
                if isJumping == True : isLoadAni = False
                curIndex, playerImage = loadAnimation(curIndex, playerImage, animation.images, isLoadAni, orientation)

            if moveRight:
                isMove = True
                orientation = "Right"
                if playerRect.right < SCREEN_WIDTH:
                    playerRect.move_ip(getVelocityMove("goRight"))

                isLoadAni = True
                if isJumping == True : isLoadAni = False
                curIndex, playerImage = loadAnimation(curIndex, playerImage, animation.images, isLoadAni, orientation)

            if isMove == False: #load image 0 again when dont move!
                curIndex, playerImage = loadAnimation(-1, playerImage, animation.images, False, orientation)

            if jump == True and isJumping == False:
                isJumping = True
                jump = False
            
            if isJumping == True and jumpTarget != 0:
                playerRect.move_ip(0, -JUMP)
                if playerRect.bottom <= jumpTarget:
                    jumpTarget = 0

            #update gravity
            if playerRect.bottom < GROUND:
                playerRect.move_ip(0, GRAVITY)
                if playerRect.bottom > GROUND:
                    playerRect.bottom = GROUND
                if  playerRect.bottom == GROUND:
                    isJumping = False
                

            window.fill(BG_COLOR)   # draw color BG
            window.blit(playerImage, playerRect)
 
            pygame.display.update()
            mainClock.tick(FPS)
        

        pygame.display.update()
        #listen last eventkeyboard game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                releaseGame()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESC:
                    releaseGame()
    #end update



if __name__ == "__main__":
    game()