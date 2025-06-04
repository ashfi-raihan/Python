import pygame


def scale_image(img, factor): # to update the size of the img and factor is jei size a update korte chao, komate or barate
    size = round(img.get_width()*factor),round(img.get_height()*factor)
    return pygame.transform.scale(img, size)

# gari gulo k ghuranor jonno 
def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect)