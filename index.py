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
iteration_max_julia = 150
taille_julia = 700
zoom_julia = 1

# =====PARAMS MANDELBROT=====
xMin_mandelbrot = -2
xMax_mandelbrot = 0.5
yMin_mandelbrot = -1.25
yMax_mandelbrot = 1.25
iteration_max_mandelbrot = 142
taille_mandelbrot = 700
zoom_mandelbrot = 1

# =============================== DON'T MODIFY ANYTHING ===============================

COLOR_TABLE = (
    0xf7df, 0xff5a, 0x07ff, 0x7ffa, 0xf7ff, 0xf7bb, 0xff38, 0xff59, 0x001f, 0x895c,
    0xa145, 0xddd0, 0x5cf4, 0x7fe0, 0xd343, 0xfbea, 0x64bd, 0xffdb, 0xd8a7, 0x07ff,
    0x0011, 0x0451, 0xbc21, 0xad55, 0x0320, 0xbdad, 0x8811, 0x5345, 0xfc60, 0x9999,
    0x8800, 0xecaf, 0x8df1, 0x49f1, 0x2a69, 0x067a, 0x901a, 0xf8b2, 0x05ff, 0x6b4d,
    0x1c9f, 0xd48e, 0xb104, 0xffde, 0x2444, 0xf81f, 0xdefb, 0xffdf, 0xfea0, 0xdd24,
    0x8410, 0x0400, 0xafe5, 0xf7fe, 0xfb56, 0xcaeb, 0x4810, 0xfffe, 0xf731, 0xe73f,
    0xff9e, 0x7fe0, 0xffd9, 0xaedc, 0xf410, 0xe7ff, 0xffda, 0xd69a, 0x9772, 0xfdb8,
    0xfd0f, 0x2595, 0x867f, 0x839f, 0x7453, 0xb63b, 0xfffc, 0x07e0, 0x3666, 0xff9c,
    0xf81f, 0x8000, 0x6675, 0x0019, 0xbaba, 0x939b, 0x3d8e, 0x7b5d, 0x07d3, 0x4e99,
    0xc0b0, 0x18ce, 0xf7ff, 0xff3c, 0xff36, 0xfef5, 0x0010, 0xffbc, 0x8400, 0x6c64,
    0xfd20, 0xfa20, 0xdb9a, 0xef55, 0x9fd3, 0xaf7d, 0xdb92, 0xff7a, 0xfed7, 0xcc27,
    0xfe19, 0xdd1b, 0xb71c, 0x8010, 0xf800, 0xbc71, 0x435c, 0x8a22, 0xfc0e, 0xf52c,
    0x2c4a, 0xffbd, 0xa285, 0xc618, 0x867d, 0x6ad9, 0x7412, 0xffdf, 0x07ef, 0x4416,
    0xd5b1, 0x0410, 0xddfb, 0xfb08, 0x471a, 0xec1d, 0xd112, 0xf6f6, 0xffff, 0xf7be,
    0xffe0, 0x9e66, 0x0000
)


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

            color = COLOR_TABLE[n]
            r = ((color >> 11) & 0x1F) << 3
            g = ((color >> 5) & 0x3F) << 2
            b = (color & 0x1F) << 3
            pixels[x, y] = (r, g, b)
            screen.set_at((x, y), (r, g, b))
        # if(n == iteration_max):
        #     screen.set_at((x, y), (0, 0, 0))
        #     pixels[x, y] = ((0, 0, 0))
        # else:
        #     screen.set_at((x, y), ((3 * n) % 256, (1 * n) % 256, (10 * n) % 256))
        #     pixels[x, y] = ((3 * n) % 256, (1 * n) % 256, (10 * n) % 256)

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
