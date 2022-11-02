import pygame #파이 게임 모듈 임포트
from random import randint
import sys
import time
from pygame.locals import QUIT,KEYDOWN,KEYUP, K_q,K_w,K_e,K_r,K_t

pygame.init() #파이 게임 초기화

WIDTH = 1920
HEIGHT = 1102
over_Font=pygame.font.SysFont(None,100)
large_Font = pygame.font.SysFont(None, 60)
small_Font = pygame.font.SysFont(None, 36)
pygame.display.set_caption('CATCHING!_MOLES')
surface = pygame.display.set_mode((WIDTH, HEIGHT)) #화면 크기 설정
fpsclock = pygame.time.Clock()
global moleA
global moleB
global face




def main():
	start_Time = int(time.time())
	start_image = pygame.image.load('시작화면.png')
	main_image = pygame.image.load('메인 화면.png')
	end_image=pygame.image.load('끝점수판.png')
	mole_image = pygame.image.load('두더지.png')
	happy=pygame.image.load('표정1.png')
	happy = pygame.transform.scale(happy, (900, 500))
	sad=pygame.image.load('표정2.png')
	sad= pygame.transform.scale(sad, (900, 500))
	hand=pygame.image.load('두더지손.png')
	hand= pygame.transform.scale(hand, (900, 500))
	mole1 = mole_image.get_rect(left= 350,top =550)
	mole2 = mole_image.get_rect(left= 550,top = 620)
	mole3 = mole_image.get_rect(left= 750,top = 700)
	mole4= mole_image.get_rect(left=960,top = 620)
	mole5 = mole_image.get_rect(left=1100,top = 550)
	moleA = mole1
	moleB = mole1
	main_sound=pygame.mixer.Sound('Staycation.mp3')
	hit_sound=pygame.mixer.Sound('맞는효과음.wav')
	boss_sound=pygame.mixer.Sound('으윽.mp3')
	giveTime =60
	In=0
	boss=350
	game_Start = False
	game_Over = False
	score = 0
	miss=0
	combo = 0
	but1 = 5
	but2 = 5
	cry_time = 0
	face=1
	Over_Message = over_Font.render("GAME_OVER",True,(255,255,255))
	while True: #게임 루프
		Score_Message = small_Font.render("score : {}".format(score),True,(255,255,255))
		facm=small_Font.render("{}".format(face),True,(255,255,255))
		comboCount_Message = small_Font.render("combo : {}".format(combo),True,(255,255,255))
		MissCount_Message = small_Font.render("miss : {}".format(miss),True,(255,255,255))
		Boss_Message = small_Font.render("HP: {}".format(boss),True,(255,255,255))
		Score_End_Message = large_Font.render("Total score : {}".format(score - miss), True, (255, 255, 255))
		Time_Message = small_Font.render("Time : {}".format(giveTime), True, (255, 255, 255))
		
		for event in pygame.event.get():
			
			if boss==0:
				boss_sound.play()
				boss=350
				score+=4000
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			
				
			elif event.type ==KEYUP:
			   
				game_Start = True
				face=1
				if game_Start==True and In==0:
					pygame.mixer.init()
					main_sound.play()
					In=1
			  
				
			
				if randint(0,4)== 0:
					moleA=mole1
					but1=0
				elif randint(0,4)==1:
					moleA=mole2
					but1=1
				elif randint(0,4)==2:
					moleA=mole3
					but1=2
				elif randint(0,4)==3:
					moleA=mole4
					but1=3
				elif randint(0,4)==4: 
					moleA=mole5
					but1=4
				
				if randint(0,4)== 0:
					moleB=mole5
					but2=4
				elif randint(0,4)==1:
					moleB=mole4
					but2=3
				elif randint(0,4)==2:
					moleB=mole3
					but2=2
				elif randint(0,4)==3:
					moleB=mole2
					but2=1
				elif randint(0,4)==4: 
					moleB = mole1
					but2=0
			
			elif event.type==KEYDOWN:   
					if event.key==K_q and game_Start==True:
						if but1==0 or but2==0:
							face=0
							hit_sound.play()
							score+=2*combo+10
							boss-=10
							combo+=1
							
						else: 
							miss +=1
							combo=0
					if event.key==K_w and game_Start==True:
						if but1==1 or but2==1: 
							hit_sound.play()
							score+=2*combo+10
							face=0
							boss-=10
							combo+=1
							
							
						else: 
							miss+=1
							combo=0
					if event.key==K_e and game_Start==True:
						if but1==2 or but2==2:
							face=0
							hit_sound.play()
							score+=2*combo+10
							boss-=10
							combo+=1
							
						else: 
							miss+= 1
							combo=0
					if event.key==K_r and game_Start==True:
						if but1==3 or but2==3:
							face=0
							hit_sound.play()
							score+=2*combo+10
							boss-=10
							combo+=1
							
						else: 
							miss+=1
							combo=0
					if event.key==K_t and game_Start==True:
						if but1 ==4 or but2==4:
							face=0
							hit_sound.play()
							score+=2*combo+10
							boss-=10
							combo+=1
							
						else: 
							miss+=1
							combo=0
			if game_Over==True and event.type==KEYUP:	 
				pygame.quit()
				sys.exit()  

		#게임이 시작되기전 대기 화면
		if game_Start == False and game_Over == False:
			Loading_Time = int(time.time())
			surface.fill((255,255,255))
			surface.blit(start_image,(0,0))
			

		#게임이 시작
		elif game_Start == True and game_Over == False:
			Current_Time = int(time.time())
			surface.fill((0,0,0))
			surface.blit(main_image,(0,0))
			surface.blit(mole_image,moleA)
			surface.blit(mole_image,moleB)
			if face==1: 
				surface.blit(happy,(WIDTH/2-120,500))
				surface.blit(hand,(WIDTH/4+200,700))
				surface.blit(hand,(WIDTH-WIDTH/3-200,700))
			else:
				cry_time += 1
				if cry_time > 10:
					cry_time = 0
				surface.blit(sad,(WIDTH/2-120,500))
				surface.blit(hand,(WIDTH/4+200,600))
				surface.blit(hand,(WIDTH-WIDTH/3-200,600))
			surface.blit(Score_Message,(15,15))
			surface.blit(comboCount_Message, (WIDTH/2-30, 15))
			surface.blit(MissCount_Message, (15, 50))
			surface.blit(Boss_Message, (WIDTH/2-30, 100))
			surface.blit(Time_Message,(WIDTH-130,15))
			giveTime = 60 - (Current_Time - start_Time) + (Loading_Time - start_Time)
			#제한 시간 오버
			if giveTime <= 0:
				game_Over = True
				game_Start = False
				giveTime = 0
		elif game_Over ==True:
			main_sound.stop()
			surface.fill((255,255,255))
			surface.blit(end_image,(0,0))
			surface.blit(Over_Message,(WIDTH/2-160,HEIGHT/2-50))
			surface.blit(Score_End_Message, (WIDTH/2-150,HEIGHT/2+100))

		pygame.display.update()
		fpsclock.tick(60)

if __name__ == '__main__':
	main()
