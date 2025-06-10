from typing import Union
import numpy as np
from matplotlib.axes import Axes
from data.elements_coordinates_classic import get_classic_coordinates, get_special_coordinates
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from utils.appearance import get_cmap
from utils.appearance import colors as custom_colors



def plot_periodic_table_from_dict(filename: Union[str, None] = None):
    """Create a base periodic table figure with empty boxes and element symbols.

    Args:
        filename (str, optional): Output filename to save the figure. If None, shows the plot.

    Returns:
        tuple[plt.Figure, plt.Axes]: The matplotlib figure and axes objects.
    """
    special_coords = get_special_coordinates()
    coords = get_classic_coordinates()
    x_vals = [x for x, _ in coords.values()]
    y_vals = [y for _, y in coords.values()]

    x_min, x_max = min(x_vals), max(x_vals)
    y_min, y_max = min(y_vals), max(y_vals)

    fig, ax = plt.subplots(figsize=(x_max - x_min + 2, y_max - y_min + 2))

    for symbol, (x, y) in coords.items():
        rect = patches.Rectangle(
            (x - 0.5, y - 0.5),
            1,
            1,
            edgecolor='black',
            linewidth=1.3,
            facecolor='none'
        )
        ax.add_patch(rect)

    for label, (x, y) in special_coords.items():
        ax.text(x, y, label, ha='center', va='center', fontsize=22)

    ax.set_xlim(x_min - 1, x_max + 1)
    ax.set_ylim(y_min - 1, y_max + 1)
    ax.set_aspect('equal')
    ax.axis('off')

    return fig, ax



def color_elements(ax: Axes, values: dict[str, float]) -> None:
    """Color elements on a periodic table plot using alpha-scaled single custom color,
    and display a horizontal alpha-based color scale at the top center.

    Args:
        ax (Axes): Matplotlib Axes returned from the base plot function.
        values (Dict[str, float]): Dictionary mapping element symbols to numeric values.
    """
    coords = get_classic_coordinates()
    cmap = get_cmap()[10]

    vmin = min(values.values())
    vmax = max(values.values())
               
    norm = Normalize(vmin=vmin, 
                     vmax=vmax)
    cmap_func = plt.get_cmap(cmap)

    for symbol, val in values.items():
        if symbol not in coords:
            continue
        x, y = coords[symbol]
        rgba = cmap_func(norm(val))
        rect = patches.Rectangle(
            (x - 0.5, y - 0.5),
            1, 1,
            facecolor=rgba,
            edgecolor="none",
            zorder=0
        )
        ax.add_patch(rect)
         # determine text color & alpha
        if val == 0:
            txt_color, txt_alpha = 'k', 0.5
        else:
            norm_val = norm(val)  # between 0 and 1
            if norm_val > 0.74:
                txt_color, txt_alpha = 'w', 1.0
            else:
                txt_color, txt_alpha = 'k', 1.0

        ax.text(
            x, y, symbol,
            ha='center', va='center',
            fontsize=24,
            color=txt_color,
            alpha=txt_alpha
        )

    dummy_data = np.linspace(vmin, vmax, 100).reshape(1, -1)  # 1 row, gradient
    im = ax.imshow(dummy_data, extent=[0, 1, 0, 0.1], cmap=cmap, visible=False)

    ticks = np.linspace(vmin, vmax, 4)
    cax = ax.inset_axes((0.19, 0.72, 0.4, 0.02))  # Top center inset
    cbar = plt.colorbar(im, cax=cax, orientation='horizontal', ticks=ticks)
    cbar.ax.tick_params(labelsize=22)


def heatmap_with_labels(ax: Axes, values: dict[str, float]) -> None:
    """Color elements on a periodic table plot using alpha-scaled single custom color,
    and display a horizontal alpha-based color scale at the top center.

    Args:
        ax (Axes): Matplotlib Axes returned from the base plot function.
        values (Dict[str, float]): Dictionary mapping element symbols to numeric values.
    """
    coords = get_classic_coordinates()
    cmap = get_cmap()[10]

    vmin = min(values.values())
    vmax = max(values.values())
               
    norm = Normalize(vmin=vmin, 
                     vmax=vmax)
    cmap_func = plt.get_cmap(cmap)

    for symbol, val in values.items():
        if symbol not in coords:
            continue
        x, y = coords[symbol]
        rgba = cmap_func(norm(val))
        rect = patches.Rectangle(
            (x - 0.5, y - 0.5),
            1, 1,
            facecolor=rgba,
            edgecolor="none",
            zorder=0
        )
        ax.add_patch(rect)
         # determine text color & alpha
        if val == 0:
            txt_color, txt_alpha = 'k', 0.5
        else:
            norm_val = norm(val)  # between 0 and 1
            if norm_val > 0.74:
                txt_color, txt_alpha = 'w', 1.0
            else:
                txt_color, txt_alpha = 'k', 1.0

        ax.text(
            x, 
            y+0.2, 
            symbol,
            ha='center',
            va='center',
            fontsize=22,
            color=txt_color,
            alpha=txt_alpha,
            weight = "bold"
        )
        ax.text(
            x, 
            y-0.2, 
            val,
            ha='center', va='center',
            fontsize=22,
            color=txt_color,
            alpha=txt_alpha
        )
    dummy_data = np.linspace(vmin, vmax, 100).reshape(1, -1)  # 1 row, gradient
    im = ax.imshow(dummy_data, extent=[0, 1, 0, 0.1], cmap=cmap, visible=False)

    ticks = np.linspace(vmin, vmax, 4)
    cax = ax.inset_axes((0.19, 0.72, 0.4, 0.02))  # Top center inset
    cbar = plt.colorbar(im, cax=cax, orientation='horizontal', ticks=ticks)
    cbar.ax.tick_params(labelsize=22)
    #plt.title("mendeleev number", fontsize = 34)
    
