import pygame
import pygame.freetype
# from Ellie import Say, get_reply

screen_height = 600
screen_width = 400 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Elli3")

def Color(name):
    if name == "white":
        return (255, 255, 255)

    if name == "blue":
        return (0, 132, 255) 

    if name == "graphite":
        return (93, 95, 97)

    if name == "rubber-blue":
        return (219, 230, 241)

    if name == "tomato":
        return (250, 32, 69)
    
    if name == "orange":
        return (255, 102, 0)

    if name == "light-smoke":
        return (225, 229, 233)

    if name == "dark":
        return (58, 63, 68)

class display:
    def __init__(self, screen):
        pygame.init()
        pygame.freetype.init()

        self.screen = screen
        self.screen.fill(Color("dark"))
        pygame.display.flip()
        self.font_size = 30
        self.font = pygame.freetype.Font(None, self.font_size)
        self.font.origin = True
        self.ascender = int(self.font.get_sized_ascender() * 1.5)
        self.descender = int(self.font.get_sized_descender() * 1.5)
        self.line_height = self.ascender - self.descender

    def write_lines(self, text, line=0):
        w, h = self.screen.get_size()
        f = pygame.font.Font(None, self.font_size)

        line_height = self.line_height
        nlines = h // line_height
        if line < 0:
            line = nlines + line
        for i, text_line in enumerate(text.split('\n'), line):
            y = i * line_height + self.ascender
            # Clear the line first.
            self.screen.fill(Color("dark"), (0, i * line_height, w, line_height))

            tw = f.render(text_line, False, (0,0,0)).get_width()
            th = f.render(text_line, False, (0,0,0)).get_height()
            if tw < 320:
            # Write new text.
                self.font.render_to(self.screen, (15, y),
                                text_line, Color("light-smoke"))
            else:
                self.font.render_to(self.screen, (15, y + th),  
                                text_line, Color("light-smoke"))
                th = 0

        pygame.display.flip()

    def get_screen(self):
        return self.screen

    def get_font(self):
        return self.font
        

def main():
    clock = pygame.time.Clock()
    done = False
    
    win = display(screen)
    box = InputBox(screen, 1, screen_height - 41, 40, screen_width - 2)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            # box.update()
            box.handle_event(event)
        
        box.draw()

        text = "\n\n\n\n                  ELLI3\n Your Personal Assistant"
        win.write_lines(text)
        win.write_lines(box.output())

        # screen.fill((30, 30, 30))
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
#     pygame.quit()
