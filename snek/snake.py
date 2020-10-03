import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        self.direction = dir
        
        # TODO: See section 3, "Turning the snake".

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        if x > WIDTH - 1 or x < 0 or y > HEIGHT - 1 or y < 0:
            return True

        for body_part in self.body[1:]:
            if body_part == (x,y):
                return True
        
        return False

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.

        if len(self.body) < self.l + 1:
            self.body.append((0, 0))
        
        # Starting from tail, each body part is now where the body part in front of it was before
        i = len(self.body) - 1
        while i > 0:
            self.body[i] = self.body[i - 1]
            i -= 1
        
        # Move the head one unit in the current direction direction
        dx,dy = DIR[self.direction]
        self.body[0] = (self.body[0][0] + dx, self.body[0][1] + dy)
        
        # Dead on collision
        if self.collision(self.body[0][0], self.body[0][1]):
            self.kill()
            

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        # Loop until a key is pressed, then return
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type != pygame.KEYDOWN:
                    continue
                self.handle_keypress(event.key)
                return

# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # TODO: see section 6, "moving the apple".
    
        if snake == []:
            return

        # Create array with all potential spaces
        all_spaces = []
        i = 0
        while i < WIDTH:
            j = 0
            while j < HEIGHT:
                all_spaces.append((i,j))
                j += 1
            i += 1

        free_spaces = []
        # Add spaces that the snake/apple are not on to another array
        for space in all_spaces:
            if not snake.collision(space[0], space[1]) and self.position != space:
                free_spaces.append(space)

        # Select a random free space to place the apple
        new_space_index = rand_int(len(free_spaces) - 1)
        self.position = free_spaces[new_space_index]


    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    # Needed to display score
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0
    
    # Used to represent difficulty
    ticks = 10

    # Wait for user input, Optional Feature 10
    draw_grid(surface)        
    snake.draw(surface)
    apple.draw(surface)
    screen.blit(surface, (0,0))
    text_surface = font.render("Press any key to begin!", True, (0,0,0))
    screen.blit(text_surface, text_surface.get_rect())
    pygame.display.update()
    snake.wait_for_key()

    while True:
        # TODO: see section 10, "incremental difficulty".
        clock.tick(ticks)
        snake.check_events()
        draw_grid(surface)        
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        
        # TODO: see section 5, "Eating the Apple".
        if (snake.collision(apple.position[0], apple.position[1])):
            apple.place(snake)
            snake.l += 1
            score += 1
            ticks += 1

        screen.blit(surface, (0,0))

        # TODO: see section 8, "Display the Score"
        text_surface = font.render(str(score), True, (0,0,0))
        screen.blit(text_surface, text_surface.get_rect())

        pygame.display.update()
        if snake.dead:
            print(f'You died. Score: {score}')
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()