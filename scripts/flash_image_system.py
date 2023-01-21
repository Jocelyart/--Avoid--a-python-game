import pygame

def flashing_damage(img, color):

    mask = pygame.mask.from_surface(img)
    img2 = mask.to_surface() 
    img2.set_colorkey((0, 0, 0))

    w, h = img2.get_size()
    for x in range(w):
        for y in range(h):
            # [0] --> pick one color (R,G,B,A) R = [0], G = [1], B = [2], A = [3]
            # and calculate if the color is not black (0, 0, 0)
            if img2.get_at((x, y))[0] != 0:
                # change the color picked
                img2.set_at((x, y), color)

    return img2