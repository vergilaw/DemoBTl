import pygame
from constants import *

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption('Go-Game - Menu')
        self.font = pygame.font.Font(None, 48)
        self.selected_size = None
        self.play_with_bot = False
        self.bot_vs_bot = False

        button_height = 60
        button_width = 200
        spacing = 30
        start_y = WINDOW_SIZE // 2 - (5 * button_height + 4 * spacing) // 2

        self.buttons = [
            {
                'rect': pygame.Rect((WINDOW_SIZE - button_width) // 2, start_y, button_width, button_height),
                'text': '9 x 9',
                'size': 9,
                'bot': False,
                'bot_vs_bot': False
            },
            {
                'rect': pygame.Rect((WINDOW_SIZE - button_width) // 2, start_y + button_height + spacing, button_width,
                                    button_height),
                'text': '13 x 13',
                'size': 13,
                'bot': False,
                'bot_vs_bot': False
            },
            {
                'rect': pygame.Rect((WINDOW_SIZE - button_width) // 2, start_y + 2 * (button_height + spacing),
                                    button_width, button_height),
                'text': '19 x 19',
                'size': 19,
                'bot': False,
                'bot_vs_bot': False
            },
            {
                'rect': pygame.Rect((WINDOW_SIZE - button_width) // 2, start_y + 3 * (button_height + spacing),
                                    button_width, button_height),
                'text': 'Play with Bot',
                'size': None,
                'bot': True,
                'bot_vs_bot': False
            },
            {
                'rect': pygame.Rect((WINDOW_SIZE - button_width) // 2, start_y + 4 * (button_height + spacing),
                                    button_width, button_height),
                'text': 'Bot vs Bot',
                'size': None,
                'bot': False,
                'bot_vs_bot': True
            }
        ]

    def draw(self):
        self.screen.fill(BROWN)

        title = self.font.render('Menu', True, BLACK)
        title_rect = title.get_rect(centerx=WINDOW_SIZE // 2, y=100)
        self.screen.blit(title, title_rect)

        # Vẽ các nút
        for button in self.buttons:
            pygame.draw.rect(self.screen, WHITE, button['rect'])
            pygame.draw.rect(self.screen, BLACK, button['rect'], 2)

            text = self.font.render(button['text'], True, BLACK)
            text_rect = text.get_rect(center=button['rect'].center)
            self.screen.blit(text, text_rect)

            if button['bot'] and self.play_with_bot:
                pygame.draw.circle(self.screen, GREEN,
                                   (button['rect'].right + 20, button['rect'].centery), 10)
            if button['bot_vs_bot'] and self.bot_vs_bot:
                pygame.draw.circle(self.screen, GREEN,
                                   (button['rect'].right + 20, button['rect'].centery), 10)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for button in self.buttons:
                if button['rect'].collidepoint(mouse_pos):
                    if button['bot']:
                        self.play_with_bot = not self.play_with_bot
                        if self.play_with_bot and self.bot_vs_bot:
                            self.bot_vs_bot = False
                        return False
                    elif button['bot_vs_bot']:
                        self.bot_vs_bot = not self.bot_vs_bot
                        if self.bot_vs_bot and self.play_with_bot:
                            self.play_with_bot = False
                        return False
                    else:
                        self.selected_size = button['size']
                        return True
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None, False, False
                if self.handle_event(event):
                    return self.selected_size, self.play_with_bot, self.bot_vs_bot

            self.draw()
        return None, False, False

