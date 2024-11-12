import matplotlib.pyplot as plt
from .base import Visualizer

class ScatterPlot(Visualizer):
    def __init__(self, data, x_col, y_col):
        super().__init__(data)
        self.x_col = x_col
        self.y_col = y_col

    def plot(self):
        plt.scatter(self.data[self.x_col], self.data[self.y_col])
        plt.xlabel(self.x_col)
        plt.ylabel(self.y_col)
        self.show()
