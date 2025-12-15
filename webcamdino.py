import pygame
import random
import cv2
import numpy as np

# ================= PYGAME SETUP =================
pygame.init()
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game - Webcam Controlled (Py 3.12)")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

# Dino physics
dino_x = 50
ground_y = HEIGHT - 40
dino_y = ground_y
dino_vel_y = 0
gravity = 1
jump = False

# Obstacle
obs_width, obs_height = 20, 40
obs_x = WIDTH
obs_y = HEIGHT - obs_height - 20
obs_speed = 6

score = 0
font = pygame.font.SysFont(None, 30)

# ================= WEBCAM SETUP =================
cap = cv2.VideoCapture(0)
prev_frame = None

# ================= FUNCTIONS =================
def draw_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))

def draw_dino(x, y):
    pygame.draw.rect(screen, BLACK, (x, y - 30, 40, 30))      # body
    pygame.draw.rect(screen, BLACK, (x + 30, y - 45, 20, 20)) # head
    pygame.draw.circle(screen, WHITE, (x + 42, y - 38), 2)   # eye
    pygame.draw.rect(screen, BLACK, (x + 5, y - 5, 10, 10))
    pygame.draw.rect(screen, BLACK, (x + 25, y - 5, 10, 10))
    pygame.draw.polygon(screen, BLACK, [(x, y - 25), (x - 15, y - 20), (x, y - 15)])

def dino_hitbox(x, y):
    return pygame.Rect(x, y - 45, 50, 45)

def motion_jump_detected():
    global prev_frame

    ret, frame = cap.read()
    if not ret:
        return False

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Region of Interest (upper-middle area)
    roi = gray[50:200, 200:450]

    jump_detected = False

    if prev_frame is not None:
        frame_delta = cv2.absdiff(prev_frame, roi)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        motion_score = np.sum(thresh)

        if motion_score > 150000:
            jump_detected = True

    prev_frame = roi.copy()

    # Debug window
    cv2.rectangle(frame, (200, 50), (450, 200), (0, 255, 0), 2)
    cv2.imshow("Webcam Control (Move hand UP)", frame)
    cv2.waitKey(1)

    return jump_detected

# ================= GAME LOOP =================
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Webcam-based jump
    if motion_jump_detected() and not jump:
        dino_vel_y = -15
        jump = True

    # Dino physics
    dino_vel_y += gravity
    dino_y += dino_vel_y
    if dino_y >= ground_y:
        dino_y = ground_y
        jump = False

    # Obstacle logic
    obs_x -= obs_speed
    if obs_x < -obs_width:
        obs_x = WIDTH + random.randint(100, 300)
        score += 1

    # Draw ground
    pygame.draw.line(screen, BLACK, (0, HEIGHT - 20), (WIDTH, HEIGHT - 20), 2)

    # Draw objects
    draw_dino(dino_x, dino_y)
    obs_rect = pygame.Rect(obs_x, obs_y, obs_width, obs_height)
    pygame.draw.rect(screen, BLACK, obs_rect)

    # Collision
    if dino_hitbox(dino_x, dino_y).colliderect(obs_rect):
        running = False

    draw_text(f"Score: {score}", 10, 10)
    pygame.display.update()

# ================= CLEANUP =================
cap.release()
cv2.destroyAllWindows()
pygame.quit()
