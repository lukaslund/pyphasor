"""
file:       pyphasor.py
author:     lukas lund
url:        https://github.com/lukaslund/pyphasor
"""

from numpy import rad2deg, angle

def print_phasor(x, ID):
	mag = abs(x)
	ang = rad2deg(angle(x))
	print(ID, "=", mag, "/_", ang)