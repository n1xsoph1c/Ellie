import pygame
import pygame.freetype
from pygame.locals import *
import multiprocessing
# from Ellie import main, get_reply, send_text_to_function, get_input_for_funtion
from Ellie import Say, get_reply
from connector import *
from E3P.Ellie_Visual_effect import get_images
import GLOBALS

GLOBALS.initialize() #INITIALIZE GLOBAL VARIBALES

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = (233, 150, 122)

COLOR_CHATBORDER = pygame.Color('dodgerblue2')
# VISUAL_FONT = pygame.font.Font('fonts/Niconne-Regular.ttf', FONT_SIZE)
VISUAL_WIDTH = 200
VISUAL_HEIGHT = 300

SENT_MSG_COLOR = (25, 221, 255)

# IMAGES = get_images()
# IMAGE_COUNT = 0
# IMAGE_AMOUNT = len(IMAGES)
# INPUT_NEEDED = GLOBALS.INPUT_NEEDED
# INPUT_FUNCTION = str()

pygame.init()
screen = pygame.display.set_mode((400, 600))

class InputBox():
    def __init__(self, x, y, w, h, text=''):
        self.screen = screen
        
        self.FONT_SIZE = 32
        self.FONT = pygame.font.Font(None, self.FONT_SIZE)

        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.received_msg = self.FONT.render(text, True, SENT_MSG_COLOR)
        self.active = False

        self.screen.fill((30, 30, 30))
        pygame.display.flip()
        
        pygame.freetype.init()
        self.font = pygame.freetype.Font(None, 20)
        self.font.origin = True
        self.ascender = int(self.font.get_sized_ascender() * 1.5)
        self.descender = int(self.font.get_sized_descender() * 1.5)
        self.line_height = self.ascender - self.descender

    def write_lines(self, text, line=0):
        w, h = self.screen.get_size()
        line_height = self.line_height
        nlines = h // line_height
        if line < 0:
            line = nlines + line
        for i, text_line in enumerate(text.split('\n'), line):
            y = i * line_height + self.ascender
            # Clear the line first.
            self.screen.fill((30, 30, 30), (0, i * line_height, w, line_height))

            # Write new text.
            self.font.render_to(self.screen, (15, y),
                                text_line, Color('blue'))
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    Say(self.text.lower())
                    print(f'Ellie reply: {get_reply()}')
                    self.win.write_lines(get_reply())
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(390, self.txt_surface.get_width()+10)
        self.rect.w = width

        font_width = self.received_msg.get_width()
        # print("Font width: ", width)
        if font_width > 380:
            self.FONT_SIZE -= 10
        else:
            self.FONT_SIZE = 80
            
    def draw(self):
        # Blit the text.
        self.screen.blit(self.txt_surface, (self.rect.x, self.rect.y))
        
        # Blit the rect.
        pygame.draw.rect(self.screen, self.color, self.rect, 2)
    
    def text_analizer(self, text):
        filename = files().open_file("Settings", "data.xml")
        self.INPUT_REQUIRED = XML().read(filename, "input_needed")


        if self.INPUT_REQUIRED == True:
            try:
                with open(files().open_file("Settings", 'data.pickle'), 'rb') as json_file:
                    self.FUNCTION_NAME = pickle.load(json_file)

            except Exception as e: 
                print(f"ERROR_READING_DATA! REASON:{e}")
    
            # Get the function name where input is required
            function_name = self.FUNCTION_NAME
            print(f"INPUT NEEDED TO THE FUNCTION {function_name.__name__}\n")
            print(F"AND THE FUNCTION IS:{function_name}")

            # print(self.FUNCTION_DICT.get("searchMusic"))
            # data = json.loads(self.FUNCTION_DICT)

            Connector().send_input_text_to_function(text.lower(), function_name, MIDDLE_INPUT=text.lower())
        else:
            print("NO INPUTS NEEDED TO ANY FUNCTION!\n")
            # print(f"INPUT NEEDED TO THE FUNCTION {function_name}\n")
            print(f"TYPE OF FUNCTION_DICT:{type(Say)}\n")
            print(F"AND THE FUNCTION IS:{Say}")
            Connector().send_input_text_to_function(text.lower(), Say)

        # if GLOBALS.INPUT_NEEDED:
        #     function_name = get_input_for_funtion() #Get the function name where input is required
        #     send_text_to_function(function_name, self.text.lower())
        #     GLOBALS.INPUT_NEEDED = False
        # else:
        #     send_text_to_function(Say, self.text.lower())

def main():
    clock = pygame.time.Clock()
    box = InputBox(5, 720-60, 250, 32)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            box.handle_event(event)

        box.update()

        screen.fill((30, 30, 30))
        box.draw()

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
#     pygame.quit()