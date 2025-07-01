import matplotlib.pyplot as plt

def get_colormap_colors(name, num_colors=256):
    """
    Returns a list of RGBA tuples from a matplotlib colormap.

    Parameters:
        name (str): The name of the colormap (e.g. 'viridis', 'plasma', 'tab10').
        num_colors (int): The number of colors to sample from the colormap.

    Returns:
        List of RGBA tuples, each with 4 floats in [0, 1].
    """
    try:
        cmap = plt.get_cmap(name)
        return [cmap(i / (num_colors - 1)) for i in range(num_colors)]
    except ValueError:
        raise ValueError(f"Colormap '{name}' not found in matplotlib.")

def get_colormaps():
    colormaps = plt.colormaps()
    return colormaps
