# Fractal_generator

<a href="https://github.com/Zuuriix/fractal_generator"><img src="https://img.shields.io/badge/Repo%3A%20-Fractal%20Generator-green"></a>
<br/>
![release](https://img.shields.io/badge/release-v1.0-blueviolet)
<br/>
![language](https://img.shields.io/badge/Language-Python-blue)
<br/>
<a href="https://github.com/Zuuriix/fractal_generator/"><img src="https://img.shields.io/badge/-LIBRARIES%3A%20-orange"></a>
<a href="https://pypi.org/project/pygame/"><img src="https://img.shields.io/badge/PyPi%3A%20-PyGame-orange"></a>
<a href="https://pypi.org/project/Pillow/"><img src="https://img.shields.io/badge/PyPi%3A%20-Pillow-orange"></a>

<!-- ![license](https://img.shields.io/badge/license-MIT) -->

<br/>

Ce dépôt contient le code source d'un générateur de formes fractales (l'ensemble de **Julia** et de **Mandelbrot**).

<br/>

<p align="center">
	<img src="https://i.imgur.com/JfO1Mtn.png" width="350">
	<br/>
	<h3 align="center">Fractales de Julia</h3>
</p>
<hr>
<hr>
<p align="center">
	<img src="https://i.imgur.com/nZFgTrq.png" width="350">
	<br/>
	<h3 align="center">Fractales de Mandelbrot</h3>
</p>

<hr>

# Utilisation

Le type de fractale sera demandé par le programme.
Le programme va générer une fenêtre affichant le fractale ainsi que sauvegarder dans le dossier du programme une image au format PNG de ce fractale.

Vous trouverez dans le fichier [index.py](https://github.com/Zuuriix/fractal-generator/blob/master/index.py) le morceau
de code permettant de modifier les différents paramètres de la simulation des fractales de Julia et de Mandelbrot:

```python
# ---------------------------- Paramètres du programme pour le fractale de Julia ----------------------------

a = 0.39						# Abscisse du point c
b = 0.6							# Ordonnée du point c
xMin_julia = -1.25					# Abscisse minimale de la zone du plan
xMax_julia = 1.25					# Abscisse maximale de la zone du plan
yMin_julia = -1.25					# Ordonnée minimal de la zone du plan
yMax_julia = 1.25					# Ordonnée maximal de la zone du plan
iteration_max_julia = 50				# Nombre maximal d'itérations
taille_julia = 700					# Taille de la fenêtre
zoom_julia = 1						# Zoom sur le fractal

# -----------------------------------------------------------------------------------------------------------
# ------------------------- Paramètres du programme pour le fractale de Mandelbrot --------------------------

xMin_mandelbrot = -2					# Abscisse minimale de la zone du plan
xMax_mandelbrot = 0.5					# Abscisse maximale de la zone du plan
yMin_mandelbrot = -1.25					# Ordonnée minimal de la zone du plan
yMax_mandelbrot = 1.25					# Ordonnée maximal de la zone du plan
iteration_max_mandelbrot = 50				# Nombre maximal d'itérations
taille_mandelbrot = 700					# Taille de la fenêtre
zoom_mandelbrot = 1					# Zoom sur le fractal

# -----------------------------------------------------------------------------------------------------------
```

<hr>

# Crédits

- [Hecht Axel](https://github.com/hecht-a) : Créateur du projet.
