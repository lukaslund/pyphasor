"""
file:       pyphasor.py
author:     lukas lund
url:        https://github.com/lukaslund/pyphasor
"""

from numpy import rad2deg, deg2rad, angle, exp

def phasor(mag, ang):
	return mag*exp(1j*deg2rad(ang))

def rect2pol(x):
	x_pol = [abs(x), rad2deg(angle(x))]
	return x_pol

def phasor_print(x, ID):
	print(ID, "=", x[0], "/_", x[1])