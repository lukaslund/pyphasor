"""
file:       pyphasor.py
author:     lukas lund
url:        https://github.com/lukaslund/pyphasor
"""

from numpy import rad2deg, deg2rad, angle, exp

def phasor(mag, ang):
	return mag*exp(1j*deg2rad(ang))

def print_phasor(x, ID):
	mag = abs(x)
	ang = rad2deg(angle(x))
	print(ID, "=", mag, "/_", ang)