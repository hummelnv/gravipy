"""Elevation corrections for gravity data."""
import numpy as np


def latitude_correction(g_measured: np.ndarray, lat: np.ndarray) -> np.ndarray:
    return np.zeros_like(g_measured)
#the orthometric height of the Green Building is 41.99 m above the geoid according to https://observablehq.com/@earthscope/geoid-height-calculator/2#code-origin
#geoid model egm2008-5
def free_air_correction(g_measured: np.ndarray) -> np.ndarray:
    return np.zeros_like(g_measured)


def bouguer_plate_correction(g_measured: np.ndarray) -> np.ndarray:
    return np.zeros_like(g_measured)
