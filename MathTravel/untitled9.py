# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q29n7IkF3_NtbFlEZGJ2Fl95eFX7zZuR
"""

! pip install git+https://github.com/Ana-Karem-Garcia/Math_Travel

from MathTravel import generar_matriz

ciudades = 10
matriz_costo = generar_matriz(10)


def calcular(ciudad1, ciudad2):
    return matriz_costo[ciudad1][ciudad2]