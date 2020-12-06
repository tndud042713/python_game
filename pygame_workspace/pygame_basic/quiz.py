import pygame
################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()  # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Sy Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()
################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트 등)

# 배경만들기
background = pygame.image.load(
    "C:\\Users\\USER\\OneDrive\\문서\\python_game\\pygame_workspace\\pygame_basic\\background.png")

# 캐릭터 만들기
character = pygame.image.load(
    "C:\\Users\\USER\\OneDrive\\문서\\python_game\\pygame_workspace\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height - character_height

# 이동위치
to_x = 0
character_speed = 10

running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 키를 눌렀을때
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 
        if event.type == pygame.KEYUP: # 키를 떼었을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos <0:
        character_x_pos = 0 # 화면 왼쪽으로 넘어가지 않게 해줌
    elif character_x_pos > screen_width - character_width:
         character_x_pos = screen_width - character_width # 화면 오른쪽으로 넘어가지 않게 해줌

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))  # 배경그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # 계속해서 게임 화면을 그려줘야됨

# pygame 종료
pygame.quit()
