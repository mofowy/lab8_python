import os
import matplotlib.pyplot as plt

class Exporter:
    @staticmethod
    def export_plot(filename):
        output_dir = os.path.dirname(filename)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        plt.savefig(filename, format="png")
        print(f"Plot saved to {filename}")
        plt.show()
        plt.close()