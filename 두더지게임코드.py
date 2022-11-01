import pygame #파이 게임 모듈 임포트
from random import randint
import sys
import time
from pygame.locals import QUIT,KEYDOWN,KEYUP, K_q,K_w,K_e,K_r,K_t

pygame.init() #파이 게임 초기화

WIDTH = 1920
HEIGHT = 1102
Over_Font=pygame.font.SysFont(None,100)
Large_Font = pygame.font.SysFont(None, 60)
Small_Font = pygame.font.SysFont(None, 36)
pygame.display.set_caption('CATCHING!_MOLES')
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT)) #화면 크기 설정
FPSCLOCK = pygame.time.Clock()
global MoleA
global MoleB
global Face



def main():
    Start_Time = int(time.time())
    GiveTime =100
    Score = 0
    Combo = 0
    Miss=0
    In=0
    Boss=350
    Game_Start = False
    Game_Over = False
    Start_image = pygame.image.load('시작화면.png')
    Main_image = pygame.image.load('메인 화면.png')
    Mole_image = pygame.image.load('두더지.png')
    End_image=pygame.image.load('끝점수판.png')
    Happy=pygame.image.load('표정1.png')
    Happy = pygame.transform.scale(Happy, (900, 500))
    Sad=pygame.image.load('표정2.png')
    Sad= pygame.transform.scale(Sad, (900, 500))
    Hand=pygame.image.load('두더지손.png')
    Hand= pygame.transform.scale(Hand, (900, 500))
    mole1 = Mole_image.get_rect(left= 350,top =550)
    mole2 = Mole_image.get_rect(left= 550,top = 620)
    mole3 = Mole_image.get_rect(left= 750,top = 700)
    mole4= Mole_image.get_rect(left=960,top = 620)
    mole5 = Mole_image.get_rect(left=1100,top = 550)
    main_sound=pygame.mixer.Sound('Staycation.mp3')
    hit_sound=pygame.mixer.Sound('맞는효과음.wav')
    Boss_sound=pygame.mixer.Sound('으윽.mp3')
    
    
    Over_Message = Over_Font.render("GAME_OVER",True,(255,255,255))
    while True: #게임 루프
        Score_Message = Small_Font.render("Score : {}".format(Score),True,(255,255,255))
        ComboCount_Message = Small_Font.render("Combo : {}".format(Combo),True,(255,255,255))
        MissCount_Message = Small_Font.render("Miss : {}".format(Miss),True,(255,255,255))
        Boss_Message = Small_Font.render("HP: {}".format(Boss),True,(255,255,255))
        Score_End_Message = Large_Font.render("Total Score : {}".format(Score - Miss), True, (255, 255, 255))
        Time_Message = Small_Font.render("Time : {}".format(GiveTime), True, (255, 255, 255))
    
        for event in pygame.event.get():
            
            if Boss==0:
                Boss_sound.play()
                Boss=350
                Score+=4000
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
                
            elif event.type ==KEYUP:
               
                Game_Start = True
                Face=1
                if Game_Start==True and In==0:
                  pygame.mixer.init()
                  main_sound.play()
                  In=1
              
                
            
                if randint(0,4)== 0:
                      MoleA=mole1
                      BUT1=0
                elif randint(0,4)==1:
                       MoleA=mole2
                       BUT1=1
                elif randint(0,4)==2:
                       MoleA=mole3
                       BUT1=2
                elif randint(0,4)==3:
                     MoleA=mole4
                     BUT1=3
                elif randint(0,4)==4: 
                     MoleA=mole5
                     BUT1=4
                
                if randint(0,4)== 0:
                      MoleB=mole5
                      BUT2=4
                elif randint(0,4)==1:
                       MoleB=mole4
                       BUT2=3
                elif randint(0,4)==2:
                       MoleB=mole3
                       BUT2=2
                elif randint(0,4)==3:
                     MoleB=mole2
                     BUT2=1
                elif randint(0,4)==4: 
                     MoleB = mole1
                     BUT2=0
            
            if event.type==KEYDOWN:
             if Game_Start:   
                if event.key==K_q:
                       if BUT1==0 or BUT2==0:
                        hit_sound.play()
                        Score+=2*Combo+10
                        Boss-=10
                        Combo+=1
                        Face=0
                       else: 
                        Miss +=1
                        Combo=0
            
                elif event.key==K_w:
                        if BUT1==1 or BUT2==1:
                            hit_sound.play()
                            Score+=2*Combo+10
                            Boss-=10
                            Combo+=1
                            Face=0
                        else: 
                            Miss+=1
                            Combo=0
                elif event.key==K_e:
                        if BUT1==2 or BUT2==2:
                            hit_sound.play()
                            Score+=2*Combo+10
                            Boss-=10
                            Combo+=1
                            Face=0
                        else: 
                            Miss+= 1
                            Combo=0
                elif event.key==K_r:
                        if BUT1==3 or BUT2==3:
                            hit_sound.play()
                            Score+=2*Combo+10
                            Boss-=10
                            Combo+=1
                            Face=0
                        else: 
                            Miss+=1
                            Combo=0
                elif event.key==K_t:
                        if BUT1 ==4 or BUT2==4:
                            hit_sound.play()
                            Score+=2*Combo+10
                            Boss-=10
                            Combo+=1
                            Face=0
                        else: 
                            Miss+=1
                            Combo=0
            if Game_Over==True and event.type==KEYUP:     
                pygame.quit()
                sys.exit()  

        #게임이 시작되기전 대기 화면
        if Game_Start == False and Game_Over == False:
            Loading_Time = int(time.time())
            SURFACE.fill((255,255,255))
            SURFACE.blit(Start_image,(0,0))
            

        #게임이 시작
        elif Game_Start == True and Game_Over == False:
            Current_Time = int(time.time())
            SURFACE.fill((0,0,0))
            SURFACE.blit(Main_image,(0,0))
            SURFACE.blit(Mole_image,MoleA)
            SURFACE.blit(Mole_image,MoleB)
            if Face==1:
                SURFACE.blit(Happy,(WIDTH/2-120,500))
                SURFACE.blit(Hand,(WIDTH/4+200,700))
                SURFACE.blit(Hand,(WIDTH-WIDTH/3-200,700))
            elif Face==0:
                SURFACE.blit(Sad,(WIDTH/2-120,500))
                SURFACE.blit(Hand,(WIDTH/4+200,600))
                SURFACE.blit(Hand,(WIDTH-WIDTH/3-200,600))
            SURFACE.blit(Score_Message,(15,15))
            SURFACE.blit(ComboCount_Message, (WIDTH/2-30, 15))
            SURFACE.blit(MissCount_Message, (15, 50))
            SURFACE.blit(Boss_Message, (WIDTH/2-30, 100))
            SURFACE.blit(Time_Message,(WIDTH-130,15))
            GiveTime = 100 - (Current_Time - Start_Time) + (Loading_Time - Start_Time)
            #제한 시간 오버
            if GiveTime <= 0:
                Game_Over = True
                Game_Start = False
                GiveTime = 0
        elif Game_Over ==True:
            main_sound.stop()
            SURFACE.fill((255,255,255))
            SURFACE.blit(End_image,(0,0))
            SURFACE.blit(Over_Message,(WIDTH/2-160,HEIGHT/2-50))
            SURFACE.blit(Score_End_Message, (WIDTH/2-150,HEIGHT/2+100))
         


        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()