import pygame
import sys
import datetime

# -----------------------
# Configuration
# -----------------------
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400
FPS = 30

LED_RADIUS = 20
LED_SPACING = 60
ROW_SPACING = 100
LEFT_MARGIN = 250   # Increased space after text

BG_COLOR = (10, 10, 20)
LED_OFF = (40, 40, 40)
HOUR_ON = (255, 80, 80)
MIN_ON = (80, 255, 80)
SEC_ON = (80, 120, 255)
TEXT_COLOR = (200, 200, 200)

# -----------------------
# Setup
# -----------------------
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Binary LED Clock")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

# -----------------------
# Draw LED Row
# -----------------------
def draw_led_row(value, bits, y_pos, color, label):
    binary_str = format(value, f'0{bits}b')

    # Draw label
    text = font.render(f"{label}: {value}", True, TEXT_COLOR)
    screen.blit(text, (20, y_pos - 20))

    # Draw LEDs
    for i in range(bits):
        x = LEFT_MARGIN + i * LED_SPACING
        bit = binary_str[i]

        if bit == '1':
            pygame.draw.circle(screen, color, (x, y_pos), LED_RADIUS)
        else:
            pygame.draw.circle(screen, LED_OFF, (x, y_pos), LED_RADIUS)

# -----------------------
# Main Loop
# -----------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    screen.fill(BG_COLOR)

    draw_led_row(hour, 5, 100, HOUR_ON, "Hour")
    draw_led_row(minute, 6, 200, MIN_ON, "Minute")
    draw_led_row(second, 6, 300, SEC_ON, "Second")

    pygame.display.flip()
    clock.tick(FPS)
