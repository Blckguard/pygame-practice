'''
pygame notes

pygame.init() = initializes pygame, needs to be run at the beginning of script
pygame.display.set_mode((width, height)) = calls the display surface
pygame.display.set_caption(str) = sets the title of the window
pygame.time.Clock() = used to control framerate
.tick(int) = sets highest possible framerate
pygame.event.get() = gets user input
pygame.QUIT = happens when clicking close on window
pygame.quit() = opposite to pygame.init(), does not quit program
pygame.display.update() = updates surfaces
pygame.Surface((width, height)) = creates surface to be displayed on display
.blit(surface, location) = adds surface to display surface
.fill(str) = changes color of surface
pygame.image.load(path) = loads and image as a surface
pygame.font.Font(font type, size) = loads a font
.render(text, AA, color) = renders the font into a surface
.convert() = converts image to different pygame file
.convert_alpha() = converts an image while keeping the alpha values
.get_rect() = gets dimensions of surface and draws rect around it
.left(), .right() et. = gets specified point of rect
rect1.colliderect(rect2) = checks if two rects are colliding
rect1.collidepoint((x,y)) = checks for collision on given location
pygame.mouse.get_pos() = gets position of cursor
pygame.mouse.get_pressed() = checks if mouse buttons are pressed returns: (left, middle, right)
pygame.draw.... = draws rect or other form to screen
pygame.key.get_pressed() = gets the status of all keys
'''