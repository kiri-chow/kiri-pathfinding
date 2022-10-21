#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:48:15 2022

@author: anthony
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# names of terrains
TERRAINS = ["glass", "mud", "water", "road", ]
# percentages of different terrains
PERCENTAGES = [70, 20, 8, 2]
# entering costs of different terrains
COST_RATIOS = [2, 4, 10, 1]
# colors to visulize the map
COLORS = ["#5FE849", "#AF6714", "#65C8E1", "#B2AEAA"]
# colormap bases on the COLORS
CMAP = LinearSegmentedColormap.from_list(
    "map_color", colors=COLORS, N=len(COLORS))


def generate_map(height, width, seed=None):
    """
    generate a map in size (height * width)

    params
    ------
    height, width : int,
        the height and width of the map

    returns
    -------
    data: np.ndarray(shape=(height, width)),
        data to describe the map

    terrain meaning please refer global variable : TERRAINS


    """
    np.random.seed(seed)
    data_raw = np.random.rand(height, width)
    data_map = np.zeros_like(data_raw, dtype=int)
    terrain_prob = np.cumsum(PERCENTAGES)
    for ind, prob in enumerate(terrain_prob):
        data_map[data_raw > np.percentile(data_raw, prob)] = ind + 1

    return data_map


def draw_map(data, axes=None):
    """
    visualize the map data

    params
    ------
    data : np.ndarray(dtype=int)
        data to describe a map
    axes : matplotlib.axes.Axes

    returns
    -------
    matplotlib.image.AxesImage

    """
    if axes is None:
        _, axes = plt.subplots()
    return axes.imshow(data, cmap=CMAP)
