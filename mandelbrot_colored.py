import numpy as np
import pandas as pd
from numba import jit
import matplotlib.pyplot as plt
import time
import os
from matplotlib.pyplot import figure


# 164 choices
cmaps = ["Accent", "Blues", "BrBG", "BuGn", "BuPu", "CMRmap", "Dark2", "GnBu", "Greens", "Greys", "OrRd", "Oranges", "PRGn", "Paired", "Pastel1", "Pastel2", "PiYG", "PuBu", "PuBuGn",  "PuOr", "PuRd", "Purples", "RdBu", "RdGy", "RdPu", "RdYlBu", "RdYlGn", "Reds",  "Set1", "Set2", "Set3", "Spectral", "Wistia", "YlGn", "YlGnBu",  "YlOrBr", "YlOrRd", "afmhot", "autumn", "binary", "bone", "brg", "bwr", "cividis",
         "cool", "coolwarm", "copper", "cubehelix", "flag", "gist_earth", "gist_gray", "gist_heat", "gist_ncar", "gist_rainbow", "gist_stern", "gist_yarg", "gnuplot", "gnuplot2",  "gray", "hot", "hsv", "inferno", "jet", "magma", "nipy_spectral", "ocean", "pink", "plasma", "prism", "rainbow", "seismic", "spring", "summer", "tab10", "tab20", "tab20b", "tab20c", "terrain", "twilight", "twilight_shifted", "viridis", "winter"]

cmaps_r = ["Accent_r", "Blues_r", "BrBG_r", "BuGn_r", "BuPu_r", "CMRmap_r", "Dark2_r", "GnBu_r", "Greens_r", "Greys_r", "OrRd_r", "Oranges_r", "PRGn_r", "Paired_r", "Pastel1_r", "Pastel2_r", "PiYG_r", "PuBu_r", "PuBuGn_r", "PuOr_r", "PuRd_r", "Purples_r", "RdBu_r", "RdGy_r", "RdPu_r", "RdYlBu_r", "RdYlGn_r", "Reds_r", "Set1_r", "Set2_r", "Set3_r", "Spectral_r", "Wistia_r", "YlGnBu_r", "YlGn_r", "YlOrBr_r", "YlOrRd_r", "afmhot_r", "autumn_r", "binary_r", "bone_r", "brg_r", "bwr_r", "cividis_r",
           "cool_r", "coolwarm_r", "copper_r", "cubehelix_r", "flag_r", "gist_earth_r", "gist_gray_r", "gist_heat_r", "gist_ncar_r", "gist_rainbow_r", "gist_stern_r", "gist_yarg_r", "gnuplot2_r", "gnuplot_r", "gray_r", "hot_r", "hsv_r", "inferno_r", "jet_r", "magma_r", "nipy_spectral_r", "ocean_r", "pink_r", "plasma_r", "prism_r", "rainbow_r", "seismic_r", "spring_r", "summer_r", "tab10_r", "tab20_r", "tab20b_r", "tab20c_r", "terrain_r", "twilight_r", "twilight_shifted_r", "viridis_r", "winter_r"]

resolutions = [[1280, 720], [1920, 1080], [2560, 1440], [4096, 2160]]

print("Résolutions proposées: \n\t1280x720 \n\t1920x1080 \n\t2560x1440 \n\t4096x2160")

print("1: Choisir le nombre de fractales à générer (ou '*' pour générer le maximum)")
print("2: Choisir la résolution ('*' pour choisir toutes les résolutions, un chiffre entre 1 et 4, 'choice' pour choisir la résolution parmis celles proposées ou 'edit' pour une résolution personnalisée)")
print("\tSi un chiffre est saisie, ce seront les permières résolutions qui seront générées. \n\tSi 'choice' est choisie, entrer le chiffre correspondant à la résolution. \n\tSi 'edit' est choisi, entrer la hauteur et la largeur de l'image.")
print("3: Si la génération doit inclure l'inversion des couleurs en plus des couleurs normales saisir yes, sinon saisir autre chose.")

choice_fractals = input("How many fractals? ")
choice_fractals = len(cmaps) if choice_fractals == "*" else choice_fractals

res = input("How many resolutions? ")


if res == "*":
    res = len(resolutions)
elif res == "edit":
    own_width = int(input("Width: "))
    own_height = int(input("Height: "))
elif res == "choice":
    choice_res = int(input(
        "Which resolution (1: 1280x720; 2: 1920x1080; 3: 2560x1440; 4: 4096x2160)? "))
    own_width = resolutions[choice_res-1][0]
    own_height = resolutions[choice_res-1][1]
else:
    if int(res) > len(resolutions):
        res = len(res)
    else:
        res = res

colormap = input("With reverse or not? ")
cmaps += cmaps_r if colormap == "yes" else cmaps


def check_directory(width, height):
    if not os.path.isdir("images"):
        os.makedirs("images")
    if not os.path.isdir("images/{0}x{1}".format(width, height)):
        os.makedirs("images/{0}x{1}".format(width, height))


@jit
def i_iteration(c, iteration_max):
    z = complex(0, 0)
    i = 0
    while(abs(z) < 2 and i < iteration_max):
        z = z**2 + c
        i += 1
    return i


def mandelbrot(height, width, iteration_max, cmap='magma'):
    check_directory(width, height)
    imaginary_start = -1
    imaginary_end = 1
    real_start = -2
    real_end = 1
    set = np.zeros((width, height))
    for h, im in enumerate(np.linspace(imaginary_start, imaginary_end, height)):
        for w, re in enumerate(np.linspace(real_start, real_end, width)):
            set[w, h] = i_iteration(complex(re, im), iteration_max)
    filename = "images/{0}x{1}/{2}_mandlebrot_{3}.png".format(
        width, height, iteration_max, cmap, )
    plt.imsave(filename, set.T, format="png", cmap=cmap)
    return filename


def main():
    start_script = time.time()

    if res == "edit" or res == "choice":
        ran = 1
    else:
        ran = int(res)

    for r in range(ran):
        for i in range(int(choice_fractals)):
            start = time.time()
            figure(dpi=600)
            if res == "edit" or res == "choice":
                width = own_width
            else:
                width = resolutions[r][0]

            if res == "edit" or res == "choice":
                height = own_height
            else:
                height = resolutions[r][1]
            iteration_max = 100
            cmap = cmaps[i]
            print(
                "Generating the fractal number {0} with the {1} color map in {2}x{3} resolution.".format(i, cmap, width, height))
            filename = mandelbrot(height, width, iteration_max, cmap=cmap)
            end = time.time()
            print(f"{filename} saved in time: {end-start}")
            print("")

    end_script = time.time()
    time_diff = round(end_script-start_script)

    if res == "edit" or res == "choice":
        prt = 1
    else:
        prt = int(res)

    print("{0} fractals generated in {1}sec.".format(
        int(choice_fractals)*prt, time_diff))


if __name__ == "__main__":
    main()
