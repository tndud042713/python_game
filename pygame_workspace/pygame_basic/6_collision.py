import pygame

pygame.init()  # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Sy Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
# \가 두개씩 있어야 파일 위치를 읽을 수 있다.
background = pygame.image.load(
    "C:\\Users\\USER\\OneDrive\\바탕 화면\\pygame_workspace\\pygame_basic\\background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "C:\\Users\\USER\\OneDrive\\바탕 화면\\pygame_workspace\\pygame_basic\character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 케릭터의 가로크기
character_height = character_size[1]  # 케릭터의 세로크기
character_x_pos = (screen_width/2) - (character_width /
                                      2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - 70  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# 이동할 좌표
to_x=0
to_y=0

# 이동속도
character_speed = 0.8

# 적 enemy 캐릭터
enemy = pygame.image.load(
    "C:\\Users\\USER\\OneDrive\\바탕 화면\\pygame_workspace\\pygame_basic\enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 케릭터의 가로크기
enemy_height = enemy_size[1]  # 케릭터의 세로크기
enemy_x_pos = (screen_width/2) - (enemy_width /2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = (screen_height/2) - (enemy_height/2)  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)


#이벤트 루프
running = True  # 게임이 진행중인가?
while running:  # 계속 돌고있는 중이라면
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

# 캐릭터가 100 만큼 이동을 해야함
# 10 fps : 1초 동안에 10 번 동작 -> 1번에 몇 만큼 이동? 10 만큼! 10 * 10 = 100
# 20 fps : 1초 동안에 20 번 동작 -> 1번에 5만큼! 5 * 20 = 100

    print("fps : "+str(clock.get_fps()))
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # x버튼을 눌러서 창을 끊다면 // 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임을 종료한다 // 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 케릭터를 왼쪽으로
                to_x-=character_speed # to_x= to_x-5와 동일함 // 강의에서는 5값을 사용했으나 컴퓨터의 사양차이로 나는 1값을 사용
            elif event.key == pygame.K_RIGHT:  # 케릭터를 오른쪽으로
                to_x+=character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y-=character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y+=character_speed

        if event.type == pygame.KEYUP: #방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x *dt
    character_y_pos += to_y *dt # *dt를 해주므로써 프레임별 이동속도를 고정시켜줌

    # 가로 경계값 처리
    if character_x_pos <0:
        character_x_pos = 0 #왼쪽 경계선을 넘어가지 못하게 함
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos <0:
        character_y_pos = 0 #위쪽 경계선을 넘어가지 못하게 함
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0))  # 실제로 배경을 그려줌

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터를 그림

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 그리기

    pygame.display.update()  # 계속해서 게임 화면을 그려줘야됨

# pygame 종료
pygame.quit()
