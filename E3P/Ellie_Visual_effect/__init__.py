import os
import pygame

def get_images():
        
    current_path = os.path.dirname(__file__) # Where your .py file is located
    image_path = os.path.join(current_path, 'Images') # The resource folder path

    print("loading images")
    image_list = [
        pygame.image.load(os.path.join(image_path,"E00.png")),
        pygame.image.load(os.path.join(image_path, "E01.png")),
        pygame.image.load(os.path.join(image_path, "E02.png")),
        pygame.image.load(os.path.join(image_path, "E03.png")),
        pygame.image.load(os.path.join(image_path, "E04.png")),
        pygame.image.load(os.path.join(image_path, "E05.png")),
        pygame.image.load(os.path.join(image_path, "E06.png")),
        pygame.image.load(os.path.join(image_path, "E07.png")),
        pygame.image.load(os.path.join(image_path, "E08.png")),
        pygame.image.load(os.path.join(image_path, "E09.png")),
        pygame.image.load(os.path.join(image_path, "E10.png")),
        pygame.image.load(os.path.join(image_path, "E11.png")),
        pygame.image.load(os.path.join(image_path, "E12.png")),
        pygame.image.load(os.path.join(image_path, "E13.png")),
        pygame.image.load(os.path.join(image_path, "E14.png")),
        pygame.image.load(os.path.join(image_path, "E15.png")),
        pygame.image.load(os.path.join(image_path, "E16.png")),
        pygame.image.load(os.path.join(image_path, "E17.png")),
        pygame.image.load(os.path.join(image_path, "E18.png")),
        pygame.image.load(os.path.join(image_path, "E19.png")),
        pygame.image.load(os.path.join(image_path, "E20.png")),
        pygame.image.load(os.path.join(image_path, "E21.png")),
        pygame.image.load(os.path.join(image_path, "E22.png")),
        pygame.image.load(os.path.join(image_path, "E23.png")),
        pygame.image.load(os.path.join(image_path, "E24.png")),
        pygame.image.load(os.path.join(image_path, "E25.png")),
        pygame.image.load(os.path.join(image_path, "E26.png")),
        pygame.image.load(os.path.join(image_path, "E27.png")),
        pygame.image.load(os.path.join(image_path, "E28.png")),
        pygame.image.load(os.path.join(image_path, "E29.png")),
        pygame.image.load(os.path.join(image_path, "E30.png")),
        pygame.image.load(os.path.join(image_path, "E31.png")),
        pygame.image.load(os.path.join(image_path, "E32.png")),
        pygame.image.load(os.path.join(image_path, "E33.png")),
        pygame.image.load(os.path.join(image_path, "E34.png")),
        pygame.image.load(os.path.join(image_path, "E35.png")),
        pygame.image.load(os.path.join(image_path, "E36.png")),
        pygame.image.load(os.path.join(image_path, "E37.png")),
        pygame.image.load(os.path.join(image_path, "E38.png")),
        pygame.image.load(os.path.join(image_path, "E39.png")),
        pygame.image.load(os.path.join(image_path, "E40.png")),
        pygame.image.load(os.path.join(image_path, "E41.png")),
        pygame.image.load(os.path.join(image_path, "E42.png")),
        pygame.image.load(os.path.join(image_path, "E43.png")),
        pygame.image.load(os.path.join(image_path, "E44.png")),
        pygame.image.load(os.path.join(image_path, "E45.png")),
        pygame.image.load(os.path.join(image_path, "E46.png")),
        pygame.image.load(os.path.join(image_path, "E47.png")),
        pygame.image.load(os.path.join(image_path, "E48.png")),
        pygame.image.load(os.path.join(image_path, "E49.png")),
        pygame.image.load(os.path.join(image_path, "E50.png")),
        pygame.image.load(os.path.join(image_path, "E51.png")),
        pygame.image.load(os.path.join(image_path, "E52.png")),
        pygame.image.load(os.path.join(image_path, "E53.png")),
        pygame.image.load(os.path.join(image_path, "E54.png")),
        pygame.image.load(os.path.join(image_path, "E55.png")),
        pygame.image.load(os.path.join(image_path, "E56.png")),
        pygame.image.load(os.path.join(image_path, "E57.png")),
        pygame.image.load(os.path.join(image_path, "E58.png")),
        pygame.image.load(os.path.join(image_path, "E59.png")),
        pygame.image.load(os.path.join(image_path, "E60.png")),
        pygame.image.load(os.path.join(image_path, "E61.png")),
        pygame.image.load(os.path.join(image_path, "E62.png")),
        pygame.image.load(os.path.join(image_path, "E63.png")),
        pygame.image.load(os.path.join(image_path, "E64.png")),
        pygame.image.load(os.path.join(image_path, "E65.png")),
        pygame.image.load(os.path.join(image_path, "E66.png")),
        pygame.image.load(os.path.join(image_path, "E67.png")),
        pygame.image.load(os.path.join(image_path, "E68.png")),
        pygame.image.load(os.path.join(image_path, "E69.png")),
        pygame.image.load(os.path.join(image_path, "E70.png")),
        pygame.image.load(os.path.join(image_path, "E71.png")),
        pygame.image.load(os.path.join(image_path, "E72.png"))
    ]
    print("Done Loading the Images..................")

    return image_list



 #------------------|VISUAL LOOP|-------------------
def run():
    fps = 20 #20 frames per second
    width = 1280 #px
    height = 720 #px
    pygame.init()

    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Ellie")

    images = get_images() #Get the images for the visual effect
    count = 0

    while True:
        i = len(images) #The amount of images
        if not count < i:
            count = 0

        surface.blit(images[count], (0,0))
        count += 1
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                break

        clock.tick(fps)
        pygame.display.update()

        # yield

    pygame.quit()
    quit()