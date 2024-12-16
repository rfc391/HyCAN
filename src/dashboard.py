# HyCAN: Dashboard Application
# Author: Robert Shubert
# Description: GUI Dashboard for the HyCAN project.

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        show_data_summary(data)
        plot_data(data)

def show_data_summary(data):
    summary_window = tk.Toplevel(root)
    summary_window.title("Data Summary")
    text = tk.Text(summary_window, wrap=tk.WORD, height=20, width=60)
    text.insert(tk.END, str(data.describe()))
    text.pack()

def plot_data(data):
    figure = plt.Figure(figsize=(6, 4), dpi=100)
    ax = figure.add_subplot(111)
    data.plot(kind='bar', ax=ax)
    ax.set_title("Data Visualization")

    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("HyCAN Dashboard")

frame = tk.Frame(root)
frame.pack(pady=20)

load_button = tk.Button(frame, text="Load CSV File", command=load_file)
load_button.pack()

exit_button = tk.Button(frame, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
