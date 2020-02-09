import pygame
from libs.PIL import Image

# if Pillow library is installed on your computer
# from PIL import Image

choice = str(input("Julia or Mandelbrot? "))

# =====PARAMS JULIA=====
a = 0.39
b = 0.6
xMin_julia = -1.25
xMax_julia = 1.25
yMin_julia = -1.25
yMax_julia = 1.25
iteration_max_julia = 500
taille_julia = 700
zoom_julia = 1

# =====PARAMS MANDELBROT=====
xMin_mandelbrot = -2
xMax_mandelbrot = 0.5
yMin_mandelbrot = -1.25
yMax_mandelbrot = 1.25
iteration_max_mandelbrot = 100
taille_mandelbrot = 700
zoom_mandelbrot = 1

# =============================== DON'T MODIFY ANYTHING ===============================


def Mandelbrot(xMin=-2, xMax=0.5, yMin=-1.25, yMax=1.25, iteration_max=50, taille=700, zoom=1):
    xmin = xMin / zoom
    xmax = xMax / zoom
    ymin = yMin / zoom
    ymax = yMax / zoom

    im = Image.new('RGB', (taille, taille), (255, 255, 255))
    pixels = im.load()

    pygame.init()
    screen = pygame.display.set_mode((taille, taille))
    pygame.display.set_caption("Mandelbrot's fractal")

    for y in range(taille):
        for x in range(taille):
            Cx = (x * (xmax-xmin) / taille + xmin)
            Cy = (y * (ymin-ymax) / taille + ymax)

            xn = 0
            yn = 0
            n = 0
            while (xn**2+yn**2) < 4 and n < iteration_max:
                save_x = xn
                save_y = yn
                xn = save_x**2 - save_y**2 + Cx
                yn = 2 * save_x * save_y + Cy
                n += 1

            if(n == iteration_max):
                screen.set_at((x, y), (0, 0, 0))
                pixels[x, y] = ((0, 0, 0))
            else:
                screen.set_at((x, y), ((3 * n) % 256, (1 * n) %
                                       256, (10 * n) % 256))
                pixels[x, y] = ((3 * n) % 256, (1 * n) % 256, (10 * n) % 256)

    im.save('fractal_mandelbrot.png')
    # im.show()
    pygame.display.flip()

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                p = pygame.mouse.get_pos()
                px = (p[0] * (xmax - xmin) / taille + xmin)
                py = (p[1] * (ymin - ymax) / taille + ymax)
                print("({};{})".format(px, py))
    pygame.quit()


def Julia(a=0.39, b=0.6, xMin=-1.25, xMax=1.25, yMin=-1.25, yMax=1.25, iteration_max=50, taille=700, zoom=1):
    xmin = xMin / zoom
    xmax = xMax / zoom
    ymin = yMin / zoom
    ymax = yMax / zoom

    im = Image.new('RGB', (taille, taille), (255, 255, 255))
    pixels = im.load()

    pygame.init()
    screen = pygame.display.set_mode((taille, taille))
    pygame.display.set_caption("Julia's fractal")

    for y in range(taille):
        for x in range(taille):
            Cx = xmin+x*(xmax-xmin)/taille
            Cy = ymax-y*(ymax-ymin)/taille
            n = 0
            while (Cx**2+Cy**2) < 4 and n < iteration_max:
                save_x = Cx
                save_y = Cy
                Cx = Cx**2-Cy**2+a
                Cy = 2*save_x*Cy+b
                n += 1

            if(n == iteration_max):
                screen.set_at((x, y), (0, 0, 0))
                pixels[x, y] = (0, 0, 0)
            else:
                screen.set_at((x, y), ((4 * n) % 256, 2 * n, (6 * n) % 256))
                pixels[x, y] = ((4*n) % 256, 2*n, (6*n) % 256)

    im.save('fractal_julia.png')
    # im.show()
    pygame.display.flip()

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                p = pygame.mouse.get_pos()
                px = (p[0] * (xmax - xmin) / taille + xmin)
                py = (p[1] * (ymin - ymax) / taille + ymax)
                print("({};{})".format(px, py))
    pygame.quit()


while choice.lower() != "julia" and choice.lower() != "mandelbrot":
    choice = str(input("Julia ou Mandelbrot? "))

if choice.lower() == "julia":
    print("Generating Julia's fractal")
    Julia(a, b, xMin_julia, xMax_julia, yMin_julia, yMax_julia,
          iteration_max_julia, taille_julia, zoom_julia)
elif choice.lower() == "mandelbrot":
    print("Generating Mandelbrot's fractal !")
    Mandelbrot(xMin_mandelbrot, xMax_mandelbrot, yMin_mandelbrot, yMax_mandelbrot,
               iteration_max_mandelbrot, taille_mandelbrot, zoom_mandelbrot)
