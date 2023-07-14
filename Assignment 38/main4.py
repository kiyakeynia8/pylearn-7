import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

my_data =pd.read_csv("input/california_cities.csv")

# extracting the data we ar interested in
latitude, longitude = my_data["latd"], my_data["longd"]
population, area = my_data["population_total"], my_data["area_total_km2"]
seaborn.set()
plt.scatter(longitude, latitude, label=None, c=np.log10(population),
            cmap='viridis', s=area, linewidth=0, alpha=0.5)
# plt.axis(aspect='equal')
plt.xlabel('Longitude')
plt.ylabel('Longitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)
# now we will craete a legend, we will plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + 'km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Areas')
plt.title("Area and Population of California my_data")
plt.show()