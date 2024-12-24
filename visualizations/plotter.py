# Visualization utility for plotting data


def plot_data(data, x_column, y_column):
    """Plots the data using matplotlib."""
    import matplotlib.pyplot as plt
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError("Specified columns must exist in the data.")
    plt.figure(figsize=(8, 6))
    plt.plot(data[x_column], data[y_column], marker='o', linestyle='-')
    plt.title(f"{y_column} vs {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid()
    plt.show()
    

def plot_interactive(data, x_column, y_column):
    """Generates an interactive Plotly plot."""
    from plotly.graph_objects import Figure
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError("Specified columns must exist in the data.")
    fig = create_interactive_plot(data, x_column, y_column)
    fig.show()
