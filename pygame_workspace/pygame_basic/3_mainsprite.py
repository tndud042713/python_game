import pygame

pygame.init()  # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Sy Game") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\USER\\OneDrive\\바탕 화면\\pygame_workspace\\pygame_basic\\background.png") #\가 두개씩 있어야 파일 위치를 읽을 수 있다.

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\USER\\OneDrive\\바탕 화면\\pygame_workspace\\pygame_basic\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 케릭터의 가로크기
character_height = character_size[1] # 케릭터의 세로크기
character_x_pos = (screen_width/2) - (character_width/2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - 70 # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)


#이벤트 루프
running = True # 게임이 진행중인가?
while running: #계속 돌고있는 중이라면
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #x버튼을 눌러서 창을 끊다면 // 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임을 종료한다 // 게임이 진행중이 아님

    
    screen.blit(background, (0,0))  # 실제로 배경을 그려줌

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    pygame.display.update() #계속해서 게임 화면을 그려줘야됨
# pygame 종료
pygame.quit()
