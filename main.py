from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Save both plots as image files
cat_plot = draw_cat_plot()
cat_plot.savefig('catplot.png')

heatmap = draw_heat_map()
heatmap.savefig('heatmap.png')
