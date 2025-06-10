import pandas as pd
from data.elements_coordinates_classic import get_classic_coordinates
from data.mendeleev_numbers import get_mendeleev_numbers
from utils.plotter import plot_periodic_table_from_dict, color_elements, heatmap_with_labels

if __name__ == "__main__":
    values = get_mendeleev_numbers()
    fig, ax = plot_periodic_table_from_dict()
    # color_elements(ax, values)
    # fig.savefig("mendeleev_colored_table.png", dpi=500, bbox_inches="tight")
    heatmap_with_labels(ax, values)
    fig.savefig("mendeleev_colored_table_numbers.png", dpi=500, bbox_inches="tight")