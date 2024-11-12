from src.data_loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizer.line_chart import LineChart
from src.visualizer.bar_chart import BarChart
from src.visualizer.scatter_plot import ScatterPlot
from src.visualizer.multi_plot import MultiPlotVisualizer
from src.exporter import Exporter

# Завантаження даних
loader = DataLoader('data/dataset.csv')
data = loader.load_data()

# Аналіз даних
analyzer = DataAnalyzer(data)
print("Extreme values:\n", analyzer.get_extreme_values())

# Візуалізація
line_chart = LineChart(data, x_col='column1', y_col='column2')
line_chart.plot()

bar_chart = BarChart(data, x_col='column1', y_col='column3')
bar_chart.plot()

scatter_plot = ScatterPlot(data, x_col='column2', y_col='column3')
scatter_plot.plot()

multi_plot = MultiPlotVisualizer(data)
multi_plot.plot_subplots([
    ('line', 'column1', 'column2'),
    ('bar', 'column1', 'column3')
])

# Експорт
Exporter.export_plot('output/visualization.png')
