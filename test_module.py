import unittest
import matplotlib
matplotlib.use('Agg')  # Prevents display errors for headless environments

import medical_data_visualizer

class CatPlotTestCase(unittest.TestCase):
    def test_cat_plot_exists(self):
        """Test that draw_cat_plot() returns a matplotlib Figure"""
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertEqual(str(type(fig)), "<class 'matplotlib.figure.Figure'>")


class HeatMapTestCase(unittest.TestCase):
    def test_heat_map_exists(self):
        """Test that draw_heat_map() returns a matplotlib Figure"""
        fig = medical_data_visualizer.draw_heat_map()
        self.assertEqual(str(type(fig)), "<class 'matplotlib.figure.Figure'>")


if __name__ == "__main__":
    unittest.main()
