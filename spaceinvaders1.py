# My simplified version of Space Invaders

class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height), 0)

class Projectile(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = -8

    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, self.width, self.height), 0)

class Invader(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height), 0)

def create_invaders():
    return [    Invader(40, invader_y, invader_width, invader_height),
                    Invader(100, invader_y, invader_width, invader_height),
                    Invader(160, invader_y, invader_width, invader_height),
                    Invader(220, invader_y, invader_width, invader_height),
                    Invader(280, invader_y, invader_width, invader_height),
                    Invader(340, invader_y, invader_width, invader_height),
                    Invader(400, invader_y, invader_width, invader_height),
                    Invader(40, invader_y + invader_height * 2, invader_width, invader_height),
                    Invader(100, invader_y + invader_height * 2, invader_width, invader_height),
                    Invader(160, invader_y + invader_height * 2, invader_width, invader_height),
                    Invader(220, invader_y + invader_height * 2, invader_width, invader_height),
                    Invader(280, invader_y + invader_height * 2, invader_width, invader_height),
                    Invader(340, invader_y + invader_height * 2, invader_width, invader_height),
                    Invader(400, invader_y + invader_height * 2, invader_width, invader_height),
                    Invader(40, invader_y + invader_height * 4, invader_width, invader_height),
                    Invader(100, invader_y + invader_height * 4, invader_width, invader_height),
                    Invader(160, invader_y + invader_height * 4, invader_width, invader_height),
                    Invader(220, invader_y + invader_height * 4, invader_width, invader_height),
                    Invader(280, invader_y + invader_height * 4, invader_width, invader_height),
                    Invader(340, invader_y + invader_height * 4, invader_width, invader_height),
                    Invader(400, invader_y + invader_height * 4, invader_width, invader_height),
                    Invader(40, invader_y + invader_height * 6, invader_width, invader_height),
                    Invader(100, invader_y + invader_height * 6, invader_width, invader_height),
                    Invader(160, invader_y + invader_height * 6, invader_width, invader_height),
                    Invader(220, invader_y + invader_height * 6, invader_width, invader_height),
                    Invader(280, invader_y + invader_height * 6, invader_width, invader_height),
                    Invader(340, invader_y + invader_height * 6, invader_width, invader_height),
                    Invader(400, invader_y + invader_height * 6, invader_width, invader_height)    ]

def get_greater_x():
    x = 0
    index = 0
    for invader in invaders:        
        if x < invader.x:
            x = invader.x
            index = invaders.index(invader)

    return index

def draw():
    display_score = font.render('Score: ' + str(score), 1, (255, 255, 255))
    window.blit(display_score, (5, 5))

    if is_game_over:
        display_game_over = font.render('GAME OVER', 1, (255, 255, 255))
        window.blit(display_game_over, (WINDOW_WIDTH / 2 - display_game_over.get_width() / 2, 200 ))
    else:
        if len(invaders) == 0:
            victory_text = font.render('Congratulations! YOU WON.', 1, (255, 255, 255))
            window.blit(victory_text, (WINDOW_WIDTH / 2 - victory_text.get_width() / 2, 200))
        else:
            player.draw(window)
            for bullet in bullets:
                bullet.draw(window)

            for invader in invaders:
                invader.draw(window)

    if len(invaders) == 0 or is_game_over:
        global play
        play = False
        continue_text = font.render('Press P to play again or Q to quit', 1, (255, 255, 255))
        window.blit(continue_text, (WINDOW_WIDTH / 2 - continue_text.get_width() / 2, 250))


    pygame.display.update()

import pygame
pygame.init()

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 580
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Invaders 1 by Helio Rui ')
explosion_sound = pygame.mixer.Sound('Sounds/explosion.wav')
laser_sound = pygame.mixer.Sound('Sounds/laser.wav')
font = pygame.font.SysFont('Arial', 30, True)
invader_width = 40
invader_height = 30
invader_y = 100
player_width = 50
player_height = 10
x = WINDOW_WIDTH / 2 + player_width / 2
y = WINDOW_HEIGHT - player_height - 20
velocity = 5
score = 0
clock = pygame.time.Clock()
player = Player(x, y, player_width, player_height)
invaders = create_invaders()
bullets = []
shootLoop = 0
cicle_of_horizontal_move = 0
cicle_of_vertical_move = 0
invaders_block_direction = 1
speed_x_block_invaders = 20
play = True
is_game_over = False
run = True
while run:
    clock.tick(27)
    window.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    if len(invaders) == 0 or is_game_over:
        if keys[pygame.K_p]:
            score = 0
            j = 0
            is_game_over = False
            play = True
            invaders = create_invaders()
            bullets = []

    if play:
        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 10:
            shootLoop = 0

        for invader in invaders:
            for bullet in bullets:
                if bullet.y < invader.y + invader.height and bullet.y + bullet.height > invader.y:
                    if bullet.x + bullet.width > invader.x and bullet.x - bullet.width < invader.x + invader.width:
                        explosion_sound.play()
                        bullets.pop(bullets.index(bullet))
                        invaders.pop(invaders.index(invader))
                        score += 10

        for bullet in bullets:
            if bullet.y < WINDOW_HEIGHT and bullet.y > 0:
                bullet.y += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet))

        if keys[pygame.K_SPACE] and shootLoop == 0:
            laser_sound.play()
            if len(bullets) < 25:
                bullets.append(Projectile(player.x + player.width / 2 - 2, player.y, 5, 10))

            shootLoop = 1

        if keys[pygame.K_LEFT] and player.x > player.velocity:
            player.x -= player.velocity

        if keys[pygame.K_RIGHT] and player.x < WINDOW_WIDTH - player.width - player.velocity:
            player.x += player.velocity

        cicle_of_horizontal_move += 1
        if cicle_of_horizontal_move == 20 and len(invaders) > 0:
            index = get_greater_x()
            if invaders[0].x <= 20 or invaders[index].x + invaders[index].width >= WINDOW_WIDTH - invader_width - 5:
                invaders_block_direction *= -1

            for invader in invaders:
                invader.x += speed_x_block_invaders * invaders_block_direction
                cicle_of_horizontal_move = 0


        cicle_of_vertical_move += 1
        if cicle_of_vertical_move == 27 * 10 and len(invaders) > 0:
            for invader in invaders:
                invader.y += invader_height * 2

            cicle_of_vertical_move = 0


        for invader in invaders:
            if invader.y >= y - 15:
                is_game_over = True
                break

    draw()


pygame.quit()
